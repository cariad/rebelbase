# Creating a new base

## A basic base

To create a new numeric base, extend the [`Number` class](./number.md) and implement the abstract `digits` class method to return the digits of the base in ascending value order.

For example, a base 4 system would look something like this:

```python
from rebelbase import Number

class Base4(Number):
    @classmethod
    def digits(cls) -> tuple[str, ...]:
        return ("0", "1", "2", "3")
```

## Custom string representation

By default, numbers are represented with a `-` to indicate negativity and a `.` to seperate the integral and fractional parts.

```python
print(Base4(-7))    # Decimal -7    == base 4 -13
print(Base4(7.75))  # Decimal  7.75 == base 4  13.3
```

To customise the string representation, override the `to_string` and `from_string` functions.

For example, to always include a sign symbol and to separate the fractional digits with a comma instead:

```python
from rebelbase import Number, Value

class Base4(Number):
    @classmethod
    def digits(cls) -> tuple[str, ...]:
        return ("0", "1", "2", "3")

    @classmethod
    def from_string(cls, v: str) -> Value:
        if not v:
            return Value(cls.base())

        positive = not v[0] == "-"

        if v[0] in ("+", "-"):
            v = v[1:]

        dot = v.find(",")

        integral_digits = v[:dot] if dot > 0 else v
        integral_bits = [cls.value_of_digit(d) for d in integral_digits]

        fractional_digits = v[dot + 1:] if dot > 0 else ""
        fractional_bits = [cls.value_of_digit(d) for d in fractional_digits]

        return Value(cls.base(), positive, integral_bits, fractional_bits)

    def to_string(self, v: Value) -> str:
        bits = ["+" if v.positive else "-"]

        if v.integral:
            bits.extend([self.digit_for_value(x) for x in v.integral])
        else:
            bits.append(self.digit_for_value(0))

        if v.fractional:
            bits.append(",")
            bits.extend([self.digit_for_value(x) for x in v.fractional])

        return "".join(bits)


print(Base4(-7))             # Decimal -7    == base 4 -13
print(Base4(7.75))           # Decimal  7.75 == base 4 +13,3
print(int(Base4("+11")))     # Base 4 +11    == decimal  5
print(float(Base4("+3,12"))) # Base 4  +3,12 == decimal  3.375
```

The `Value` class describes a number by its:

- Base as an integer decimal.
- Sign; `True` indicates a positive value.
- Tuple of integral digit values, from most-significant on the left to least-significant on the right. For example, an integral value represented by `1023` would be recorded as `(1, 0, 2, 3)`.
- Tuple of fractional digit values, from most-significant on the left to least-significant on the right. For example, a fractional value represented by `7012` would be recorded as `(7, 0, 1, 2)`.

The `value_of_digit()` function returns the integer bit value of the passed digit. Respectively, `digit_for_value()` returns the digit for any passed integer bit value.

## Numeric bases without zero

If your base won't support zero then override `supports_zero` to return `False` and don't return a zero digit from `digits`.

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

See [optional zero support](./optional-zero.md) for more information about why you might want to do this.
