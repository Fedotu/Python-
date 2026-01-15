import pytest

from string_utils import StringUtils


string_utils = StringUtils()


# тесты для capitalize


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python"),
    ("тест", "Тест"),
    ("123abc", "123abc"),
    ("a", "A"),
    ("SKYPRO", "Skypro"),
    (" hello", " hello")
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("", ""),
    ("   ", "   "),
])
def test_capitalize_negative(input_str, expected):
    """Тесты на дефекты - ожидаем падение"""
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.xfail(reason="capitalize() делает остальные буквы строчными")
@pytest.mark.parametrize("input_str, expected", [
    ("hELLO", "HELLO"),
    ("PyThOn", "PyThOn"),
    (" World", " world"),
])
def test_capitalize_preserves_case_xfail(input_str, expected):
    """capitalize() не сохраняет регистр остальных букв"""
    assert string_utils.capitalize(input_str) == expected


# тесты для trim


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("   skypro", "skypro"),
    ("  hello world  ", "hello world  "),
    ("", ""),
    ("тест", "тест"),
    ("    ", ""),
    ("  a", "a"),
])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.negative
@pytest.mark.xfail(raises=AttributeError, strict=True)
@pytest.mark.parametrize("input_str", [
    None,
    123,
    ["   test"]
])
def test_trim_negative_wrong_type(input_str):
    """Тесты на дефекты - ожидаем падение"""
    string_utils.trim(input_str)


# тесты для contains


@pytest.mark.positive
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "S", True),
    ("SkyPro", "k", True),
    ("SkyPro", "Pro", True),
    ("Hello World", " ", True),
    ("", "", True),
    ("   ", " ", True),
    ("123", "2", True),
    ("тест", "е", True),
])
def test_contains_positive(string, symbol, expected):
    assert string_utils.contains(string, symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "U", False),
    ("", "a", False),
    ("a", " ", False),
    ("Hello", "hello", False),
    ("test", "z", False),
])
def test_contains_negative(string, symbol, expected):
    """Тесты на дефекты - ожидаем падение"""
    assert string_utils.contains(string, symbol) == expected


@pytest.mark.negative
@pytest.mark.xfail(raises=(AttributeError, TypeError), strict=True)
@pytest.mark.parametrize("string, symbol", [
    (None, "a"),
    ("test", None),
    (123, "2"),
])
def test_contains_negative_wrong_type(string, symbol):
    """Тесты на дефекты - ожидаем падение"""
    string_utils.contains(string, symbol)


# тесты для delete


@pytest.mark.positive
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "k", "SyPro"),
    ("SkyPro", "Pro", "Sky"),
    ("Hello World", " ", "HelloWorld"),
    ("aaa", "a", ""),
    ("ababab", "ab", ""),
    ("test", "e", "tst"),
    ("12345", "3", "1245"),
    ("", "a", ""),
    ("test", "", "test")
])
def test_delete_symbol_positive(string, symbol, expected):
    assert string_utils.delete_symbol(string, symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "X", "SkyPro"),
    ("", "", ""),
    ("   ", "a", "   ")
])
def test_delete_symbol_negative(string, symbol, expected):
    """Тесты на дефекты - ожидаем падение"""
    assert string_utils.delete_symbol(string, symbol) == expected


@pytest.mark.negative
@pytest.mark.xfail(raises=(AttributeError, TypeError), strict=True)
@pytest.mark.parametrize("string, symbol", [
    (None, "a"),
    ("test", None),
])
def test_delete_symbol_negative_wrong_type(string, symbol):
    """Тесты на дефекты - ожидаем падение"""
    string_utils.delete_symbol(string, symbol)


# интеграционные тесты


@pytest.mark.integration
def test_chained_operations():
    result = string_utils.trim("   hello world ")
    result = string_utils.capitalize(result)
    result = string_utils.delete_symbol(result, "o")
    assert result == "Hell wrld "


@pytest.mark.integration
def test_all_methods_together():
    text = "   skypro is awesome   "
    text = string_utils.trim(text)
    text = string_utils.capitalize(text)
    text = string_utils.delete_symbol(text, " ")
    assert string_utils.contains(text, "Skypro")
    assert not string_utils.contains(text, " ")
    assert text == "Skyproisawesome"
