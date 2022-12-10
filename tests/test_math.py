from io import StringIO

from pytest import mark

from vinculum import greatest_common_divisor, int_to_buffer


@mark.parametrize(
    "a, b, expect",
    [
        (0, 0, 0),
        (0, 1, 0),
        (45, 300, 15),
    ],
)
def test_greatest_common_divisor(a: int, b: int, expect: int) -> None:
    assert greatest_common_divisor(a, b) == expect


def test_int_to_buffer__leading() -> None:
    buffer = StringIO()
    int_to_buffer(300, buffer, leading_zeros=3)
    assert buffer.getvalue() == "000300"
