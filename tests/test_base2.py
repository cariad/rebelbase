from pytest import mark

from rebelbase.base2 import Base2


@mark.parametrize(
    "value, expect",
    [
        (+0, "0"),
        (+1, "1"),
        (+1.25, "1.01"),
        (+2, "10"),
        (-1, "-1"),
        (-2, "-10"),
        (-3, "-11"),
        (-4, "-100"),
    ],
)
def test_str(value: float, expect: str) -> None:
    b = Base2(value)
    assert str(b) == expect
