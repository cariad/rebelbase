from typing import Protocol


class NumberProtocol(Protocol):
    """
    Raw numeric value protocol.
    """

    def __abs__(self) -> "NumberProtocol":
        ...

    @property
    def fractional(self) -> tuple[int, ...]:
        ...

    @property
    def integral(self) -> tuple[int, ...]:
        ...

    @property
    def positive(self) -> bool:
        ...
