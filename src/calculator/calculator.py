"""Core calculator engine.

Provides the :class:`Calculator` class with stateless arithmetic,
power/root, modulo, rounding, and logarithmic/exponential operations.
All methods accept and return ``float`` values.
"""

import logging
import math

logger = logging.getLogger(__name__)


class Calculator:
    """Stateless calculator that exposes arithmetic operations as methods.

    Every method takes ``float`` arguments, returns a ``float`` result,
    and raises :exc:`ValueError` for invalid inputs (e.g. division by
    zero, square root of a negative number).
    """

    # Core Arithmetic

    def add(self, a: float, b: float) -> float:
        """Return the sum of *a* and *b*."""
        result = a + b
        logger.debug("add(%s, %s) = %s", a, b, result)
        return result

    def subtract(self, a: float, b: float) -> float:
        """Return *a* minus *b*."""
        result = a - b
        logger.debug("subtract(%s, %s) = %s", a, b, result)
        return result

    def multiply(self, a: float, b: float) -> float:
        """Return the product of *a* and *b*."""
        result = a * b
        logger.debug("multiply(%s, %s) = %s", a, b, result)
        return result

    def divide(self, a: float, b: float) -> float:
        """Return *a* divided by *b*.

        Raises:
            ValueError: If *b* is zero.
        """
        if b == 0:
            logger.warning("Division by zero attempted: divide(%s, %s)", a, b)
            raise ValueError("Cannot divide by zero")
        result = a / b
        logger.debug("divide(%s, %s) = %s", a, b, result)
        return result

    # Power & Roots

    def power(self, a: float, b: float) -> float:
        """Return *a* raised to the power *b*."""
        result = a**b
        logger.debug("power(%s, %s) = %s", a, b, result)
        return result

    def sqrt(self, a: float) -> float:
        """Return the square root of *a*.

        Raises:
            ValueError: If *a* is negative.
        """
        if a < 0:
            logger.warning("Square root of negative number attempted: sqrt(%s)", a)
            raise ValueError("Cannot take square root of a negative number")
        result = a**0.5
        logger.debug("sqrt(%s) = %s", a, result)
        return result

    def nth_root(self, a: float, n: float) -> float:
        """Return the *n*-th root of *a*.

        Raises:
            ValueError: If *n* is zero, or if *a* is negative and *n*
                is even.
        """
        if n == 0:
            logger.warning("Zeroth root attempted: nth_root(%s, %s)", a, n)
            raise ValueError("Cannot take zeroth root")
        if a < 0 and n % 2 == 0:
            logger.warning(
                "Even root of negative number attempted: nth_root(%s, %s)", a, n
            )
            raise ValueError("Cannot take even root of a negative number")
        if a < 0:
            result = -((-a) ** (1 / n))
        else:
            result = a ** (1 / n)
        logger.debug("nth_root(%s, %s) = %s", a, n, result)
        return result

    # Modulo & Integer Math

    def modulo(self, a: float, b: float) -> float:
        """Return the remainder of *a* divided by *b*.

        Raises:
            ValueError: If *b* is zero.
        """
        if b == 0:
            logger.warning("Modulo by zero attempted: modulo(%s, %s)", a, b)
            raise ValueError("Cannot modulo by zero")
        result = a % b
        logger.debug("modulo(%s, %s) = %s", a, b, result)
        return result

    def floor_divide(self, a: float, b: float) -> float:
        """Return the floor division of *a* by *b*.

        Raises:
            ValueError: If *b* is zero.
        """
        if b == 0:
            logger.warning(
                "Floor division by zero attempted: floor_divide(%s, %s)", a, b
            )
            raise ValueError("Cannot floor divide by zero")
        result = a // b
        logger.debug("floor_divide(%s, %s) = %s", a, b, result)
        return result

    # Absolute & Rounding

    def absolute(self, a: float) -> float:
        """Return the absolute value of *a*."""
        result = abs(a)
        logger.debug("absolute(%s) = %s", a, result)
        return result

    def round_number(self, a: float, decimals: int = 0) -> float:
        """Return *a* rounded to *decimals* decimal places."""
        result = round(a, decimals)
        logger.debug("round_number(%s, %s) = %s", a, decimals, result)
        return result

    def floor(self, a: float) -> float:
        """Return the largest integer less than or equal to *a*."""
        result = float(math.floor(a))
        logger.debug("floor(%s) = %s", a, result)
        return result

    def ceil(self, a: float) -> float:
        """Return the smallest integer greater than or equal to *a*."""
        result = float(math.ceil(a))
        logger.debug("ceil(%s) = %s", a, result)
        return result

    # Logarithmic & Exponential

    def log10(self, a: float) -> float:
        """Return the base-10 logarithm of *a*.

        Raises:
            ValueError: If *a* is not positive.
        """
        if a <= 0:
            logger.warning("Log of non-positive number attempted: log10(%s)", a)
            raise ValueError("Cannot take logarithm of a non-positive number")
        result = math.log10(a)
        logger.debug("log10(%s) = %s", a, result)
        return result

    def ln(self, a: float) -> float:
        """Return the natural logarithm of *a*.

        Raises:
            ValueError: If *a* is not positive.
        """
        if a <= 0:
            logger.warning("Log of non-positive number attempted: ln(%s)", a)
            raise ValueError("Cannot take logarithm of a non-positive number")
        result = math.log(a)
        logger.debug("ln(%s) = %s", a, result)
        return result

    def exp(self, a: float) -> float:
        """Return *e* raised to the power *a*."""
        result = math.exp(a)
        logger.debug("exp(%s) = %s", a, result)
        return result
