from pytest import mark

from rebelbase import Value


def test_abs() -> None:
    assert abs(Value(3, False, (1,), (2,))) == Value(3, True, (1,), (2,))


@mark.parametrize(
    "value, expect",
    [
        (Value(2, integral=()), 0),
        (Value(2, integral=(1,)), 1),
        (Value(2, integral=(1,0)), 2),
        (Value(2, integral=(1,), fractional=(1,)), 1.5),
        (Value(2, integral=(1,), fractional=(1, 1)), 1.75),
        (Value(2, integral=(1,), fractional=(1, 1), positive=False), -1.75),
        (Value(10, integral=()), 0),
        (Value(10, integral=(1,)), 1),
        (Value(10, integral=(2,)), 2),
        (Value(10, integral=(3,)), 3),
        (Value(10, integral=(1, 1)), 11),
        (Value(10, integral=(2,), fractional=(1,)), 2.1),
    ],
)
def test_float(value: Value, expect: float) -> None:
    assert value.float == expect


def test_repr() -> None:
    assert repr(Value(3, False, (1,), (2,))) == "-(1,).(2,)b3"
