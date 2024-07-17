from jar import Jar
import pytest

def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"

def test_init():
    jar = Jar(5)
    assert jar.capacity == 5
    assert jar.size == 0
    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0
    jar = Jar(100)
    assert jar.capacity == 100
    assert jar.size == 0

def test_deposit():
    jar = Jar()
    jar.deposit(5)
    assert jar.size == 5
    jar.deposit(5)
    assert jar.size == 10
    with pytest.raises(ValueError):
        jar.deposit(5)

def test_withdraw():
    jar = Jar(100)
    jar.deposit(100)
    jar.withdraw(50)
    assert jar.size == 50
    jar.withdraw(25)
    assert jar.size == 25
    with pytest.raises(ValueError):
        jar.withdraw(50)
