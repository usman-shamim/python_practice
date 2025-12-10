from twttr import shorten

def text_lowercase():
    assert shorten("usman") == "smn"

def test_uppercase():
    assert shorten("HELLO") == "HLL"   

def test_mixed_case():
    assert shorten("Programming") == "Prgrmmng"

def test_non_alphabetic():
    assert shorten("CS50, Python 3!") == "CS50, Pythn 3!"

def test_only_vowels():
    assert shorten("AEIOUaeiou") == ""