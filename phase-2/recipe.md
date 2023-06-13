# {{PROBLEM}} Function Design Recipe

## 1. Describe the Problem

As a user
So that I can improve my grammar
I want to verify that a text starts with a capital letter and ends with a suitable sentence-ending punctuation mark

## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

```python
# EXAMPLE

def verify_text(text):
    """Check that a text starts with a capitalised letter and ends with a sentence ending punctuation mark

    Parameters: 
        text: a string containing words (e.g. "hello WORLD")

    Returns: (state the return value and its type)
        a string containing words verifying the conditions

    Side effects: (state any side effects)
        printing out the correct string
    """
    pass # Test-driving means _not_ writing any code here yet.
```

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python
# EXAMPLE

"""
Given a text with no capitalised first letter
"""
verify_text("text.") => "No capitalised first letter"

"""
Given a text with no suitable ending punctuation marks
"""
verify_text("Text") => "No suitable ending punctuation mark"

"""
Given an empty text
"""
verify_text("") => throw an error

"""
Given a text with a capitalised first letter and suitable ending punctuation mark
"""
```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python
# EXAMPLE

from lib.verify_text import *

"""
Given a lower and an uppercase word
It returns a list with the uppercase word
"""
def test_extract_uppercase_with_upper_then_lower():
    result = extract_uppercase("hello WORLD")
    assert result == ["WORLD"]

```

Ensure all test function names are unique, otherwise pytest will ignore them!

