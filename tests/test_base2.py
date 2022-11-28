from pytest import mark

from rebelbase import Base2, Value


def test_abs() -> None:
    assert abs(Base2(-9)).value == 9


def test_abs__idempotent() -> None:
    assert abs(Base2(9)).value == 9


@mark.parametrize(
    "value, expect",
    [
        ("", 0),
        ("0", 0),
        ("1", 1),
        ("10", 2),
        ("11", 3),
        ("-101", -5),
        ("1101.01", 13.25),
    ],
)
def test_init__string(value: str, expect: float) -> None:
    assert Base2(value).value == expect


def test_init__value() -> None:
    assert Base2(Value(2, integral=(1, 0, 1))).value == 5


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
