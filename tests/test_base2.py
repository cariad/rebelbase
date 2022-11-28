from pytest import mark, raises

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


def test_parse__fail() -> None:
    with raises(ValueError) as ex:
        assert Base2.parse((0, 0))

    assert str(ex.value) == "Base2 cannot parse (0, 0) (tuple)"


def test_parse__float() -> None:
    assert Base2.parse(9.5) == 9.5


def test_parse__int() -> None:
    assert Base2.parse(9) == 9


def test_parse__number() -> None:
    assert Base2.parse(Base2(9)) == 9


def test_parse__string() -> None:
    assert Base2.parse("1001") == 9


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


def test_subtract() -> None:
    assert Base2(9) - 4 == 5


def test_subtract__reverse() -> None:
    assert 4 - Base2(9) == -5
