# Number class

The `Number` class is the base for all numbers. All of the provided numeric classes wrap and extend this class.

## Construction

To construct a `Number`, either:

- Pass in the decimal value as a float or integer:

    ```python
    from rebelbase import Base2

    n = Base2(22)
    print(n)       # "10110" (Decimal 22 == base 2 10110)
    ```

- Pass in the string representation of the number in its base form:

    ```python
    from rebelbase import Base2

    n = Base2("10110")
    print(int(n))  # "22" (Base 2 10110 == decimal 22)
    ```

## String representation

Cast a `Number` to a string to get a representation of its base value. For example, to cast a base 2 number to a series of `0` and `1`:

```python
from rebelbase import Base2

print(Base2(12))  # "1100" (Decimal 12 == base 2 1100)
```

## Functions

- `.base()` gets the base of the number. For example, `10` to indicate a base 10 number.
- `.digits()` gets a tuple of the digits that make up the number's numeric system in ascending value order.
- `.from_string()` converts a string to internal value representation.
- `.name()` gets the name of the number's numeric system.
- `.parse()` attempts to parse any given object into a float or integer value.
- `.supports_zero()` indicates whether or not the number supports zero. See [optional zero support](./optional-zero.md) for more information about why zero might be unsupported.
- `.to_string()` converts internal value representation to a string.

## Properties

- `.value` gets the decimal value as a float or int. This value can also be read by passing the `Number` into `float()` or `int()`.
- `.values` gets the internal representation of the value.

## Math operations

### Absolute value

Given a positive or negative `Number` _n_, `abs(n)` returns a `Number` of the positive value of _n_.

```python
from rebelbase import Base2

n = Base2(-17)
print(abs(n))  # "10001" (Decimal 17 == base 2 10001)
```

### Addition

Adding a float, integer, string or `Number` to a `Number` will return a new `Number` with the summed value, even if the bases are different:

```python
from rebelbase import Base2, Base3

a = Base2(2)

print(a + Base2(3))     # "101" (Base 2 10 + base 2 11 == base 2 101)
print(a + Base3("10"))  # "101" (Base 2 10 + base 3 10 == base 2 101)
print(a + "11")         # "101" (Base 2 10 + base 2 11 == base 2 101)
print(a + 3)            # "101" (Base 2 10 + decimal 3 == base 2 101)
```

### Conversion to float

Given a `Number` _n_, `float(n)` returns a `Number` of the float value of _n_.

```python
from rebelbase import Base2

n = Base2(3)
print(float(n))  # "3.0"
```

### Conversion to integer

Given a `Number` _n_, `int(n)` returns a `Number` of the int value of _n_.

```python
from rebelbase import Base2

n = Base2(3.4)
print(int(n))  # 3
```

### Equality

A `Number` is considered equal to a float, integer, string or another `Number` if the represented value is the same, even if the bases are different:

```python
from rebelbase import Base2, Base3

a = Base2(2)

print(a == Base2(2))   # "True" (Base 2 10 == base 2 10)
print(a == Base3("2")) # "True" (Base 2 10 == base 3 2)
print(a == "10")       # "True" (Base 2 10 == base 2 10)
print(a == 2)          # "True" (Base 2 10 == decimal 2)
```

### Exponentiation

Raising a float, integer, string or `Number` to a power represented by a `Number` (or vice versa) will return a new `Number` with the exponentiated value, even if the bases are different:

```python
from rebelbase import Base2, Base3

n = Base2(8)

print(n ** Base2(3))     # "1000000000" (Base 2 1000 ** base 2 11 == base 2 1000000000)
print(n ** Base3("10"))  # "1000000000" (Base 2 1000 ** base 3 10 == base 2 1000000000)
print(n ** "11")         # "1000000000" (Base 2 1000 ** base 2 11 == base 2 1000000000)
print(n ** 3)            # "1000000000" (Base 2 1000 ** decimal 3 == base 2 1000000000)
```

### Division

Dividing a float, integer, string or `Number` by a `Number` (or vice versa) will return a new `Number` with the divided value, even if the bases are different:

```python
from rebelbase import Base2, Base3

n = Base2(13.2)

print(n / Base2(3))     # "100.01100110011001100" (Base 2 1101.00110011001100110 / base 2 11 == base 2 100.01100110011001100)
print(n / Base3("10"))  # "100.01100110011001100" (Base 2 1101.00110011001100110 / base 3 10 == base 2 100.01100110011001100)
print(n / "11")         # "100.01100110011001100" (Base 2 1101.00110011001100110 / base 2 11 == base 2 100.01100110011001100)
print(n / 3)            # "100.01100110011001100" (Base 2 1101.00110011001100110 / decimal 3 == base 2 100.01100110011001100)

print(n // Base2(3))     # "100" (Base 2 1101.00110011001100110 // base 2 11 == base 2 100)
print(n // Base3("10"))  # "100" (Base 2 1101.00110011001100110 // base 3 10 == base 2 100)
print(n // "11")         # "100" (Base 2 1101.00110011001100110 // base 2 11 == base 2 100)
print(n // 3)            # "100" (Base 2 1101.00110011001100110 // decimal 3 == base 2 100)
```

### Modulo

Reducing a float, integer, string or `Number` modulo a `Number` (or vice versa) will return a new `Number` with the modulus value, even if the bases are different:

```python
from rebelbase import Base2, Base3

n = Base2(8)

print(n % Base2(3))     # "10" (Base 2 1000 % base 2 11 == base 2 10)
print(n % Base3("10"))  # "10" (Base 2 1000 % base 3 10 == base 2 10)
print(n % "11")         # "10" (Base 2 1000 % base 2 11 == base 2 10)
print(n % 3)            # "10" (Base 2 1000 % decimal 3 == base 2 10)
```

### Multiplication

Multiplying a float, integer, string or `Number` by a `Number` (or vice versa) will return a new `Number` with the multiplied value, even if the bases are different:

```python
from rebelbase import Base2, Base3

n = Base2(8)

print(n * Base2(3))     # "11000" (Base 2 1000 * base 2 11 == base 2 11000)
print(n * Base3("10"))  # "11000" (Base 2 1000 * base 3 10 == base 2 11000)
print(n * "11")         # "11000" (Base 2 1000 * base 2 11 == base 2 11000)
print(n * 3)            # "11000" (Base 2 1000 * decimal 3 == base 2 11000)
```

### Subtraction

Subtracting a float, integer, string or `Number` from a `Number` (or vice versa) will return a new `Number` with subtracted value, even if the bases are different:

```python
from rebelbase import Base2, Base3

a = Base2(17)

print(a - Base2(3))     # "1110" (Base 2 10001 - base 2 11 == base 2 1110)
print(a - Base3("10"))  # "1110" (Base 2 10001 - base 3 10 == base 2 1110)
print(a - "11")         # "1110" (Base 2 10001 - base 2 11 == base 2 1110)
print(a - 3)            # "1110" (Base 2 10001 - decimal 3 == base 2 1110)
```
