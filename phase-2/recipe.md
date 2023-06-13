# {{PROBLEM}} Function Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

As a user
So that I can manage my time
I want to see an estimate of reading time for a text, assuming that I can read 200 words a minute.

## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

```python
# EXAMPLE

def estimated_reading_time(text):
    """Gives an estimated reading time of a text based on 200 words per minute

    Parameters: 
        text: a string containing words (e.g. "hello WORLD")

    Returns: (state the return value and its type)
        a string containing words and the minutes as a flot to 2 decimal places it will take

    Side effects: (state any side effects)
        This function doesn't print anything or have any other side-effects
    """
    pass # Test-driving means _not_ writing any code here yet.
```

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python
# EXAMPLE

"""
Given a text of 200 words
"""
estimated_reading_time("text of 200 words.....") => "This wil take you 1.00 minutes to read"

"""
Given a text of 100 words
"""
estimated_reading_time("text of 100 words") => "This wil take you 0.50 minutes to read"

"""
Given an empty text
"""
estimated_reading_time("") => "Pick up a book!"

"""
Given a None value
It throws an error
"""
estimated_reading_time(None) throws an error
```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python
# EXAMPLE

from lib.estimated_reading_time import *

"""
Given a lower and an uppercase word
It returns a list with the uppercase word
"""
def test_extract_uppercase_with_upper_then_lower():
    result = extract_uppercase("hello WORLD")
    assert result == ["WORLD"]

```

Ensure all test function names are unique, otherwise pytest will ignore them!

