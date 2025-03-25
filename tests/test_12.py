import pytest

@pytest.mark.parametrize("value1, value2, result", [
    (2.1, 3.05, 6.405),
    (-0.75, 2, -1.5),
    (12, 3, 36),
    (-9, -0.9, 8.1)
])

def test_multiply_two_values(value1, value2, result):
    assert value1 * value2 == result