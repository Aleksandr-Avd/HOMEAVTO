import pytest

from string_utils import StringUtils

string_utils = StringUtils()


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python"),
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
    assert string_utils.capitalize(input_str) == expected

@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    (" Hello World", "Hello World"),
    (" 123", "123"),
    ("  Skypro", "Skypro"),
])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected

@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected",[ 
    ("  Hello World! ", "Hello World! "),
    ("123  ", "123  "),
    ("  ", "")
])
def test_trim_negative(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.positive
@pytest.mark.parametrize("input_str, symbol, expected_result", [ 
    ("Hello World","W", True),
    ("123", "1", True),
    ("Skypro", "o" ,True)

])

def test_contains_positive(input_str, symbol, expected_result):
    assert string_utils.contains(input_str, symbol) == expected_result


@pytest.mark.negative
@pytest.mark.parametrize("input_str, symbol, expected_result", [
    ("123", "a", False),
    ("Python", "i", False),
    ("", "o" ,False)

])
def test_contains_negative(input_str, symbol, expected_result):
    assert string_utils.contains(input_str, symbol) == expected_result

@pytest.mark.positive
@pytest.mark.parametrize("input_str, symbol, expected_result", [ 
    ("Hello World","World", "Hello "),
    ("123", "1", "23"),
    ("Skypro", "ro" ,"Skyp")
])
def test_delete_symbol_positive(input_str, symbol, expected_result):
    assert string_utils.delete_symbol(input_str, symbol) == expected_result

@pytest.mark.negative
@pytest.mark.parametrize("input_str, symbol, expected_result", [
    ("123", "i", "123" ),
    ("Python", "i", "Python" ),
    ("", "o" ,"")
])
def test_delete_symbol_negative(input_str, symbol, expected_result):
    assert string_utils.delete_symbol(input_str, symbol) == expected_result