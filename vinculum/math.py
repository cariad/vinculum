def greatest_common_divisor(a: int, b: int) -> int:
    """
    Gets the greatest common divisor of `a` and `b`.
    """

    biggest = max(a, b)
    smallest = min(a, b)

    if smallest in (0, biggest):
        return smallest

    while True:
        remainder = biggest % smallest

        if remainder == 0:
            return smallest

        biggest = smallest
        smallest = remainder
