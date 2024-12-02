import pytest
from calculations import multiply, divide, distance, quadratic, geometric_sum

class TestMathFunctions:

    @pytest.mark.parametrize("a, b, expected", [
        (2, 3, 6),
        (0, 5, 0),
        (-2, -3, 6),
    ])
    def test_multiply(self, a, b, expected):
        assert multiply(a, b) == expected

    @pytest.mark.parametrize("a, b, expected", [
        (6, 3, 2),
        (5, 2, 2.5),
        (-6, -3, 2),
        (-6, 3, -2),
        (0, 1, 0),
    ])
    def test_divide(self, a, b, expected):
        if b == 0:
            with pytest.raises(ValueError):
                divide(a, b)
        else:
            assert divide(a, b) == expected
