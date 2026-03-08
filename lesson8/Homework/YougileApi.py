import requests

base_url = "https://ru.yougile.com"

# данные для тестов
# Добавить данные из сообщения
# LOGIN = "fedotu.00@gmail.com"
# PASSWORD = "DNN4g535TJ_ZZdv"
# COMPANY_ID = "e2f9f107-11e9-491d-9d33-8e20f0a83689"
# USER_ID = "bc41dced-060b-4d60-83ef-ea733ae0b53d"
# PROJECT_ID = "b4e199b9-4af4-4ee1-a24f-17f572964f01"
MY_KEY = "zCEWBmLoq2KEJV41mnvKn39CEXK8eoJ+A1sw8BwvEj-leAxLfvEJNQmWDKIDLDLm"
LOGIN = "5cicbwd24r@zudpck.com"
PASSWORD = "12345Qwerty"
COMPANY_ID = "ce00c8c0-53d4-4cc0-925d-6f0194d558c8"
USER_ID = "9cb5b2fc-ca2c-4a01-bafc-103ae55d2a57"
PROJECT_ID = "87ce7009-7085-491f-a93f-f0068b64bf6e"

# для негативных проверок
WRONG_PASSWORD = "wrong_password"
WRONG_COMPANY_ID = "0jtb59ji-159k-gdu4-huks-hik5964olhf5"
WRONG_PROJECT_ID = "1ujftgs1-185u-tspj-ljt5-659lhuj596kw"
WRONG_TOKEN = "invalid_token_12345"


class YougileApi:

    def __init__(self):
        self.token = MY_KEY
        self.base_url = base_url
        self.headers = {'Content-Type': 'application/json',
                        'Authorization': f'Bearer {self.token}'
                        }

    def delete_token(self, user_key):
        return requests.delete(f"{self.base_url}/api-v2/auth/keys/keys/{
            user_key}",)

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

    def update_project(self, project_id, title, users, deleted=True):
        data = {"deleted": deleted, "title": title, "users": users}
        return requests.put(f"{self.base_url}/api-v2/projects/{project_id}",
                            json=data, headers=self.headers)

# curl --request PUT \
#   --url https://ru.yougile.com/api-v2/projects/id \
#   --header 'Authorization: Bearer undefined' \
#   --header 'Content-Type: application/json' \
#   --data '{
#   "deleted": true,
#   "title": "ГосУслуги",
#   "users": {
#     "4902b994-b806-4af4-acec-018ea5ea6468": "worker",
#     "8aeaeb9d-f94e-4c66-96d3-eb8d96fe7018":
#         "ee88efd5-5cb2-41a0-9ea2-295da25863d4"
#   }
# }'
