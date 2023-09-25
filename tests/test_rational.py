from typing import Any

from pytest import mark, raises

from vinculum import Rational


@mark.parametrize(
    "a, b, expect",
    [
        (Rational(2, 3), 1, Rational(5, 3)),
        (Rational(2, 3), 1.5, Rational(13, 6)),
        (Rational(2, 3), Rational(4, 6), Rational(4, 3)),
        (Rational(1, 4), Rational(-1, 2), Rational(-1, 4)),
    ],
)
def test_add(a: Rational, b: Any, expect: Rational) -> None:
    assert a + b == expect


@mark.parametrize(
    "a, b, expect",
    [
        (
            Rational.ZERO(),
            Rational.ZERO(),
            (Rational.ZERO(), Rational.ZERO()),
        ),
        (
            Rational(3, 2),
            Rational(15, 30),
            (Rational(90, 60), Rational(30, 60)),
        ),
    ],
)
def test_comparable(a: Rational, b: Rational, expect: Rational) -> None:
    assert Rational.comparable(a, b) == expect


@mark.parametrize(
    "f, other, expect",
    [
        (Rational(3, 2), 1, (Rational(3, 2), Rational(2, 2))),
        (Rational(3, 2), 1.5, (Rational(3, 2), Rational(3, 2))),
        (
            Rational(3, 2),
            Rational(15, 30),
            (Rational(90, 60), Rational(30, 60)),
        ),
    ],
)
def test_comparable_with_self(
    f: Rational,
    other: Any,
    expect: tuple[Rational, Rational],
) -> None:
    assert f.comparable_with_self(other) == expect


@mark.parametrize(
    "f, expect",
    [
        (Rational.ZERO(), "0.0"),
        (Rational(1), "1.0"),
        (Rational(2), "2.0"),
        (Rational(10), "10.0"),
        (Rational(20), "20.0"),
        (Rational(-3, 2), "-1.5"),
        (Rational(1, 3), "0.̇3"),
        (Rational(2, 3), "0.̇6"),
        (Rational(9, 11), "0.̇8̇1"),
        (Rational(3, 10), "0.3"),
        (Rational(3, 100), "0.03"),
        (Rational(3, 1000), "0.003"),
        (Rational(303, 10000), "0.0303"),
    ],
)
def test_decimal(f: Rational, expect: str) -> None:
    assert f.decimal() == expect


def test_decimal__pi() -> None:
    assert Rational(355, 113).decimal(max_dp=6, recursion=False) == "3.141592"


@mark.parametrize(
    "a, b, expect",
    [
        (Rational(7, 4), 2, False),
        (Rational(8, 4), 2, True),
        (Rational(5, 4), 1.5, False),
        (Rational(6, 4), 1.5, True),
        (Rational(67, 99), 0.67676767676, True),
        (Rational(7, 4), Rational(8, 4), False),
        (Rational(8, 4), Rational(8, 4), True),
    ],
)
def test_eq(a: Rational, b: Any, expect: bool) -> None:
    assert (a == b) is expect


@mark.parametrize(
    "f, expect",
    [
        (Rational.ZERO(), 0),
        (Rational(1), 1),
        (Rational(1, 3), 0.3333333333333333),
    ],
)
def test_float(f: Rational, expect: float) -> None:
    assert float(f) == expect


@mark.parametrize(
    "a, b, expect",
    [
        (Rational(20, 4), "2.125", Rational(2)),
    ],
)
def test_floordiv(a: Rational, b: Any, expect: Rational) -> None:
    assert a // b == expect


@mark.parametrize(
    "f, expect",
    [
        (Rational.ZERO(), Rational.ZERO()),
        (Rational(1), Rational.ZERO()),
        (Rational(3, 2), Rational(1, 2)),
    ],
)
def test_fractional(f: Rational, expect: Rational) -> None:
    assert f.fractional == expect


@mark.parametrize(
    "value, expect",
    [
        (2, Rational(2, 1)),
        (2.5, Rational(5, 2)),
        (Rational(3, 2), Rational(3, 2)),
    ],
)
def test_from_any(value: Any, expect: tuple[Rational, Rational]) -> None:
    assert Rational.from_any(value) == expect


