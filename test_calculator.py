'''
TDD:
Failing test first
Writing that make test pass
Refactor to improve it
'''
from calculator import add

def test_empty_string_returns_zero():
    assert add("") == 0

def test_single_num_string_returns_num():
    assert add("1") == 1

def test_string_with_whitespace_delimiter():
    assert add("1 2") == 3

def test_string_with_comma_delimiter():
    assert add("1,2,3") == 6