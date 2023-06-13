# {{PROBLEM}} Function Design Recipe

## 1. Describe the Problem

As a user
So that I can keep track of my tasks
I want to check if a text includes the string #TODO.



## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

```python
# EXAMPLE

def check_if_includes_TODO(text):
    """Checks a string to see if it includes #TODO

    Parameters: 
        text: a string containing words (e.g. "hello WORLD")

    Returns: (state the return value and its type)
        a string containing words verifying the conditions

    Side effects: (state any side effects)
        
    """
    pass # Test-driving means _not_ writing any code here yet.
```

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python
# EXAMPLE
"""
Given an empty text
"""
check_if_includes_TODO("") => throw an error

"""
Given a text that contains #TODO
"""
check_if_includes_TODO("#TODO walk dog") => "This contains TODO"

"""
Given a text that doesn't contain #TODO
"""
check_if_includes_TODO("walk the dog") => "This doesn't contain #TODO"


```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python
# EXAMPLE

from lib.check_if_includes_TODO import *

"""
Given a lower and an uppercase word
It returns a list with the uppercase word
"""
def test_extract_uppercase_with_upper_then_lower():
    result = extract_uppercase("hello WORLD")
    assert result == ["WORLD"]

```

Ensure all test function names are unique, otherwise pytest will ignore them!

