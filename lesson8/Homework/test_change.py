from test_yougile import YougileApi, LOGIN, PASSWORD, COMPANY_ID, \
    USER_ID, PROJECT_ID, WRONG_PROJECT_ID


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

    api = YougileApi(token)
    resp = api.get_users()
    print("Статус:", resp.status_code)
    print("Список пользователей:", resp.text)

    assert resp.status_code == 200


# обновления проекта
def test_update_project():
    # Получаем токен
    api = YougileApi()
    token_resp = api.get_token(LOGIN, PASSWORD, COMPANY_ID)
    token = token_resp.json()["key"]
    assert token

    # Обновляем проект
    api = YougileApi(token)
    project_data = {
        "deleted": False,
        "title": "ГосУслуги",
        "users": {USER_ID: "admin"}
    }

    resp = api.update_project(
        PROJECT_ID,
        project_data["title"],
        project_data["users"],
        project_data["deleted"]
    )

    print(resp.status_code)
    print(resp.text)

    assert resp.status_code == 200


# негативные проверки

# несуществующий проект
def test_update_project_negative_not_found():
    api = YougileApi()
    token_resp = api.get_token(LOGIN, PASSWORD, COMPANY_ID)
    token = token_resp.json()["key"]

    api = YougileApi(token)
    resp = api.update_project(WRONG_PROJECT_ID, "Тест", {USER_ID: "admin"})

    print(f"Статус: {resp.status_code}")
    print(f"Ответ: {resp.text}")

    assert resp.status_code == 404


# пустое название
def test_update_project_negative_empty_title():
    api = YougileApi()
    token_resp = api.get_token(LOGIN, PASSWORD, COMPANY_ID)
    token = token_resp.json()["key"]

    api = YougileApi(token)
    resp = api.update_project(PROJECT_ID, "", {USER_ID: "admin"})

    print(f"Статус: {resp.status_code}")
    print(f"Ответ: {resp.text}")

    assert resp.status_code == 400
