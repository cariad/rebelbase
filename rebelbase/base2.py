from typing import Optional

from rebelbase.base import Base


class Base2(Base):
    """
    Base 2 number factory.

    `fraction_len` describes the maximum number of digits to calculate
    fractional values. Defaults to 16.
    """

    def __init__(self, fraction_len: Optional[int] = None) -> None:
        super().__init__(2, (0, 1), fraction_len)
