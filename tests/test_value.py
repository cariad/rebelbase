from rebelbase import Value


def test_abs() -> None:
    assert abs(Value(3, False, (1,), (2,))) == Value(3, True, (1,), (2,))


def test_repr() -> None:
    assert repr(Value(3, False, (1,), (2,))) == "-(1,).(2,)"
