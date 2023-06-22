from lib.diary import *

def test_diary_empty_initially():
    diary = Diary()
    assert diary.all() == []