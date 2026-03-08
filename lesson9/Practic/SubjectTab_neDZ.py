from sqlalchemy import create_engine, text
# Оператор with — это «предохранитель».
# Что бы ни случилось внутри блока (ошибка, return, break),
# как только код выходит за пределы отступа with,
# он автоматически вызывает закрытие соединения.
# Тебе не нужно писать conn.close()


class SubjectTab:
    _scripts = {
            "get_max_id": text("SELECT MAX(subject_id) FROM subject"),
            "insert": text(
                "INSERT INTO subject "
                "(subject_id, subject_title) VALUES (:id, :title)"),
            "select_by_id": text(
                "SELECT * FROM subject WHERE subject_id = :id"),
            "delete_by_id": text("DELETE FROM subject WHERE subject_id = :id"),
            "update": text("""
                           UPDATE subject
                           SET subject_title = :new_title
                           WHERE subject_id = :id
                           """)
        }

    def __init__(self, connection_string):
        self.__db = create_engine(connection_string)

    def get_next_id(self):
        with self.engine.connect() as conn:
            result = conn.execute(self._scripts["get_max_id"]).scalar()
            return (result if result is not None else 0) + 1

    def create(self, title):
        next_id = self.get_next_id()
        with self.engine.connect() as conn:
            conn.execute(self._scripts["insert"],
                         {"id": next_id, "title": title})
            conn.commit()
            return next_id

    def get_by_id(self, subject_id):
        with self.engine.connect() as conn:
            result = conn.execute(self._scripts["select_by_id"],
                                  {"id": subject_id})
            return result.mappings().first()

    def delete(self, subject_id):
        with self.engine.connect() as conn:
            conn.execute(self._scripts["delete_by_id"], {"id": subject_id})
            conn.commit()

    def update(self, subject_id, new_title):
        with self.engine.connect() as conn:
            conn.execute(self._scripts["update"],
                         {"id": subject_id, "new_title": new_title})
            conn.commit()
