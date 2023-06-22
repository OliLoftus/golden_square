from lib.diary import *
from lib.diary_entry import *

def test_add_and_list_diary():
    diary = Diary()
    entry_1 = "Entry 1", "This is entry one"
    entry_2 = "Entry 2", "This is my second entry in the diary"
    diary.add(entry_1)
    diary.add(entry_2)
    assert diary.all() == [entry_1, entry_2]

def test_count_words_returns_count_for_diary_contents():
    diary = Diary()
    entry_1 = "Entry 1", "This is entry one"
    entry_2 = "Entry 2", "This is my second entry in the diary"
    diary.add(entry_1)
    diary.add(entry_2)
    #assert diary.count_words() == 12