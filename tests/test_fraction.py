from typing import Any

from pytest import mark, raises

from vinculum import Fraction


@mark.parametrize(
    "a, b, expect",
    [
        (
            Fraction(2, 3),
            1,
            Fraction(5, 3),
        ),
        (
            Fraction(2, 3),
            1.5,
            Fraction(13, 6),
        ),
        (
            Fraction(2, 3),
            Fraction(4, 6),
            Fraction(4, 3),
        ),
    ],
)
def test_add(a: Fraction, b: Any, expect: Fraction) -> None:
    assert a + b == expect


def test_add__unhandled_type() -> None:
    with raises(TypeError) as ex:
        _ = Fraction(0) + "zero"

    assert str(ex.value) == "Cannot add 'zero' (str) to 0/1 (Fraction)"


@mark.parametrize(
    "a, b, expect",
    [
        (
            Fraction(0),
            Fraction(0),
            (Fraction(0), Fraction(0)),
        ),
        (
            Fraction(3, 2),
            Fraction(15, 30),
            (Fraction(90, 60), Fraction(30, 60)),
        ),
    ],
)
def test_comparable(a: Fraction, b: Fraction, expect: Fraction) -> None:
    assert Fraction.comparable(a, b) == expect


def test_eq__unhandled_type() -> None:
    assert Fraction(0) != "zero"


@mark.parametrize(
    "f, expect",
    [
        (1.0, Fraction(1)),
        (1.5, Fraction(3, 2)),
        (1.25, Fraction(5, 4)),
        (-1.25, Fraction(-5, 4)),
    ],
)
def test_from_float(f: float, expect: Fraction) -> None:
    assert Fraction.from_float(f) == expect


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
