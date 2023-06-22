from lib.track import Track

"""
Given a title and artist and serch keyword for full title
Matches true
"""
def test_matches_on_full_title():
    track = Track("Title 1", "Artist 1")
    assert track.matches("Title 1") == True

"""
Given a title and artist
Search keyword partial title
Matches true
"""
def test_matches_on_partial_title():
    track = Track("Title 1", "Artist 1")
    assert track.matches("Title") == True

"""
Given a title and artist
Search keyword full artist
Matches true
"""
def test_matches_on_full_artist():
    track = Track("Title 1", "Artist 1")
    assert track.matches("Artist 1") == True

"""
Given a title and artist
Search keyword partial artist
Matches true
"""
def test_matches_on_partial_title():
    track = Track("Title 1", "Artist 1")
    assert track.matches("Artist") == True

"""
Given a title and artist
Search keyword doesn't match either
Matches false
"""
def test_does_not_match_on_non_matching_keyword():
    track = Track("Title 1", "Artist 1")
    assert track.matches("eskimo") == False