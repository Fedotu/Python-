import allure
from sqlalchemy import create_engine, text


class CompanyTable:

    __scripts = {
        "select": text("SELECT * FROM company WHERE deleted_at IS NULL"),
        "select only active": text(
            "SELECT * FROM company "
            "WHERE \"is_active\" = true "
            "AND deleted_at IS NULL"
        ),
        "delete by id": text("DELETE FROM company WHERE id = :id_to_delete"),
    }

    def __init__(self, connection_string):
        self.__db = create_engine(connection_string)

    @allure.step("БД. Создание следующего {id} + 1")
    def get_companies(self):
        conn = self.__db.connect()
        result = conn.execute(self.__scripts["select"])
        rows = result.mappings().all()
        conn.close()
        return rows

    @allure.step("БД. Список активных компаний]")
    def get_active_companies(self):
        conn = self.__db.connect()
        result = conn.execute(self.__scripts["select only active"])
        rows = result.mappings().all()
        conn.close()
        return rows

    @allure.step("БД. Удалить организацию по {id}")
    def delete(self, id):
        conn = self.__db.connect()

        # Получаем SQL запрос и в строку
        sql_query = str(self.__scripts["delete by id"])
        params = {"id_to_delete": id}

        # Добавляем вложение с SQL запросом
        allure.attach(
            sql_query,
            name="SQL запрос",
            attachment_type=allure.attachment_type.TEXT
        )

        # Добавляем вложение с параметрами
        allure.attach(
            str(params),
            name="Параметры запроса",
            attachment_type=allure.attachment_type.TEXT
        )

        conn.execute(self.__scripts["delete by id"], params)
        conn.commit()
        conn.close()
