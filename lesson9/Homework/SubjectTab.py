from sqlalchemy import create_engine, text


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
        self.db = create_engine(connection_string)

    def get_next_id(self):  # ищем мах id +1
        conn = self.db.connect()
        result = conn.execute(self._scripts["get_max_id"]).scalar()
        conn.close()
        return (result if result is not None else 0) + 1

    def create(self, title):
        next_id = self.get_next_id()
        conn = self.db.connect()
        conn.execute(
            self._scripts["insert"],
            {"id": next_id, "title": title}
        )
        conn.commit()
        conn.close()
        return next_id

    def get_by_id(self, subject_id):
        conn = self.db.connect()
        result = conn.execute(
            self._scripts["select_by_id"],
            {"id": subject_id}
        )
        row = result.mappings().first()
        conn.close()
        return row

    def delete(self, subject_id):
        conn = self.db.connect()
        conn.execute(
            self._scripts["delete_by_id"],
            {"id": subject_id}
        )
        conn.commit()
        conn.close()

    def update(self, subject_id, new_title):
        conn = self.db.connect()
        conn.execute(
            self._scripts["update"],
            {"id": subject_id, "new_title": new_title}
        )
        conn.commit()
        conn.close()
