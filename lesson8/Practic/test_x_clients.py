from CompanyApi import CompanyApi


api = CompanyApi("http://5.101.50.27:8000")


def test_get_companies():
    body = api.get_company_list()
    assert len(body) > 0


# Проверка получения активных компаний
def test_get_active_companies():
    full_list = api.get_company_list()
    filtered_list = api.get_company_list(params_to_add={"active": "true"})
    assert len(full_list) > len(filtered_list)


# Проверка добавления новой компании
def test_add_new():
    body = api.get_company_list()
    len_before = len(body)
    name = "Autotest"
    descr = "Descr"
    api.create_company(name, descr)

    body = api.get_company_list()
    len_after = len(body)

    assert len_after - len_before == 1
    assert body[-1]["name"] == name
    assert body[-1]["description"] == descr
