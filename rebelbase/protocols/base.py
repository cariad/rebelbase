from typing import Protocol

from rebelbase.protocols.number import NumberProtocol


class BaseProtocol(Protocol):
    """
    Base number factory protocol.
    """

    @property
    def base(self) -> int:
        ...

    def string(self, v: NumberProtocol) -> str:
        ...
