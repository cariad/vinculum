from pytest import mark

from vinculum import greatest_common_divisor


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
