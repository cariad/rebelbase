from pytest import mark

from rebelbase import Base26


@mark.parametrize(
    "value, expect",
    [
        (+0, "A"),
        (+1, "B"),
        (+1.25, "B.GN"),
        (+2, "C"),
        (+10, "K"),
        (-1, "-B"),
        (-2, "-C"),
        (-3, "-D"),
        (-4, "-E"),
        (-10, "-K"),
    ],
)
def test_str(value: float, expect: str) -> None:
    b = Base26(value)
    assert str(b) == expect
