from __future__ import annotations

from math import modf
from typing import Any

from vinculum.math import greatest_common_divisor


class Fraction:
    """
    A fractional number.

    For example, given the fraction 3/2 (decimal 1.5), the `numerator` is 3 and
    `denominator` is 2.
    """

    def __init__(self, numerator: int, denominator: int = 1) -> None:
        self._numerator = numerator
        self._denominator = denominator

        if self._denominator < 0:
            self._denominator = abs(self._denominator)
            self._numerator = self._numerator * -1

    def __add__(self, other: Any) -> Fraction:
        a, b = self.comparable_with_self(other)
        f = Fraction(a.numerator + b.numerator, a.denominator)
        return f.reduced

    def __eq__(self, other: Any) -> bool:
        a, b = self.comparable_with_self(other)
        return a.numerator == b.numerator

    def __ge__(self, other: Any) -> bool:
        a, b = self.comparable_with_self(other)
        return a.numerator >= b.numerator

    def __gt__(self, other: Any) -> bool:
        a, b = self.comparable_with_self(other)
        return a.numerator > b.numerator

    def __le__(self, other: Any) -> bool:
        a, b = self.comparable_with_self(other)
        return a.numerator <= b.numerator

    def __lt__(self, other: Any) -> bool:
        a, b = self.comparable_with_self(other)
        return a.numerator < b.numerator

    def __mul__(self, other: Any) -> Fraction:
        other = Fraction.from_any(other)
        result = Fraction(
            self.numerator * other.numerator,
            self.denominator * other.denominator,
        )
        return result.reduced

    def __repr__(self) -> str:
        return f"{self._numerator}/{self._denominator}"

    @staticmethod
    def comparable(a: Fraction, b: Fraction) -> tuple[Fraction, Fraction]:
        """
        Converts fractions `a` and `b` to the same denominator.
        """

        if a.denominator == b.denominator:
            return a, b

        return (
            Fraction(
                a.numerator * b.denominator,
                a.denominator * b.denominator,
            ),
            Fraction(
                b.numerator * a.denominator,
                b.denominator * a.denominator,
            ),
        )

    def comparable_with_self(self, value: Any) -> tuple[Fraction, Fraction]:
        """
        Converts this and `value` to Fractions of the same denominator.
        """

        value = Fraction.from_any(value)
        return Fraction.comparable(self, value)

    @property
    def denominator(self) -> int:
        """
        Denominator.

        For example, given the fraction 3/2, the denominator is "2".
        """

        return self._denominator

    @classmethod
    def from_any(cls, value: Any) -> Fraction:
        """
        Converts `value` to a Fraction.

        Raises `TypeError` if `value` cannot be converted to a Fraction.
        """

        if isinstance(value, int):
            return Fraction(value)

        if isinstance(value, float):
            return Fraction.from_float(value)

        if isinstance(value, Fraction):
            return value

        raise TypeError(
            f"Cannot create a Fraction from {repr(value)} "
            f"({value.__class__.__name__})"
        )

    @classmethod
    def from_float(cls, f: float) -> Fraction:
        f, i = modf(f)
        result = Fraction(int(i))
        over = 10

        while f != 0:
            f, i = modf(f * 10)
            result += Fraction(int(i), over)
            over *= 10

        return result

    @property
    def numerator(self) -> int:
        """
        Numerator.

        For example, given the fraction 3/2, the numerator is "3".
        """

        return self._numerator

    @property
    def reduced(self) -> Fraction:
        """
        Gets the fraction in its reduced form.

        For example, 15/30 reduces to 1/2.
        """

        gcf = greatest_common_divisor(self._numerator, self._denominator)

        if gcf in (0, 1):
            return self

        return Fraction(
            self._numerator // gcf,
            self._denominator // gcf,
        )
