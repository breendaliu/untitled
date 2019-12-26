import pytest


def div(a, b):
    return a / b


@pytest.mark.happy
@pytest.mark.parametrize("number1, number2, exception", {
    (10, 5, 2),
    (10, 2, 5),
    (1000000, 1, 1000000),
    (0.55, 5, 0.11),
    (10, 3, 0.33333),
    (9, -1, -9),
    (-9, -1, 9),
    (5, 0, None),
    (0, 4, None)
})
def test_001(number1, number2, exception):
    assert div(number1, number2) == exception