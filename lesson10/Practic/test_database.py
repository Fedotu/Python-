from sqlalchemy import create_engine, inspect, text


db_connection_string = "postgresql://qa:skyqa@5.101.50.27:5432/x_clients"
db = create_engine(db_connection_string)
# create_engine принимает в качестве аргумента строку подключения
# «разбивает» ее на компоненты, передает их на сервер
# и устанавливает соединение с базой данных


# Используем инспектор для получения информации о таблицах
def test_db_connection():
    inspector = inspect(db)
    names = inspector.get_table_names()
    assert names[1] == 'students'


def test_select():
    connection = db.connect()
    result = connection.execute(text("SELECT * FROM company"))
    rows = result.mappings().all()
    row1 = rows[0]

    assert row1['id'] == 1
    assert row1['name'] == "QA Студия 'ТестировщикЪ'"

    connection.close()


def test_select_1_row_with_two_filters():
    connection = db.connect()
    sql_statement = text("SELECT * FROM company "
                         "WHERE \"is_active\" = :is_active AND id >= :id")
    result = connection.execute(sql_statement, {"id": 1, "is_active": True})
    rows = result.mappings().all()

    assert len(rows) == 40


# Она запишет в таблицу company новую компанию.
def test_insert():
    connection = db.connect()
    transaction = connection.begin()

    sql = text("INSERT INTO company(\"name\") VALUES (:new_name)")
    connection.execute(sql, {
        'new_name': "Skypro"
        })

    transaction.commit()
    connection.close()


# изменит описание компании
def test_update():
    connection = db.connect()
    transaction = connection.begin()

    sql = text("UPDATE company SET description = :descr WHERE id = :id")
    connection.execute(sql, {"descr": 'New descr', "id": 10})

    transaction.commit()
    connection.close()


# удалит компанию из таблицы
def test_delete():
    connection = db.connect()
    transaction = connection.begin()

    sql = text("DELETE FROM company WHERE id = :id")
    connection.execute(sql, {"id": 156})

    transaction.commit()
    connection.close()
