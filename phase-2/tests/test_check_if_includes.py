import pytest
from lib.check_if_includes import *

def test_empty_string():
    with pytest.raises(Exception) as e:
        check_if_includes("")
    error_message = str(e.value)
    assert error_message == "No text found, try again!"

def test_text_includes_TODO():
    assert check_if_includes("#TODO walk the dog" ) == "This contains TODO"

def test_does_not_include_TODO():
    assert check_if_includes("walk the dog") == "This doesn't contain #TODO"

    
