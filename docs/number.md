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
