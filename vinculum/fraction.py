from __future__ import annotations

from typing import Any

from vinculum.log import log
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

    def __eq__(self, other: Any) -> bool:
        if isinstance(other, Fraction):
            a, b = Fraction.comparable(self, other)

            return (
                a.numerator == b.numerator and a.denominator == b.denominator
            )

        log.warning(
            "Cannot check if %s (%s) equals %s (%s)",
            self,
            self.__class__.__name__,
            other,
            other.__class__.__name__,
        )

        return False

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

    @property
    def denominator(self) -> int:
        """
        Denominator.

        For example, given the fraction 3/2, the denominator is "2".
        """

        return self._denominator

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
