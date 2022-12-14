from pytest import mark, raises

from rebelbase import Base2, Value


def require_base2(_: Base2) -> None:
    pass


def test_abs() -> None:
    assert abs(Base2(-9)).value == 9


def test_abs__idempotent() -> None:
    assert abs(Base2(9)).value == 9


def test_abs__type() -> None:
    require_base2(abs(Base2(-9)))


def test_add_float() -> None:
    assert Base2(2) + 3.5 == 5.5


def test_add_int() -> None:
    assert Base2(2) + 3 == 5


def test_add_int__reverse() -> None:
    assert 3 + Base2(2) == 5


def test_add__int__reverse__type() -> None:
    require_base2(3 + Base2(2))


def test_add__int__type() -> None:
    require_base2(Base2(2) + 3)


def test_add_number() -> None:
    assert Base2(2) + Base2(3) == 5


def test_add_string() -> None:
    assert Base2(2) + "11" == 5


def test_floor_division() -> None:
    assert Base2(9) // 2 == 4


def test_floor_division__reverse() -> None:
    assert 13 // Base2(6) == 2


def test_floor_division__reverse__type() -> None:
    require_base2(13 // Base2(6))


def test_floor_division__type() -> None:
    require_base2(Base2(9) // 2)


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


def test_mod() -> None:
    assert Base2(9) % 2 == 1


def test_mod__reverse() -> None:
    assert 9 % Base2(4) == 1


def test_mod__reverse__type() -> None:
    require_base2(9 % Base2(4))


def test_mod__type() -> None:
    require_base2(Base2(9) % 2)


def test_multiply() -> None:
    assert Base2(9) * 3 == 27


def test_multiply__reverse() -> None:
    assert 3 * Base2(9) == 27


def test_multiply__reverse__type() -> None:
    require_base2(3 * Base2(9))


def test_multiply__type() -> None:
    require_base2(Base2(9) * 3)


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


def test_pow() -> None:
    assert pow(Base2(3), 2) == 9


def test_pow__reverse() -> None:
    assert pow(2, Base2(3)) == 8


def test_pow__reverse__type() -> None:
    require_base2(pow(2, Base2(3)))


def test_pow__type() -> None:
    require_base2(pow(Base2(3), 2))


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


def test_subtract__reverse__type() -> None:
    require_base2(4 - Base2(9))


def test_subtract__type() -> None:
    require_base2(Base2(9) - 4)


def test_true_division() -> None:
    assert Base2(9) / 2 == 4.5


def test_true_division__reverse() -> None:
    assert 15 / Base2(6) == 2.5


def test_true_division__type() -> None:
    require_base2(Base2(9) / 2)


def test_true_division__reverse__type() -> None:
    require_base2(15 / Base2(6))
