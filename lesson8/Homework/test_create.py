from YougileApi import YougileApi, LOGIN, PASSWORD, COMPANY_ID, \
    USER_ID, WRONG_PASSWORD, PROJECT_ID


# получения компаний
def test_get_companies():
    api = YougileApi()
    resp = api.get_companies(LOGIN, PASSWORD)
    assert resp.status_code == 200


# получения пользователей
def test_get_users():
    api = YougileApi()

    resp = api.get_users()
    assert resp.status_code == 200


# создания проекта
def test_create_project():
    # Создаем проект
    api = YougileApi()
    project_data = {
        "title": "ГосУслуги",
        "users": {USER_ID: "admin"}
    }

    resp = api.create_project(project_data["title"], project_data["users"])

    assert resp.status_code == 201


def test_update_project():

    api = YougileApi()
    project_data = {
        "title": "Delete",
        "users": {USER_ID: "admin"}
    }

    resp = api.create_project(project_data["title"], project_data["users"])

    # Обновляем проект
    project_delete = {
        "deleted": True,
        "title": "Delete",  # Имя
        "users": {USER_ID: "admin"}
    }

    resp = api.update_project(
        PROJECT_ID,
        project_delete["title"],
        project_delete["users"],
        project_delete["deleted"]
    )

    assert resp.status_code == 200

# негативные проверки


# получения токена
def test_get_token():
    api = YougileApi()
    resp = api.get_token(LOGIN, PASSWORD, COMPANY_ID)
    print(resp.status_code)
    print(resp.text)

    assert resp.status_code == 201

# получения пользователей


def test_get_user():
    # Получаем токен
    api = YougileApi()

    resp = api.get_users()
    print("Статус:", resp.status_code)
    print("Список пользователей:", resp.text)

    assert resp.status_code == 200


# обновления проекта
def test_update_projects():
    # Обновляем проект
    api = YougileApi()
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
    token = token_resp.json()

    api = YougileApi(token)
    project_data = {
        "title": "",
        "users": {USER_ID: "admin"}
    }

    resp = api.create_project(project_data["title"], project_data["users"])
    print(f"Статус: {resp.status_code}")
    print(f"Ответ: {resp.text}")

    assert resp.status_code == 401
