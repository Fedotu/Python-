import pytest
from SubjectTab import SubjectTab

db = SubjectTab("postgresql://postgres:111@localhost:5432/postgres")


@pytest.fixture
def subject():
    sid = db.create("Base_Test_Subject")
    yield sid
    db.delete(sid)  # точное удаление, при любых условиях


def test_add_subject():
    name = "Anatomic"
    new_id = db.create(name)
    res = db.get_by_id(new_id)
    assert res["subject_title"] == name
    db.delete(new_id)


def test_update_subject(subject):
    new_title = "New_Anatomic"
    db.update(subject, new_title)
    res = db.get_by_id(subject)
    assert res["subject_title"] == new_title


def test_delete_subject():
    new_id = db.create("For_Delete")
    db.delete(new_id)
    res = db.get_by_id(new_id)
    assert res is None  # проверка удаления
