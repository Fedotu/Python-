import requests

base_url = "http://5.101.50.27:8000"


def test_simple_req():
    resp = requests.get(base_url + '/company/list')

    response_body = resp.json()
    first_company = response_body[0]

    assert first_company["name"] == "QA Студия 'ТестировщикЪ'"
    # Проверяем статус-код в ответе:
    assert resp.status_code == 200
    assert resp.headers["Content-Type"] == "application/json"


def test_auth():
    creds = {
        'username': 'harrypotter',
        'password': 'expelliarmus'
    }
    resp = requests.post(base_url + '/auth/login', json=creds)
    assert resp.json()["user_token"] is not None
    assert resp.status_code == 200


def test_create_company():
    creds = {
        'username': 'harrypotter',
        'password': 'expelliarmus'
    }
    company = {
        "name": "python",
        "description": "requests"
    }
# авторизация
    resp = requests.post(base_url + '/auth/login', json=creds)
    assert resp.json()["user_token"]
# создание
    resp = requests.post(base_url + '/company/create',
                         json=company)
    assert resp.status_code == 201
