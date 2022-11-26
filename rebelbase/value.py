class Value:
    """
    A raw numeric value.

    `base` describes the numeric base. For example, "10" to indicate base 10.

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
        base: int,
        positive: bool,
        integral: tuple[int, ...],
        fractional: tuple[int, ...],
    ) -> None:
        self._base = base
        self._positive = positive
        self._integral = integral
        self._fractional = fractional

    def __eq__(self, other: object) -> bool:
        return (
            isinstance(other, Value)
            and self.base == other.base
            and self.positive == other.positive
            and self.integral == other.integral
            and self.fractional == other.fractional
        )

    @property
    def base(self) -> int:
        """
        Numeric base.

        For example, "10" to indicate base 10.
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
