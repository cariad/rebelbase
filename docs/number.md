# Number class

The `Number` class is the base for all numbers. All of the provided numeric classes extend and simplify this class.

## Construction

To construct a `Number`, either:

- Pass in the decimal value as a float or integer:

    ```python
    from rebelbase import Base2

    n = Base2(22)
    print(n)
    # 10110
    ```

- Pass in the string representation of the number in its base form:

    ```python
    from rebelbase import Base2

    n = Base2("10110")
    print(int(n))
    # 22
    ```

## String representation

Cast a `Number` to a string to get a representation of its base value. For example, to cast a base 2 number to a series of `0` and `1`:

```python
from rebelbase import Base2

print(Base2(12))
# 1100
```

## Math operations

### Absolute value

Given a positive or negative `Number` _n_, `abs(n)` returns a `Number` of the positive value of _n_.

```python
from rebelbase import Base2

n = Base2(-17)
print(abs(n))
# 10001
```

### Addition

Adding a float, integer, string or `Number` to a `Number` will return a new `Number` with the summed value, even if the bases are different:

```python
from rebelbase import Base2, Base3

a = Base2(2)

print(a + Base2(3))
print(a + Base3("10"))
print(a + "11")
print(a + 3)
# 101
```

### Conversion to float

Given a `Number` _n_, `float(n)` returns a `Number` of the float value of _n_.

```python
from rebelbase import Base2

n = Base2(3)
print(float(n))
# 3.0
```

### Conversion to integer

Given a `Number` _n_, `int(n)` returns a `Number` of the int value of _n_.

```python
from rebelbase import Base2

n = Base2(3.4)
print(int(n))
# 3
```

### Equality

A `Number` is considered equal to a float, integer, string or another `Number` if the represented value is the same, even if the bases are different:

```python
from rebelbase import Base2, Base3

a = Base2(2)

print(a == Base2(2))
print(a == Base3("2"))
print(a == "10")
print(a == 2)
# True
```

### Exponentiation

Raising a float, integer, string or `Number` to a power represented by a `Number` (or vice versa) will return a new `Number` with the exponentiated value, even if the bases are different:

```python
from rebelbase import Base2, Base3

n = Base2(8)

print(n ** Base2(3))
print(n ** Base3("10"))
print(n ** "11")
print(n ** 3)
# 1000000000
```

### Division

Dividing a float, integer, string or `Number` by a `Number` (or vice versa) will return a new `Number` with the divided value, even if the bases are different:

```python
from rebelbase import Base2, Base3

n = Base2(13.2)

print(n / Base2(3))
print(n / Base3("10"))
print(n / "11")
print(n / 3)
# 100.01100110011001100

print(n // Base2(3))
print(n // Base3("10"))
print(n // "11")
print(n // 3)
# 100
```

### Modulo

Reducing a float, integer, string or `Number` modulo a `Number` (or vice versa) will return a new `Number` with the modulus value, even if the bases are different:

```python
from rebelbase import Base2, Base3

n = Base2(8)

print(n % Base2(3))
print(n % Base3("10"))
print(n % "11")
print(n % 3)
# 10
```

### Multiplication

Multiplying a float, integer, string or `Number` by a `Number` (or vice versa) will return a new `Number` with the multiplied value, even if the bases are different:

```python
from rebelbase import Base2, Base3

n = Base2(8)

print(n * Base2(3))
print(n * Base3("10"))
print(n * "11")
print(n * 3)
# 11000
```

### Subtraction

Subtracting a float, integer, string or `Number` from a `Number` (or vice versa) will return a new `Number` with subtracted value, even if the bases are different:

```python
from rebelbase import Base2, Base3

a = Base2(17)

print(a - Base2(3))
print(a - Base3("10"))
print(a - "11")
print(a - 3)
# 1110
```
