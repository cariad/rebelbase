# Base2 class

The `Base2` class extends and simplifies [the `Number` class](./number.md) to represent base 2 numbers.

```python
from rebelbase import Base2

print(Base2(5))
# 101

print(int(Base2("101")))
# 5

print(Base2(5) + 2)
# 111

print(Base2(5) - 2)
# 11

print(Base2(5) * 2)
# 1010

print(Base2(5) / 2)
# 10.1
```
