from lib.diary_entry import *

def test_diary_entry():
    diary_entry = DiaryEntry("Entry 1", "This is entry one")
    assert diary_entry.title == "Entry 1"
    assert diary_entry.contents == "This is entry one"

def test_count_words_returns_words_of_contents():
    diary_entry = DiaryEntry("Entry 1", "This is entry one")
    assert diary_entry.count_words() == 4