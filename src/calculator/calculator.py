class Calculator:

    # Core Arithmetic

    def add(self, a: float, b: float) -> float:
        return a + b

    def subtract(self, a: float, b: float) -> float:
        return a - b

    def multiply(self, a: float, b: float) -> float:
        return a * b

    def divide(self, a: float, b: float) -> float:
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

    # Power & Roots

    def power(self, a: float, b: float) -> float:
        return a**b

    def sqrt(self, a: float) -> float:
        if a < 0:
            raise ValueError("Cannot take square root of a negative number")
        return a**0.5

    def nth_root(self, a: float, n: float) -> float:
        if n == 0:
            raise ValueError("Cannot take zeroth root")
        if a < 0 and n % 2 == 0:
            raise ValueError("Cannot take even root of a negative number")
        if a < 0:
            return -((-a) ** (1 / n))
        return a ** (1 / n)

    # Modulo & Integer Math

    def modulo(self, a: float, b: float) -> float:
        if b == 0:
            raise ValueError("Cannot modulo by zero")
        return a % b

    def floor_divide(self, a: float, b: float) -> float:
        if b == 0:
            raise ValueError("Cannot floor divide by zero")
        return a // b

    # Absolute & Rounding

    def absolute(self, a: float) -> float:
        return abs(a)

    def round_number(self, a: float, decimals: int = 0) -> float:
        return round(a, decimals)

    def floor(self, a: float) -> float:
        import math

        return float(math.floor(a))

    def ceil(self, a: float) -> float:
        import math

        return float(math.ceil(a))

    # Logarithmic & Exponential

    def log10(self, a: float) -> float:
        import math

        if a <= 0:
            raise ValueError("Cannot take logarithm of a non-positive number")
        return math.log10(a)

    def ln(self, a: float) -> float:
        import math

        if a <= 0:
            raise ValueError("Cannot take logarithm of a non-positive number")
        return math.log(a)

    def exp(self, a: float) -> float:
        import math

        return math.exp(a)
