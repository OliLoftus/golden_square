import pytest 
from lib.to_do_list import *

def test_add_to_do():
    to_do_list = To_do_list()
    to_do_list.add_to_do("Walk the dog")
    assert to_do_list.show_list() == ["Walk the dog"]

def test_add_two_to_do():
    to_do_list = To_do_list()
    to_do_list.add_to_do("Walk the dog")
    assert to_do_list.show_list() == ["Walk the dog"]
    to_do_list.add_to_do("Cook dinner")
    assert to_do_list.show_list() == ["Walk the dog", "Cook dinner"]

def test_empty_string_gives_error():
    with pytest.raises(Exception) as e:
        to_do_list = To_do_list()
        to_do_list.add_to_do("")
    assert str(e.value) == "No task added"

def test_task_removes_from_list():
    to_do_list = To_do_list()
    to_do_list.add_to_do("Walk the dog")
    to_do_list.add_to_do("Cook dinner")
    assert to_do_list.show_list() == ["Walk the dog", "Cook dinner"]
    to_do_list.completed_task("Walk the dog")
    assert to_do_list.show_list() == ["Cook dinner"]

