import requests

base_url = "https://ru.yougile.com"

# данные для тестов
# Добавить данные из сообщения

# для негативных проверок
WRONG_PASSWORD = "wrong_password"
WRONG_COMPANY_ID = "0jtb59ji-159k-gdu4-huks-hik5964olhf5"
WRONG_PROJECT_ID = "1ujftgs1-185u-tspj-ljt5-659lhuj596kw"
WRONG_TOKEN = "invalid_token_12345"


class YougileApi:

    def __init__(self, token=None):
        self.token = token
        self.base_url = base_url
        self.headers = {'Content-Type': 'application/json'}
        if token:
            self.headers['Authorization'] = f'Bearer {token}'

    def get_companies(self, login, password):
        data = {"login": login, "password": password}
        return requests.post(f"{self.base_url}/api-v2/auth/companies",
                             json=data)

    def get_token(self, login, password, company_id):
        data = {"login": login, "password": password, "companyId": company_id}
        return requests.post(f"{self.base_url}/api-v2/auth/keys", json=data)

    def get_users(self):
        return requests.get(f"{self.base_url}/api-v2/users",
                            headers=self.headers)

    def create_project(self, title, users):
        data = {"title": title, "users": users}
        return requests.post(f"{self.base_url}/api-v2/projects", json=data,
                             headers=self.headers)

    def get_project_by_id(self, project_id):
        return requests.get(f"{self.base_url}/api-v2/projects/{project_id}",
                            headers=self.headers)

    def update_project(self, project_id, title, users, deleted=False):
        data = {"deleted": deleted, "title": title, "users": users}
        return requests.put(f"{self.base_url}/api-v2/projects/{project_id}",
                            json=data, headers=self.headers)
