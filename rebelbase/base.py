from abc import ABC
from math import modf
from typing import Any, List, Optional

from rebelbase.number import Number
from rebelbase.protocols import BaseProtocol, NumberProtocol


class Base(ABC, BaseProtocol):
    """
    Base number factory.

    `base` is the numeric base. For example, "10" describes a base 10 system.

    `digits` describes the set of digits in ascending value order.

    `fraction_len` describes the maximum number of digits to calculate
    fractional values. Defaults to 16.
    """

    def __init__(
        self,
        base: int,
        digits: tuple[Any, ...],
        fraction_len: Optional[int],
    ) -> None:
        self._base = base
        self._digits = digits
        self._fraction_len = fraction_len

    @property
    def base(self) -> int:
        """
        Numeric base.

        For example, "10" describes a base 10 system.
        """

        return self._base

    @property
    def fraction_len(self) -> int:
        """
        Maximum number of digits to calculate fractional values.
        """

        return 16 if self._fraction_len is None else self._fraction_len

    def number(self, value: float) -> "Number":
        """
        Converts the decimal `value` to a number of this base.
        """

        f, i = modf(abs(value))

        int_bits: List[int] = []
        int_remain = int(i)

        while int_remain > 0:
            int_bits.append(int_remain % self._base)
            int_remain = int_remain // self._base

        frac_bits: List[int] = []
        frac_remain = f

        while frac_remain > 0 and len(frac_bits) <= self.fraction_len:
            frac_remain, i = modf(frac_remain * self._base)
            frac_bits.append(int(i))

        return Number(
            self,
            value >= 0,
            tuple(reversed(int_bits)),
            tuple(frac_bits),
        )

    def string(self, n: float | int | NumberProtocol) -> str:
        """
        Gets the string representation of the number `v`.
        """

        if isinstance(n, float | int):
            return self.string(self.number(n))

        bits: List[str] = []

        if not n.positive:
            bits.append("-")

        if n.integral:
            bits.extend([str(self._digits[x]) for x in n.integral])
        else:
            bits.append(str(self._digits[0]))

        if n.fractional:
            bits.append(".")
            bits.extend([str(self._digits[x]) for x in n.fractional])

        return "".join(bits)
