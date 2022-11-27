from typing import Any

from rebelbase.number import Number


class Base2(Number):
    """
    A base 2 number.
    """

    @property
    def digits(self) -> tuple[Any, ...]:
        """
        The digits of this base 2 numeric system.
        """

        return (0, 1)
