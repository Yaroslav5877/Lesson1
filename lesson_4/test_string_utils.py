import pytest
from string_utils import StringUtils

utils = StringUtils()

""""capitilize"""

def test_capitalize():
    ''''POSITIVE'''
    assert utils.capitalize("skypro") == "Skypro"
    assert utils.capitalize("hi people") == "Hi People"
    assert utils.capitalize("555") == "555"
    """"NEGATIVE"""
    assert utils.capitalize("") == ""
    assert utils.capitalize(" ") == " "
    assert utils.capitalize("yarik77") == "yarik77"


""""trim"""
def test_trim():
    ''''POSITIVE'''
    assert utils.trim("     skypro") == "skypro"
    assert utils.trim("   hi people") == "hi people"
    assert utils.trim("  TOT  ") == "TOT  "
    """"NEGATIVE"""
    assert utils.trim("") == ""



""""to_list"""
@pytest.mark.parametrize('string, delimeter, result', [
    #POSITIVE
    ("яблоко, банан, апельсин", ",", ["яблоко", "банан", "апельсин"]),
    ("1, 2, 3, 4, 5", ",", ["1", "2", "3", "4", "5"]),
    #NEGATIVE
    ("", None, []),
    ("1, 2, 3, 4  5", "None", ["1", "2", "3", "4  5"]),
])
def test_to_list(string, delimeter, result):
    if delimeter is None:
        res = utils.to_list(string)
    else:
        res = utils.to_list(string, delimeter)
    assert res == result



""""contains"""
@pytest.mark.parametrize('string, stmbol, result', [
    ("банан", "б", True),
    ("дом", "о", True),
    ("ком", "м", True),
    ("динь-донь", "-", True),
    ("123546", "5", True),
    ("Город", "г", False),
    ("Город", "п", False),
    ("снег", "*", False),
    ("123456", "Ж", False),
])
def test_contains(string, symbol, result):
    res = utils.contains(string, symbol)
    assert res == result
    
    
""""delete_symbol"""
@pytest.mark.parametrize('string, symbol, result', [
    ("дверь", "д", "верь"),
    ("Ярик", "и", "Ярк"),
    ("Ярик", "Я", "рик"),
    ("12345", "3", "1245"), 
    
    ("дом", "к", "дом"),
    ("", "", ""),
    ("", "", "33"),
    ("live", "", "live")
])
def test_delete_symbol(string, symbol, result):
    res = utils.delete_symbol(string, symbol, result)
    assert res == result
    
    
    
""""starts_with"""
@pytest.mark.parametrize('string, symbol, result', [
    ("дверь", "д", True),
    ("Ярик", "Я", True),
    ("live", "l", True),
    ("Проспект-Мира", "П", True),
    ("123456", "1", True),
    
    ("дверь", "Д", False),
    ("Ярик", "я", False),
    ("Ярик", "y", False),
    ("12345", "0", False)  
])
def test_starts_with(string, symbol, result):
    res = utils.starts_with(string, symbol)
    assert res == result




""""end_with"""
@pytest.mark.parametrize('string, symbol, result', [
    ("Yarik", "k", True),
    ("live", "e", True),
    ("95", "5", True),
    ("Агент007", "7", True),
    
    ("дверь", "Ь", False),
    ("Ярик", "и", False),
    ("Ярик", "Y", False),
    ("12345", "4", False), 
])
def test_end_with(string, symbol, result):
    res = utils.end_with(string, symbol)
    assert res == result
    
    

"""is_empty"""
@pytest.mark.parametrize('string, result' [
    ("", True),
    (" ", True),
    ("   ", True),
    
    ("что-то есть", False),
    (" кто-то есть ", False),
    ("1231241234", False),
])
def test_is_empty(string, result):
    res = utils.is_empty(string)
    assert res == result
    
    
"""list_to_string"""
@pytest.mark.parametrize('lst, joiner, result', [
    (["s", "o", "s"], ",", "s,o,s"),
    ([1, 2, 3, 4, 5, 6, 7], None, "1, 2, 3, 4, 5, 6, 7"),
    (["Один", "Два"], "-", "Один-Два"),
    
    ([], None, ""),
    ([], 'Кино', "")
    
])
def test_list_to_string(lst, joiner, result):
    if joiner == None:
        res = utils.list_to_string(lst)
    else:
        res = utils.list_to_string(lst, joiner)
    assert res == result
    
    