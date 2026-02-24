from test_yougile import YougileApi, LOGIN, PASSWORD, COMPANY_ID, \
    USER_ID, WRONG_PASSWORD


# получения компаний
def test_get_companies():
    api = YougileApi()
    resp = api.get_companies(LOGIN, PASSWORD)
    assert resp.status_code == 200
    companies = resp.json()
    print(f"Your companies: {companies}")


# получения токена
def test_get_token():
    api = YougileApi()
    resp = api.get_token(LOGIN, PASSWORD, COMPANY_ID)
    print(resp.status_code)
    print(resp.text)

    assert resp.status_code == 201


# получения пользователей
def test_get_users():
    # Получаем токен
    api = YougileApi()
    token_resp = api.get_token(LOGIN, PASSWORD, COMPANY_ID)
    token = token_resp.json()["key"]

    # Получаем пользователей
    api = YougileApi(token)
    resp = api.get_users()
    print("Статус:", resp.status_code)
    print("Список пользователей:", resp.text)

    assert resp.status_code == 200


# создания проекта
def test_create_project():
    # Получаем токен
    api = YougileApi()
    token_resp = api.get_token(LOGIN, PASSWORD, COMPANY_ID)
    token = token_resp.json()["key"]
    assert token

    # Создаем проект
    api = YougileApi(token)
    project_data = {
        "title": "ГосУслуги",
        "users": {USER_ID: "admin"}
    }

    print("Отправляемые данные:", project_data)
    resp = api.create_project(project_data["title"], project_data["users"])
    print(resp.status_code)
    print(resp.text)

    assert resp.status_code == 201


# негативные проверки

# неверный пароль
def test_get_companies_negative_wrong_password():
    api = YougileApi()
    resp = api.get_companies(LOGIN, WRONG_PASSWORD)
    print(f"Статус: {resp.status_code}")
    print(f"Ответ: {resp.text}")

    assert resp.status_code == 401


# пустое название проекта
def test_create_project_negative_empty_title():
    api = YougileApi()
    token_resp = api.get_token(LOGIN, PASSWORD, COMPANY_ID)
    token = token_resp.json()["key"]

    api = YougileApi(token)
    project_data = {
        "title": "",
        "users": {USER_ID: "admin"}
    }

    resp = api.create_project(project_data["title"], project_data["users"])
    print(f"Статус: {resp.status_code}")
    print(f"Ответ: {resp.text}")

    assert resp.status_code == 400
