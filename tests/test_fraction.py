from typing import Any

from pytest import mark, raises

from vinculum import Fraction


@mark.parametrize(
    "a, b, expect",
    [
        (Fraction(2, 3), 1, Fraction(5, 3)),
        (Fraction(2, 3), 1.5, Fraction(13, 6)),
        (Fraction(2, 3), Fraction(4, 6), Fraction(4, 3)),
        (Fraction(1, 4), Fraction(-1, 2), Fraction(-1, 4)),
    ],
)
def test_add(a: Fraction, b: Any, expect: Fraction) -> None:
    assert a + b == expect


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


@mark.parametrize(
    "f, other, expect",
    [
        (Fraction(3, 2), 1, (Fraction(3, 2), Fraction(2, 2))),
        (Fraction(3, 2), 1.5, (Fraction(3, 2), Fraction(3, 2))),
        (
            Fraction(3, 2),
            Fraction(15, 30),
            (Fraction(90, 60), Fraction(30, 60)),
        ),
    ],
)
def test_comparable_with_self(
    f: Fraction,
    other: Any,
    expect: tuple[Fraction, Fraction],
) -> None:
    assert f.comparable_with_self(other) == expect


@mark.parametrize(
    "f, expect",
    [
        (Fraction(0), "0.0"),
        (Fraction(1), "1.0"),
        (Fraction(2), "2.0"),
        (Fraction(10), "10.0"),
        (Fraction(20), "20.0"),
        (Fraction(-3, 2), "-1.5"),
        (Fraction(1, 3), "0.̇3"),
        (Fraction(2, 3), "0.̇6"),
        (Fraction(9, 11), "0.̇8̇1"),
    ],
)
def test_decimal(f: Fraction, expect: str) -> None:
    assert f.decimal() == expect


def test_decimal__pi() -> None:
    assert Fraction(355, 113).decimal(max_dp=6, recursion=False) == "3.141592"


@mark.parametrize(
    "a, b, expect",
    [
        (Fraction(7, 4), 2, False),
        (Fraction(8, 4), 2, True),
        (Fraction(5, 4), 1.5, False),
        (Fraction(6, 4), 1.5, True),
        (Fraction(7, 4), Fraction(8, 4), False),
        (Fraction(8, 4), Fraction(8, 4), True),
    ],
)
def test_eq(a: Fraction, b: Any, expect: bool) -> None:
    assert (a == b) is expect


@mark.parametrize(
    "a, b, expect",
    [
        (Fraction(4, 3), Fraction(4, 6), Fraction(2)),
    ],
)
def test_floordiv(a: Fraction, b: Any, expect: Fraction) -> None:
    assert a / b == expect


@mark.parametrize(
    "value, expect",
    [
        (2, Fraction(2, 1)),
        (2.5, Fraction(5, 2)),
        (Fraction(3, 2), Fraction(3, 2)),
    ],
)
def test_from_any(value: Any, expect: tuple[Fraction, Fraction]) -> None:
    assert Fraction.from_any(value) == expect


def test_from_any__unhandled_type() -> None:
    with raises(TypeError) as ex:
        _ = Fraction.from_any("zero")

    assert str(ex.value) == "Cannot create a Fraction from 'zero' (str)"


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
    "a, b, expect",
    [
        (Fraction(7, 4), 2, False),
        (Fraction(8, 4), 2, True),
        (Fraction(9, 4), 2, True),
        (Fraction(5, 4), 1.5, False),
        (Fraction(6, 4), 1.5, True),
        (Fraction(7, 4), 1.5, True),
        (Fraction(7, 4), Fraction(8, 4), False),
        (Fraction(8, 4), Fraction(8, 4), True),
        (Fraction(9, 4), Fraction(8, 4), True),
    ],
)
def test_ge(a: Fraction, b: Any, expect: bool) -> None:
    assert (a >= b) is expect


