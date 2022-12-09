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
