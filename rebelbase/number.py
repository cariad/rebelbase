from rebelbase.protocols import BaseProtocol


class Number:
    """
    A raw numeric value.

    `base` describes the numeric base.

    `positive` indicates whether the value is positive or negative. Zero must
    be considered positive.

    `integral` is a tuple that describes the decimal value of each digit of the
    integral part of the value, from most- to least-significant. For example,
    (1, 0) indicates "10" in base 10.

    `fractional` is a tuple that describes the decimal value of each digit of
    the fractional part of the value, from most- to least-significant. For
    example, (0, 1) indicates "0.25" in base 10.
    """

    def __init__(
        self,
        base: BaseProtocol,
        positive: bool,
        integral: tuple[int, ...],
        fractional: tuple[int, ...],
    ) -> None:
        self._base = base
        self._positive = positive
        self._integral = integral
        self._fractional = fractional

    def __abs__(self) -> "Number":
        return Number(self.base, True, self.integral, self.fractional)

    def __eq__(self, other: object) -> bool:
        return (
            isinstance(other, Number)
            and self.base.base == other.base.base
            and self.positive == other.positive
            and self.integral == other.integral
            and self.fractional == other.fractional
        )

    def __repr__(self) -> str:
        sign = "+" if self._positive else "-"
        return f"{sign}{self._integral}.{self._fractional}"

    def __str__(self) -> str:
        return self._base.string(self)

    @property
    def base(self) -> BaseProtocol:
        """
        Numeric base.
        """

        return self._base

    @property
    def fractional(self) -> tuple[int, ...]:
        """
        The decimal value of each digit of the fractional part of the value,
        from most- to least-significant.

        For example, (0, 1) indicates "0.25" in base 10.
        """

        return self._fractional

    @property
    def integral(self) -> tuple[int, ...]:
        """
        The decimal value of each digit of the integral part of the value, from
        most- to least-significant.

        For example, (1, 0) indicates "10" in base 10.
        """

        return self._integral

    @property
    def positive(self) -> bool:
        """
        Value is positive or negative.
        """

        return self._positive
