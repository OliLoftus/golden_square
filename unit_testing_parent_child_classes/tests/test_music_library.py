from unittest.mock import Mock
from lib.music_library import MusicLibrary

"""
When i add multiple tracks and search for a keyword
I get tracks that match that keyword
"""

def test_searches_by_keyword():
    library = MusicLibrary()
    fake_match = Mock()
    fake_match.matches.return_value = True
    library.add(fake_match)
    fake_not_match = Mock()
    fake_not_match.matches.return_value = False
    library.add(fake_not_match)
    assert library.search("eskimo") == [fake_match]

"""
Initially tracks is empty
"""
def test_tracks_initially_empty():
    library = MusicLibrary()
    assert library.tracks == []

"""
Added tracks show in list
"""
def test_added_tracks_show_in_list():
    library = MusicLibrary
    track_1 = Mock()
    track_2 = Mock()
    library.add(track_1)
    library.add(track_2)
    assert library.tracks == [track_1, track_2]