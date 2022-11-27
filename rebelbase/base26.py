from typing import Any

from rebelbase.number import Number


class Base26(Number):
    """
    A base 26 number.
    """

    @property
    def digits(self) -> tuple[Any, ...]:
        """
        The digits of this numeric system in ascending order.
        """

        return tuple([chr(n) for n in range(65, 65 + 26)])
