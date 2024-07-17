from working import convert
import pytest

def test_correctness():
    assert convert("9 am to 5 pm") == "09:00 to 17:00"
    assert convert("11:45 pm to 8:30 am") == "23:45 to 08:30"

def test_not():
    with pytest.raises(ValueError):
        convert("9:60 am to 10:60 pm")
    with pytest.raises(ValueError):
        convert("8 am - 9 pm")

def test_slick():
    with pytest.raises(ValueError):
        convert("12:00 to 17:00")