@mark.parametrize(
    "a, b, expect",
    [
        (Fraction(7, 4), 2, False),
        (Fraction(8, 4), 2, False),
        (Fraction(9, 4), 2, True),
        (Fraction(5, 4), 1.5, False),
        (Fraction(6, 4), 1.5, False),
        (Fraction(7, 4), 1.5, True),
        (Fraction(7, 4), Fraction(8, 4), False),
        (Fraction(8, 4), Fraction(8, 4), False),
        (Fraction(9, 4), Fraction(8, 4), True),
    ],
)
def test_gt(a: Fraction, b: Any, expect: bool) -> None:
    assert (a > b) is expect


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
    "a, b, expect",
    [
        (Fraction(7, 4), 2, True),
        (Fraction(8, 4), 2, True),
        (Fraction(9, 4), 2, False),
        (Fraction(5, 4), 1.5, True),
        (Fraction(6, 4), 1.5, True),
        (Fraction(7, 4), 1.5, False),
        (Fraction(7, 4), Fraction(8, 4), True),
        (Fraction(8, 4), Fraction(8, 4), True),
        (Fraction(9, 4), Fraction(8, 4), False),
    ],
)
def test_le(a: Fraction, b: Any, expect: bool) -> None:
    assert (a <= b) is expect


@mark.parametrize(
    "a, b, expect",
    [
        (Fraction(7, 4), 2, True),
        (Fraction(8, 4), 2, False),
        (Fraction(9, 4), 2, False),
        (Fraction(5, 4), 1.5, True),
        (Fraction(6, 4), 1.5, False),
        (Fraction(7, 4), 1.5, False),
        (Fraction(7, 4), Fraction(8, 4), True),
        (Fraction(8, 4), Fraction(8, 4), False),
        (Fraction(9, 4), Fraction(8, 4), False),
    ],
)
def test_lt(a: Fraction, b: Any, expect: bool) -> None:
    assert (a < b) is expect


@mark.parametrize(
    "a, b, expect",
    [
        (
            Fraction(1, 2),
            2,
            Fraction(1),
        ),
        (
            Fraction(1, 2),
            0.25,
            Fraction(1, 8),
        ),
        (
            Fraction(1, 2),
            Fraction(1, 4),
            Fraction(1, 8),
        ),
    ],
)
def test_mul(a: Fraction, b: Any, expect: Fraction) -> None:
    assert (a * b) == expect


@mark.parametrize(
    "a, b, expect",
    [
        (1, Fraction(2, 3), Fraction(5, 3)),
        (1.5, Fraction(2, 3), Fraction(13, 6)),
    ],
)
def test_radd(a: Any, b: Fraction, expect: Fraction) -> None:
    assert a + b == expect


def test_reciprocal() -> None:
    assert Fraction(2, 3).reciprocal == Fraction(3, 2)


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


def test_repr() -> None:
    assert repr(Fraction(2, 3)) == "2/3"


@mark.parametrize(
    "a, b, expect",
    [
        (Fraction(100), Fraction(2, 19), Fraction(950)),
    ],
)
def test_rfloordiv(a: Any, b: Fraction, expect: Fraction) -> None:
    assert a / b == expect


@mark.parametrize(
    "a, b, expect",
    [
        (
            2,
            Fraction(1, 2),
            Fraction(1),
        ),
        (
            0.25,
            Fraction(1, 2),
            Fraction(1, 8),
        ),
    ],
)
def test_rmul(a: Any, b: Fraction, expect: Fraction) -> None:
    assert (a * b) == expect


@mark.parametrize(
    "a, b, expect",
    [
        (1, Fraction(2, 3), Fraction(1, 3)),
    ],
)
def test_rsub(a: Any, b: Fraction, expect: Fraction) -> None:
    assert a - b == expect


@mark.parametrize(
    "a, b, expect",
    [
        (4, Fraction(1, 2), Fraction(8)),
    ],
)
def test_rtruediv(a: Any, b: Fraction, expect: Fraction) -> None:
    assert a / b == expect


@mark.parametrize(
    "a, b, expect",
    [
        (Fraction(4, 3), 1, Fraction(1, 3)),
    ],
)
def test_sub(a: Fraction, b: Any, expect: Fraction) -> None:
    assert a - b == expect


@mark.parametrize(
    "a, b, expect",
    [
        (Fraction(2, 3), Fraction(4, 6), Fraction(1)),
    ],
)
def test_truediv(a: Fraction, b: Any, expect: Fraction) -> None:
    assert a / b == expect
