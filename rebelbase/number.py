from abc import ABC, abstractmethod
from math import modf
from typing import Any, List

from rebelbase.value import Value


class Number(ABC):
    """
    Number.
    """

    def __init__(self, value: float) -> None:
        self._value = value

    @property
    @abstractmethod
    def digits(self) -> tuple[Any, ...]:
        """
        The digits of this numeric system in ascending order.
        """

    @property
    def base(self) -> int:
        """
        Numeric base.

        For example, "10" describes a base 10 system.
        """

        return len(self.digits)

    @property
    def values(self) -> "Value":
        """
        Converts the decimal `value` to a number of this base.
        """

        f, i = modf(abs(self._value))

        int_bits: List[int] = []
        int_remain = int(i)

        while int_remain > 0:
            int_bits.append(int_remain % self.base)
            int_remain = int_remain // self.base

        frac_bits: List[int] = []
        frac_remain = f

        fraction_len = 16

        while frac_remain > 0 and len(frac_bits) <= fraction_len:
            frac_remain, i = modf(frac_remain * self.base)
            frac_bits.append(int(i))

        return Value(
            self.base,
            self._value >= 0,
            tuple(reversed(int_bits)),
            tuple(frac_bits),
        )

    def __str__(self) -> str:
        n = self.values

        bits: List[str] = []

        if not n.positive:
            bits.append("-")

        if n.integral:
            bits.extend([str(self.digits[x]) for x in n.integral])
        else:
            bits.append(str(self.digits[0]))

        if n.fractional:
            bits.append(".")
            bits.extend([str(self.digits[x]) for x in n.fractional])

        return "".join(bits)
