from pytest import mark

from rebelbase import Number
from rebelbase.base2 import Base2

b2 = Base2()


@mark.parametrize(
    "value, expect",
    [
        (0, Number(b2, True, (), ())),
        (
            0.1,
            Number(
                b2,
                True,
                (),
                (0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1),
            ),
        ),
        (0.5, Number(b2, True, (), (1,))),
        (1, Number(b2, True, (1,), ())),
        (2, Number(b2, True, (1, 0), ())),
    ],
)
def test_number(value: int, expect: Number) -> None:
    assert b2.number(value) == expect


@mark.parametrize(
    "value, expect",
    [
        (0, "0"),
        (0.1, "0.00011001100110011"),
        (0.5, "0.1"),
        (1, "1"),
        (2, "10"),
    ],
)
def test_string(value: int, expect: str) -> None:
    assert b2.string(value) == expect
