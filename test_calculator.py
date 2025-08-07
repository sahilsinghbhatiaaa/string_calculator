'''
TDD:
Failing test first
Writing that make test pass
Refactor to improve it
'''
import pytest

from calculator import add

def test_empty_string_returns_zero():
    assert add("") == 0

def test_single_num_string_returns_num():
    assert add("1") == 1

def test_string_with_whitespace_delimiter():
    assert add("1 2") == 3

def test_string_with_comma_delimiter():
    assert add("1,2,3") == 6

def test_newline_between_numbers():
    assert add("1\n2,3") == 6

def test_custom_delimiter():
    assert add("//;\n1;2") == 3

def test_negative_number_raises():
    with pytest.raises(ValueError, match="negative numbers not allowed -1"):
        add("-1")