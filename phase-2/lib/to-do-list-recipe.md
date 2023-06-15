## 1. Describe the Problem

User story 1:

As a user
So that I can keep track of my tasks
I want a program that I can add todo tasks to and see a list of them.

User story 2:

As a user
So that I can focus on tasks to complete
I want to mark tasks as complete and have them disappear from the list.

## 2. Design the Class Interface

_Include the initializer, public properties, and public methods with all parameters, return values, and side-effects._

```python

class To_do_list:
    # User-facing properties:
    #   name: string

    def __init__(self, task_list):
        # Parameters:
        #   task_list: list
        # Side effects:
        #   none
        pass # No code here yet

    def show_list(self)
        # Parameters:
        #   none
        # Returns:
        #   task_list
        # Side effects:
        #   none

    def add_to_do(self, task):
        # Parameters:
        #   task: string representing a single task
        # Returns:
        #   Nothing
        # Side-effects
        #   adds task to the task list
        pass # No code here yet

    def completed_task(self, task):
        # Returns:
        #   nothing
        # Side-effects:
        #   Throws an exception if no task is set
        pass # No code here yet
```

## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._

``` python
# EXAMPLE

"""
Given a task
#adds task to task_list
"""
to_do_list = To_do_list()
to_do_list.add_to_do("Walk the dog")
to_do_list.show_list() # => "Walk the dog"

"""
Given two tasks
#adds tasks to task_list
"""
to_do_list = To_do_list()
to_do_list.add_to_do("Walk the dog")
to_do_list.add_to_do("Cook dinner")
to_do_list.show_list() # => ["Walk the dog", "Cook dinner"]

"""
Given an empty string
#raises an error
"""
to_do_list = To_do_list()
to_do_list.add_to_do("") # raises an error with the message "No task added."

"""
Given a task
#removes from list
"""
to_do_list = To_do_list()
to_do_list.add_to_do("Walk the dog")
to_do_list.add_to_do("Cook dinner")
to_do_list.completed_task("Walk the dog")
to_do_list.show_list() # => "Cook dinner"
```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

