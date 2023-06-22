from lib.to_do_list import *
from lib.to_do import *

"""
when two tasks added to to_do list
incomplete shows the incomplete tasks
"""

def test_two_added_show_incomplete() :
    to_do_list = TodoList()
    task_1 = Todo("Task one")
    task_2 = Todo("Task two")
    to_do_list.add(task_1)
    to_do_list.add(task_2)
    assert to_do_list.incomplete() == [task_1, task_2]

"""
when two tasks added to to_do list
return completed list
"""
def test_two_added_show_complete() :
    to_do_list = TodoList()
    task_1 = Todo("Task one")
    task_2 = Todo("Task two")
    task_1.mark_complete()
    task_2.mark_complete()
    to_do_list.add(task_1)
    to_do_list.add(task_2)
    assert to_do_list.complete() == [task_1, task_2]

