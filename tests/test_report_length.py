from lib.report_length import *

def test_correct_length():
    str = "hello"
    result = report_length(str)
    assert result == "This string was 5 characters long."
    
def test_empty_string_length():
    str = ""
    result = report_length(str)
    assert result == "This string was 0 characters long."
