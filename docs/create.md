# Creating a new numeric base

## A basic base

To create a new numeric base, extend `Number` and add a `digits` class method that returns the digits of the base in ascending value order.

For example, the base 4 system looks like this:

```python
from rebelbase import Number

class Base4(Number):
    @classmethod
    def digits(cls) -> tuple[str, ...]:
        return ("0", "1", "2", "3")
```

The class can be used immediately:

```python
n = Base4(6)
print(n)
# 12
```

## Custom string representation

By default, numbers are represented with a `-` to indicate negativity and a `.` to seperate the integral and fractional parts.

```python
print(Base4(-7))
# -13

print(Base4(7.75))
# 13.3
```

To customise the string representation, override `__str__` and `from_string`.

For example, to always include a sign symbol and to separate the fractional digits with a comma instead:

```python
from typing import List

from rebelbase import Number, Value

class Base4(Number):
    @classmethod
    def digits(cls) -> tuple[str, ...]:
        return ("0", "1", "2", "3")

    def __str__(self) -> str:
        v = self.values

        bits: List[str] = [
            "+" if v.positive else "-"
        ]

        digits = self.digits()

        if v.integral:
            bits.extend([str(digits[x]) for x in v.integral])
        else:
            bits.append(str(digits[0]))

        if v.fractional:
            bits.append(",")
            bits.extend([str(digits[x]) for x in v.fractional])

        return "".join(bits)

    @classmethod
    def from_string(cls, v: str) -> Value:
        if not v:
            return Value(cls.base())

        positive = v[0] == "+"
        v = v[1:]

        dot_index = v.find(",")

        if dot_index > 0:
            integral_string = v[:dot_index]
            fractional_string = v[dot_index + 1:]
        else:
            integral_string = v
            fractional_string = None

        digits = cls.digits()

        integral_bits: List[int] = []
        for digit in integral_string:
            digit_value = digits.index(digit)
            integral_bits.append(digit_value)

        fractional_bits: List[int] = []
        if fractional_string:
            for fv in fractional_string:
                fractional_bits.append(digits.index(fv))

        return Value(cls.base(), positive, integral_bits, fractional_bits)


print(Base4(-7))
# -13

print(Base4(7.75))
# +13,3

n = Base4("+11")
print(int(n))
# 5

n = Base4("+3,12")
print(float(n))
# 3.375
```

The `Value` class describes a number by recording its base and series of bits as tuples. The `.digits()` tuple is used to translate between digits and decimal values.

## Numeric bases without zero

If your numeric base won't support zero then override `supports_zero` to return `False`.

```python
from rebelbase import Number

class Base4(Number):
    @classmethod
    def digits(cls) -> tuple[str, ...]:
        return ("1", "2", "3")

    @classmethod
    def supports_zero(cls) -> bool:
        return False
```

See [optional zero support](./optional_zero.md) for more information about why you might want to do this.
