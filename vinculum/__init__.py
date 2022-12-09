"""
&copy; 2022 Cariad Eccleston and released under the MIT License.

For usage and support, see https://github.com/cariad/vinculum.
"""

from importlib.resources import files

from vinculum.fraction import Fraction
from vinculum.math import greatest_common_divisor, int_to_buffer, string_to_int


def version() -> str:
    """
    Gets the package's version.
    """

    with files(__package__).joinpath("VERSION").open("r") as t:
        return t.readline().strip()


__all__ = [
    "Fraction",
    "greatest_common_divisor",
    "int_to_buffer",
    "string_to_int",
    "version",
]
