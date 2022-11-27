"""
&copy; 2022 Cariad Eccleston and released under the MIT License.

For usage and support, see https://github.com/cariad/rebelbase.
"""

from importlib.resources import files

from rebelbase.base2 import Base2
from rebelbase.number import Number
from rebelbase.value import Value


def version() -> str:
    """
    Gets the package's version.
    """

    with files(__package__).joinpath("VERSION").open("r") as t:
        return t.readline().strip()


__all__ = [
    "Base2",
    "Number",
    "Value",
    "version",
]
