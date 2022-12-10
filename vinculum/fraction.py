from __future__ import annotations

from io import StringIO
from locale import localeconv
from math import modf
from re import compile  # pylint: disable=redefined-builtin
from typing import Any, List, Optional, cast

from vinculum.log import log
from vinculum.math import greatest_common_divisor, int_to_buffer, string_to_int

DECIMAL_POINT = str(localeconv()["decimal_point"])

DECIMAL_PATTERN = compile(rf"^(-?\d+)(?:\{DECIMAL_POINT}(\d+))?$")
FRACTION_PATTERN = compile(r"^(\d+)/(\d+)$")


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

    def __float__(self) -> float:
        return self._numerator / self._denominator

    def __floordiv__(self, other: Any) -> Fraction:
        a, b = self.comparable_with_self(other)
        true_result = a * b.reciprocal
        return Fraction(true_result.integral)

    def __ge__(self, other: Any) -> bool:
        a, b = self.comparable_with_self(other)
        return a.numerator >= b.numerator

    def __gt__(self, other: Any) -> bool:
        a, b = self.comparable_with_self(other)
        return a.numerator > b.numerator

    def __int__(self) -> int:
        return self.integral

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

    def __radd__(self, other: Any) -> Fraction:
        a, b = self.comparable_with_self(other)
        f = Fraction(b.numerator + a.numerator, a.denominator)
        return f.reduced

    def __repr__(self) -> str:
        return f"{self._numerator}/{self._denominator}"

    def __rfloordiv__(self, other: Any) -> Fraction:
        a, b = self.comparable_with_self(other)
        true_result = b * a.reciprocal
        return Fraction(true_result.integral)

    def __rmul__(self, other: Any) -> Fraction:
        other = Fraction.from_any(other)
        result = Fraction(
            other.numerator * self.numerator,
            other.denominator * self.denominator,
        )
        return result.reduced

    def __rsub__(self, other: Any) -> Fraction:
        a, b = self.comparable_with_self(other)
        f = Fraction(b.numerator - a.numerator, a.denominator)
        return f.reduced

    def __rtruediv__(self, other: Any) -> Fraction:
        a, b = self.comparable_with_self(other)
        return b * a.reciprocal

    def __sub__(self, other: Any) -> Fraction:
        a, b = self.comparable_with_self(other)
        f = Fraction(a.numerator - b.numerator, a.denominator)
        return f.reduced

    def __truediv__(self, other: Any) -> Fraction:
        a, b = self.comparable_with_self(other)
        return a * b.reciprocal

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

    def decimal(
        self,
        max_dp: int = 100,
        recursion: bool = True,
        recurring_prefix: Optional[str] = "\u0307",
    ) -> str:
        """
        Gets the fraction as a decimal string appropriate to the local culture.
        For example, 3/2 in the United Kingdom is rendered as "1.5".

        Recurring digits are represented by overhead dots. For example, 1/3
        returns 0.̇3.

        This function is aware of and avoids CVE-2020-10735:
        https://github.com/python/cpython/issues/95778

        `max_dp` describes the maximum number of decimal places to render. This
        is limited only by your available memory and patience.

        `recursion` describes whether or not to track recursion. There is a
        slight performance benefit to disabling this if you don't care.

        `recurring_prefix` describes the string with which to prefix each
        recurring digit. This is \u0307 (the Unicode "Dot Above" character) by
        default, but you might prefer \u0305 ("Combining Overline").
        """

        log.debug("Rendering %s to a decimal string", self)

        result = StringIO()

        positive = self._numerator >= 0

        integral = abs(self._numerator) // self._denominator
        if not positive:
            integral *= -1

        result = StringIO()

        int_to_buffer(integral, result)

        result.write(DECIMAL_POINT)

        recursion_track: Optional[List[int]] = [] if recursion else None
        remainder = (abs(self._numerator) % self._denominator) * 10

        added_non_zero = False
        decimal_places = 0
        fractional = 0
        leading_zeros = 0
        recurring_count = 0

        while True:
            i = remainder // self._denominator
            remainder = (remainder % self._denominator) * 10

            if recursion_track is not None and (remainder in recursion_track):
                index_of = recursion_track.index(remainder)
                recurring_count = len(recursion_track) - index_of
                break

            fractional *= 10
            fractional += i

            if i > 0:
                added_non_zero = True
            elif not added_non_zero:
                leading_zeros += 1

            decimal_places += 1

            if remainder == 0 or decimal_places >= max_dp:
                break

            if recursion_track is not None:
                recursion_track.append(remainder)

        int_to_buffer(
            fractional,
            result,
            leading_zeros=leading_zeros,
            recurring_count=recurring_count,
            recurring_prefix=recurring_prefix,
        )

        return result.getvalue()

    @property
    def denominator(self) -> int:
        """
        Denominator.

        For example, given the fraction 3/2, the denominator is "2".
        """

        return self._denominator

    @property
    def fractional(self) -> Fraction:
        """
        The fractional part of this number.

        For example, for 3/2, the integral part is 1 (2/2) and the fractional
        part is 1/2.
        """

        return self - self.integral

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

        if isinstance(value, str):
            return Fraction.from_string(value)

        if isinstance(value, Fraction):
            return value

        raise TypeError(
            f"Cannot create a Fraction from {repr(value)} "
            f"({value.__class__.__name__})"
        )

    @classmethod
    def from_float(cls, f: float) -> Fraction:
        log.debug("Parsing float %s", f)

        positive = f >= 0
        f = abs(f)

        fractional, i = modf(f)

        result = Fraction(int(i))
        over = 10

        while fractional != 0:
            f *= 10
            fractional, i = modf(f)
            digit = int(i) % 10
            result += Fraction(digit, over)
            over *= 10

        if not positive:
            result *= -1

        return result

    @classmethod
    def from_string(cls, string: str) -> Fraction:
        """
        Parses `string` as either a decimal or fraction.
        """

        match = DECIMAL_PATTERN.match(string)
        if match is not None:
            log.debug('Parsing "%s" as a decimal', string)

            groups = match.groups(0)

            i = string_to_int(cast(str, groups[0]))
            integral = Fraction(i)

            decimal_group = groups[1]

            log.debug(
                'The decimal group of "%s" is %s (%s)',
                string,
                decimal_group,
                decimal_group.__class__.__name__,
            )

            if decimal_group == 0:
                decimal = Fraction(0)
            else:
                d = cast(str, decimal_group)
                decimal = Fraction(string_to_int(d), 10 ** len(d))

            return (integral + decimal).reduced

        match = FRACTION_PATTERN.match(string)
        if match is not None:
            log.debug('Parsing "%s" as a fraction', string)

            groups = match.groups(0)
            numerator_group = groups[0]

            log.debug(
                'The numerator group of "%s" is %s (%s)',
                string,
                numerator_group,
                numerator_group.__class__.__name__,
            )

            denominator_group = groups[1]

            log.debug(
                'The denominator group of "%s" is %s (%s)',
                string,
                denominator_group,
                denominator_group.__class__.__name__,
            )

            return Fraction(
                string_to_int(cast(str, numerator_group)),
                string_to_int(cast(str, denominator_group)),
            )

        raise ValueError(f'Cannot parse "{string}" as decimal or fraction')

    @property
    def integral(self) -> int:
        """
        The integral part of this number.

        For example, for 3/2, the integral part is 1 (2/2) and the fractional
        part is 1/2.
        """

        return self._numerator // self._denominator

    @property
    def numerator(self) -> int:
        """
        Numerator.

        For example, given the fraction 3/2, the numerator is "3".
        """

        return self._numerator

    @property
    def reciprocal(self) -> Fraction:
        """
        Gets the reciprocal of the fraction.

        For example, the reciprocal of 2/3 is 3/2.
        """

        return Fraction(self.denominator, self.numerator)

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
