import math

import pytest
from calculator_lib import Calculator


@pytest.fixture
def calc():
    return Calculator()


class TestAdd:
    def test_positive_numbers(self, calc):
        assert calc.add(2, 3) == 5

    def test_negative_numbers(self, calc):
        assert calc.add(-1, -2) == -3

    def test_mixed_signs(self, calc):
        assert calc.add(-1, 3) == 2

    def test_floats(self, calc):
        assert calc.add(1.5, 2.5) == 4.0


class TestSubtract:
    def test_positive_numbers(self, calc):
        assert calc.subtract(5, 3) == 2

    def test_negative_result(self, calc):
        assert calc.subtract(3, 5) == -2

    def test_floats(self, calc):
        assert calc.subtract(5.5, 2.5) == 3.0


class TestMultiply:
    def test_positive_numbers(self, calc):
        assert calc.multiply(3, 4) == 12

    def test_by_zero(self, calc):
        assert calc.multiply(5, 0) == 0

    def test_negative_numbers(self, calc):
        assert calc.multiply(-2, -3) == 6

    def test_floats(self, calc):
        assert calc.multiply(2.5, 4) == 10.0


class TestDivide:
    def test_even_division(self, calc):
        assert calc.divide(10, 2) == 5

    def test_float_result(self, calc):
        assert calc.divide(7, 2) == 3.5

    def test_divide_by_zero(self, calc):
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            calc.divide(10, 0)

    def test_negative_numbers(self, calc):
        assert calc.divide(-6, 3) == -2


class TestPower:
    def test_positive_exponent(self, calc):
        assert calc.power(2, 3) == 8

    def test_zero_exponent(self, calc):
        assert calc.power(5, 0) == 1

    def test_negative_exponent(self, calc):
        assert calc.power(2, -1) == 0.5

    def test_fractional_exponent(self, calc):
        assert calc.power(9, 0.5) == 3.0


class TestModulo:
    def test_positive_numbers(self, calc):
        assert calc.modulo(10, 3) == 1

    def test_negative_dividend(self, calc):
        assert calc.modulo(-10, 3) == 2

    def test_modulo_by_zero(self, calc):
        with pytest.raises(ValueError, match="Cannot modulo by zero"):
            calc.modulo(10, 0)

    def test_floats(self, calc):
        assert calc.modulo(5.5, 2) == 1.5


class TestSqrt:
    def test_perfect_square(self, calc):
        assert calc.sqrt(16) == 4.0

    def test_non_perfect_square(self, calc):
        assert calc.sqrt(2) == pytest.approx(1.4142135623730951)

    def test_zero(self, calc):
        assert calc.sqrt(0) == 0.0

    def test_negative_number(self, calc):
        with pytest.raises(
            ValueError, match="Cannot take square root of a negative number"
        ):
            calc.sqrt(-1)


class TestLog10:
    def test_ten(self, calc):
        assert calc.log10(10) == 1.0

    def test_hundred(self, calc):
        assert calc.log10(100) == 2.0

    def test_one(self, calc):
        assert calc.log10(1) == 0.0

    def test_zero(self, calc):
        with pytest.raises(
            ValueError, match="Cannot take logarithm of a non-positive number"
        ):
            calc.log10(0)

    def test_negative(self, calc):
        with pytest.raises(
            ValueError, match="Cannot take logarithm of a non-positive number"
        ):
            calc.log10(-5)


class TestLn:
    def test_e(self, calc):
        assert calc.ln(math.e) == pytest.approx(1.0)

    def test_one(self, calc):
        assert calc.ln(1) == 0.0

    def test_zero(self, calc):
        with pytest.raises(
            ValueError, match="Cannot take logarithm of a non-positive number"
        ):
            calc.ln(0)

    def test_negative(self, calc):
        with pytest.raises(
            ValueError, match="Cannot take logarithm of a non-positive number"
        ):
            calc.ln(-1)


class TestExp:
    def test_zero(self, calc):
        assert calc.exp(0) == 1.0

    def test_one(self, calc):
        assert calc.exp(1) == pytest.approx(math.e)

    def test_negative(self, calc):
        assert calc.exp(-1) == pytest.approx(1 / 2.718281828459045)


class TestNthRoot:
    def test_cube_root(self, calc):
        assert calc.nth_root(27, 3) == pytest.approx(3.0)

    def test_fourth_root(self, calc):
        assert calc.nth_root(16, 4) == pytest.approx(2.0)

    def test_negative_odd_root(self, calc):
        assert calc.nth_root(-27, 3) == pytest.approx(-3.0)

    def test_even_root_of_negative(self, calc):
        with pytest.raises(
            ValueError, match="Cannot take even root of a negative number"
        ):
            calc.nth_root(-4, 2)

    def test_zeroth_root(self, calc):
        with pytest.raises(ValueError, match="Cannot take zeroth root"):
            calc.nth_root(8, 0)


class TestFloorDivide:
    def test_even_division(self, calc):
        assert calc.floor_divide(10, 2) == 5

    def test_truncates_toward_negative_infinity(self, calc):
        assert calc.floor_divide(7, 2) == 3

    def test_negative_numbers(self, calc):
        assert calc.floor_divide(-7, 2) == -4

    def test_floor_divide_by_zero(self, calc):
        with pytest.raises(ValueError, match="Cannot floor divide by zero"):
            calc.floor_divide(10, 0)


class TestAbsolute:
    def test_positive(self, calc):
        assert calc.absolute(5) == 5

    def test_negative(self, calc):
        assert calc.absolute(-5) == 5

    def test_zero(self, calc):
        assert calc.absolute(0) == 0

    def test_float(self, calc):
        assert calc.absolute(-3.14) == 3.14


class TestRoundNumber:
    def test_round_down(self, calc):
        assert calc.round_number(3.3) == 3

    def test_round_up(self, calc):
        assert calc.round_number(3.7) == 4

    def test_round_to_decimals(self, calc):
        assert calc.round_number(3.14159, 2) == 3.14

    def test_negative(self, calc):
        assert calc.round_number(-2.7) == -3


class TestFloor:
    def test_positive_float(self, calc):
        assert calc.floor(3.7) == 3.0

    def test_negative_float(self, calc):
        assert calc.floor(-3.2) == -4.0

    def test_integer(self, calc):
        assert calc.floor(5.0) == 5.0


class TestCeil:
    def test_positive_float(self, calc):
        assert calc.ceil(3.2) == 4.0

    def test_negative_float(self, calc):
        assert calc.ceil(-3.7) == -3.0

    def test_integer(self, calc):
        assert calc.ceil(5.0) == 5.0
