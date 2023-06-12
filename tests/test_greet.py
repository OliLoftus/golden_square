from lib.greet import *

def test_greet():
    result = greet("Oli")
    assert result == "Hello, Oli!"