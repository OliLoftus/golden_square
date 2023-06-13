import pytest
from lib.estimated_reading_time import *

def test_empty_string_input():
    result = estimated_reading_time("")
    assert result == "Pick up a book!"

def test_with_200_words():
    text = " ".join(["word" for i in range(0, 200)] )
    result = estimated_reading_time(text)
    assert result == f"This will take you 1.0 minutes to read."

def test_with_400_words():
    text = " ".join(["word" for i in range(0, 400)] )
    result = estimated_reading_time(text)
    assert result == f"This will take you 2.0 minutes to read."

def test_error_with_none_input():
    with pytest.raises(Exception) as e:
        estimated_reading_time(None)
    error_message = str(e.value)
    assert error_message == "Unable to estimate a None value"