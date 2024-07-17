from plates import is_valid

def test_start():
    assert is_valid("23CSSS") == False
    assert is_valid("43") == False

def test_range():
    assert is_valid("C") == False
    assert is_valid("CSAA2222") == False

def test_number():
    assert is_valid("AAA22A") == False
    assert is_valid("AAA002") == False
def test_punc():
    assert is_valid("CS50.") == False
    assert is_valid("AAA22!") == False

