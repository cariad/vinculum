from pytest import mark

from vinculum import Fraction


def test_eq__unhandled_type() -> None:
    assert Fraction(0) != "zero"


@mark.parametrize(
    "n, d, expect_n, expect_d",
    [
        (0, 0, 0, 0),
        (1, 2, 1, 2),
        (-1, 2, -1, 2),
        (1, -2, -1, 2),
        (-1, -2, 1, 2),
    ],
)
def test_init(n: int, d: int, expect_n: int, expect_d: int) -> None:
    f = Fraction(n, d)
    assert f.denominator == expect_d
    assert f.numerator == expect_n


@mark.parametrize(
    "f, expect",
    [
        (Fraction(0), Fraction(0)),
        (Fraction(1), Fraction(1)),
        (Fraction(1, 2), Fraction(1, 2)),
        (Fraction(15, 30), Fraction(1, 2)),
    ],
)
def test_reduced(f: Fraction, expect: Fraction) -> None:
    assert f.reduced == expect
