from pytest import mark, raises

from rebelbase import Base26C, Value


@mark.parametrize(
    "value, expect",
    [
        (+1, "A"),
        (+2, "B"),
        (+3, "C"),
        (+4, "D"),
        (+5, "E"),
        (+6, "F"),
        (+7, "G"),
        (+8, "H"),
        (+9, "I"),
        (+10, "J"),
        (+11, "K"),
        (+12, "L"),
        (+13, "M"),
        (+14, "N"),
        (+15, "O"),
        (+16, "P"),
        (+17, "Q"),
        (+18, "R"),
        (+19, "S"),
        (+20, "T"),
        (+21, "U"),
        (+22, "V"),
        (+23, "W"),
        (+24, "X"),
        (+25, "Y"),
        (+26, "Z"),
        (+27, "AA"),
        (+28, "AB"),
        (+29, "AC"),
        (+50, "AX"),
        (+51, "AY"),
        (+52, "AZ"),
        (+53, "BA"),
        (+54, "BB"),
        (+55, "BC"),
        (+700, "ZX"),
        (+701, "ZY"),
        (+702, "ZZ"),
        (+703, "AAA"),
        (+704, "AAB"),
        (+705, "AAC"),
    ],
)
def test_str(value: float, expect: str) -> None:
    b = Base26C(value)
    assert str(b) == expect


def test_str__zero() -> None:
    with raises(ValueError) as ex:
        _ = Base26C(0)

    assert str(ex.value) == "Base26C cannot represent zero"


@mark.parametrize(
    "value, expect",
    [
        ("A", Value(26, integral=(1,))),
        ("B", Value(26, integral=(2,))),
        ("C", Value(26, integral=(3,))),
        ("X", Value(26, integral=(24,))),
        ("Y", Value(26, integral=(25,))),
        ("Z", Value(26, integral=(26,))),
        ("AA", Value(26, integral=(1, 1))),
        ("AB", Value(26, integral=(1, 2))),
        ("ZZ", Value(26, integral=(26, 26))),
        ("AAA", Value(26, integral=(1, 1, 1))),
        ("AAB", Value(26, integral=(1, 1, 2))),
    ],
)
def test_make_value(value: str, expect: Value) -> None:
    assert Base26C.from_string(value) == expect
