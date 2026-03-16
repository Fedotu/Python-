from YougileApi import YougileApi, LOGIN, PASSWORD, COMPANY_ID, \
    PROJECT_ID, WRONG_PROJECT_ID


# получения токена
def test_get_token():
    api = YougileApi()
    resp = api.get_token(LOGIN, PASSWORD, COMPANY_ID)
    print(resp.status_code)
    print(resp.text)

    assert resp.status_code == 201


# получения проекта по ID
def test_get_by_id():
    # Получаем токен
    api = YougileApi()
    token_resp = api.get_token(LOGIN, PASSWORD, COMPANY_ID)
    token = token_resp.json()["key"]
    assert token

    # Получаем проект по ID
    api = YougileApi(token)
    resp = api.get_project_by_id(PROJECT_ID)
    print(resp.status_code)
    print(resp.text)

    assert resp.status_code == 200


# негативные проверки

# несуществующий проект
def test_get_by_id_negative_not_found():
    api = YougileApi()
    token_resp = api.get_token(LOGIN, PASSWORD, COMPANY_ID)
    token = token_resp.json()["key"]

    api = YougileApi(token)
    resp = api.get_project_by_id(WRONG_PROJECT_ID)
    print(f"Статус: {resp.status_code}")
    print(f"Ответ: {resp.text}")

    assert resp.status_code == 404


# пустой ID
def test_get_by_id_negative_empty_id():
    api = YougileApi()
    token_resp = api.get_token(LOGIN, PASSWORD, COMPANY_ID)
    token = token_resp.json()["key"]

    api = YougileApi(token)
    resp = api.get_project_by_id("")
    print(f"Статус: {resp.status_code}")
    print(f"Ответ: {resp.text}")

    assert resp.status_code == 405
