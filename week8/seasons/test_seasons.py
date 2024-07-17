from seasons import convert
import pytest

def test_function():
    assert convert("2007-05-10") == "Eight million, nine hundred thirteen thousand, six hundred minutes"
    assert convert("1987-06-21") == "Nineteen million, three hundred seventy-two thousand, three hundred twenty minutes"
    with pytest.raises(SystemExit):
        assert convert("May 6, 1767")
