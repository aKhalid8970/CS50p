from numb3rs import validate

def test_true():
    assert validate("223.45.6.9") == True
    assert validate("45.0.42.222") == True
    assert validate("127.0.0.1") == True

def test_falsenumbers():
    assert validate("234.765.4.65") == False
    assert validate("100.256.23.45") == False
    assert validate("256.255.255.255") == False

def test_falseother():
    assert validate("cat") == False
    assert validate("thirty.45.345.9") == False

