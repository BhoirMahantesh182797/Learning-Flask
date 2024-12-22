import pytest
from square import get_square
def test_square():
    x = 5
    res = get_square(5)
    assert res == 25
    assert get_square(4) == 16
    assert get_square(3) == 9
