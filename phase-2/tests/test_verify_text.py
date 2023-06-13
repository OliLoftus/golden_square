from lib.verify_text import *

def test_no_capital():
    result = verify_text("text.")
    assert result == "No capitalised first letter."

def test_ending():
    result = verify_text("Text")
    assert result == "No suitable ending punctuation mark"