def test_from_any__unhandled_type() -> None:
    with raises(TypeError) as ex:
        _ = Rational.from_any(["zero"])

    assert str(ex.value) == "Cannot create a Rational from ['zero'] (list)"


@mark.parametrize(
    "f, expect",
    [
        (1.0, Rational(1)),
        (1.2, Rational(6, 5)),
        (1.5, Rational(3, 2)),
        (1.25, Rational(5, 4)),
        (-1.25, Rational(-5, 4)),
    ],
)
def test_from_float(f: float, expect: Rational) -> None:
    assert Rational.from_float(f) == expect


@mark.parametrize(
    "s, expect",
    [
        ("0", Rational.ZERO()),
        ("0.0", Rational.ZERO()),
        ("1", Rational(1)),
        ("1.0", Rational(1)),
        ("1.2", Rational(6, 5)),
        ("1.25", Rational(5, 4)),
        ("1.125", Rational(9, 8)),
        ("2.5", Rational(5, 2)),
        ("99.75", Rational(399, 4)),
        ("0/1", Rational.ZERO()),
        ("1/1", Rational(1)),
        ("2/1", Rational(2)),
        ("2/3", Rational(2, 3)),
        ("123/456", Rational(123, 456)),
        ("-7", -7),
        ("-7.3", -7.3),
    ],
)
def test_from_string(s: str, expect: Rational | float) -> None:
    rational = Rational.from_string(s)
    assert rational == expect


def test_from_string__unrecognised() -> None:
    with raises(ValueError) as ex:
        _ = Rational.from_string("foo")

    assert str(ex.value) == 'Cannot parse "foo" as decimal or fraction'


@mark.parametrize(
    "a, b, expect",
    [
        (Rational(7, 4), 2, False),
        (Rational(8, 4), 2, True),
        (Rational(9, 4), 2, True),
        (Rational(5, 4), 1.5, False),
        (Rational(6, 4), 1.5, True),
        (Rational(7, 4), 1.5, True),
        (Rational(7, 4), Rational(8, 4), False),
        (Rational(8, 4), Rational(8, 4), True),
        (Rational(9, 4), Rational(8, 4), True),
    ],
)
def test_ge(a: Rational, b: Any, expect: bool) -> None:
    assert (a >= b) is expect


@mark.parametrize(
    "a, b, expect",
    [
        (Rational(7, 4), 2, False),
        (Rational(8, 4), 2, False),
        (Rational(9, 4), 2, True),
        (Rational(5, 4), 1.5, False),
        (Rational(6, 4), 1.5, False),
        (Rational(7, 4), 1.5, True),
        (Rational(7, 4), Rational(8, 4), False),
        (Rational(8, 4), Rational(8, 4), False),
        (Rational(9, 4), Rational(8, 4), True),
    ],
)
def test_gt(a: Rational, b: Any, expect: bool) -> None:
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
    f = Rational(n, d)
    assert f.denominator == expect_d
    assert f.numerator == expect_n


@mark.parametrize(
    "f, expect",
    [
        (Rational.ZERO(), 0),
        (Rational(1), 1),
        (Rational(1, 2), 0),
        (Rational(2, 2), 1),
        (Rational(3, 2), 1),
        (Rational(5, 2), 2),
    ],
)
def test_int(f: Rational, expect: int) -> None:
    assert int(f) == expect


@mark.parametrize(
    "a, b, expect",
    [
        (Rational(7, 4), 2, True),
        (Rational(8, 4), 2, True),
        (Rational(9, 4), 2, False),
        (Rational(5, 4), 1.5, True),
        (Rational(6, 4), 1.5, True),
        (Rational(7, 4), 1.5, False),
        (Rational(7, 4), Rational(8, 4), True),
        (Rational(8, 4), Rational(8, 4), True),
        (Rational(9, 4), Rational(8, 4), False),
    ],
)
def test_le(a: Rational, b: Any, expect: bool) -> None:
    assert (a <= b) is expect


