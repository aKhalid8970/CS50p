from twttr import shorten

def test_string():
    assert shorten("Hello, world") == "Hll, wrld"
    assert shorten("What's up") == "Wht's p"
    assert shorten("Ello world") == "ll wrld"

def test_int():
    assert shorten("CS50") == "CS50"
    assert shorten("216abc!") == "216bc!"
