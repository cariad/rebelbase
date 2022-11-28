from pytest import mark

from rebelbase import Base3


@mark.parametrize(
    "value, expect",
    [
        ("", 0.0),
        ("0", 0.0),
        ("1", 1.0),
        ("2", 2.0),
        ("10", 3.0),
        ("11", 4.0),
        ("-101", -10.0),
        ("102.2", 35.0 / 3),
    ],
)
def test_init__string(value: str, expect: float) -> None:
    assert float(Base3(value)) == expect


def test_int() -> None:
    assert int(Base3("102.2")) == 11
