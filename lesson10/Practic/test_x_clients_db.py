import allure
from CompanyApi import CompanyApi
from CompanyTable import CompanyTable


@allure.epic("компании")
@allure.severity("blocker")
class TestCompany:

    api = CompanyApi("http://5.101.50.27:8000")
    db = CompanyTable("postgresql://qa:skyqa@5.101.50.27:5432/x_clients")

    @allure.id("SKYPRO-1")
    @allure.story("Получение списка компаний")
    @allure.feature("READ")
    @allure.epic("компании")
    @allure.title("Получение списка организаций")
    def test_get_companies(self):
        api_result = self.api.get_company_list()
        db_result = self.db.get_companies()
        assert len(api_result) == len(db_result)

    @allure.id("SKYPRO-2")
    @allure.story("Получение списка компаний")
    @allure.feature("READ")
    @allure.title("Получение списка активных организаций")
    @allure.description("Запрос организация с параметром active = true")
    # получение активных компаний в классе CompanyTable
    def test_get_active_companies(self):
        filtered_list = self.api.get_company_list(
            params_to_add={"active": "true"})
        db_list = self.db.get_active_companies()

        assert len(filtered_list) == len(db_list)

    @allure.id("SKYPRO-3")
    @allure.story("Создание компаний")
    @allure.feature("CREATE")
    @allure.title("Создание организации")
    def test_add_new(self):
        with allure.step("Получить количество организаций ДО"):
            body_before = self.api.get_company_list()
            len_before = len(body_before)

        with allure.step("Создать организацию"):
            with allure.step("Сгенерировать название"):
                name = "Autotest"
                descr = "Descr"

            with allure.step("Вызвать API-метод для создания"):
                result = self.api.create_company(name, descr)
                new_id = result["id"]

        with allure.step("Получить список организаций ПОСЛЕ создания"):
            body_after = self.api.get_company_list()
            len_after = len(body_after)

        with allure.step("Проверить, что список ДО меньше списка ПОСЛЕ на 1"):
            assert len_after - len_before == 1

        with allure.step("Удалить из БД новую организацию"):
            self.db.delete(new_id)

        with allure.step(
                "Проверить поля новой организации. Корректно заполнены"):
            found = False
            for company in body_after:
                if company["name"] == name:
                    assert company["description"] == descr
                    found = True
                    break

            assert found, f"Компания с названием '{name}' не найдена в списке"