@mark.parametrize(
    "a, b, expect",
    [
        (Rational(7, 4), 2, True),
        (Rational(8, 4), 2, False),
        (Rational(9, 4), 2, False),
        (Rational(5, 4), 1.5, True),
        (Rational(6, 4), 1.5, False),
        (Rational(7, 4), 1.5, False),
        (Rational(7, 4), Rational(8, 4), True),
        (Rational(8, 4), Rational(8, 4), False),
        (Rational(9, 4), Rational(8, 4), False),
    ],
)
def test_lt(a: Rational, b: Any, expect: bool) -> None:
    assert (a < b) is expect


@mark.parametrize(
    "a, b, expect",
    [
        (
            Rational(1, 2),
            0,
            Rational.ZERO(),
        ),
        (
            Rational(1, 2),
            1,
            Rational(1, 2),
        ),
        (
            Rational(1, 2),
            2,
            Rational(1),
        ),
        (
            Rational(1, 2),
            0.25,
            Rational(1, 8),
        ),
        (
            Rational(1, 2),
            Rational(1, 4),
            Rational(1, 8),
        ),
    ],
)
def test_mul(a: Rational, b: Any, expect: Rational) -> None:
    result = a * b
    assert result == expect


@mark.parametrize(
    "a, b, expect",
    [
        (1, Rational(2, 3), Rational(5, 3)),
        (1.5, Rational(2, 3), Rational(13, 6)),
    ],
)
def test_radd(a: Any, b: Rational, expect: Rational) -> None:
    assert a + b == expect


def test_reciprocal() -> None:
    assert Rational(2, 3).reciprocal == Rational(3, 2)


@mark.parametrize(
    "f, expect",
    [
        (Rational.ZERO(), Rational.ZERO()),
        (Rational(1), Rational(1)),
        (Rational(1, 2), Rational(1, 2)),
        (Rational(15, 30), Rational(1, 2)),
    ],
)
def test_reduced(f: Rational, expect: Rational) -> None:
    assert f.reduced == expect


def test_repr() -> None:
    assert repr(Rational(2, 3)) == "2/3"


@mark.parametrize(
    "a, b, expect",
    [
        ("20/4", Rational(17, 8), Rational(2)),
    ],
)
def test_rfloordiv(a: Any, b: Rational, expect: Rational) -> None:
    assert a // b == expect


@mark.parametrize(
    "a, b, expect",
    [
        (
            0,
            Rational(1, 2),
            Rational.ZERO(),
        ),
        (
            1,
            Rational(1, 2),
            Rational(1, 2),
        ),
        (
            2,
            Rational(1, 2),
            Rational(1),
        ),
        (
            0.25,
            Rational(1, 2),
            Rational(1, 8),
        ),
    ],
)
def test_rmul(a: Any, b: Rational, expect: Rational) -> None:
    result = a * b
    assert result == expect


@mark.parametrize(
    "a, b, expect",
    [
        (1, Rational(2, 3), Rational(1, 3)),
        (Rational(4, 7), Rational(1, 7), Rational(3, 7)),
        (Rational(1, 7), Rational(4, 7), Rational(-3, 7)),
    ],
)
def test_rsub(a: Any, b: Rational, expect: Rational) -> None:
    assert a - b == expect


@mark.parametrize(
    "a, b, expect",
    [
        (4, Rational(1, 2), Rational(8)),
    ],
)
def test_rtruediv(a: Any, b: Rational, expect: Rational) -> None:
    assert a / b == expect


@mark.parametrize(
    "a, b, expect",
    [
        (Rational(4, 3), 1, Rational(1, 3)),
    ],
)
def test_sub(a: Rational, b: Any, expect: Rational) -> None:
    assert a - b == expect


@mark.parametrize(
    "a, b, expect",
    [
        (Rational(2, 3), Rational(4, 6), Rational(1)),
    ],
)
def test_truediv(a: Rational, b: Any, expect: Rational) -> None:
    assert a / b == expect
