from bank import value

def test_zero():
    assert value("Hello") == 0

def test_twenty():
    assert value("hi") == 20
    assert value("hey") == 20
    assert value("happy") == 20

def test_hundred():
    assert value("CS50") == 100
    assert value("100") == 100
    assert value("whats up") == 100
