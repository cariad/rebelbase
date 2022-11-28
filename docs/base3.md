# Base3 class

The `Base3` class extends and simplifies [the `Number` class](./number.md) to represent base 3 numbers.

```python
from rebelbase import Base3

print(Base3(5))
# 12

print(int(Base3("101")))
# 10

print(Base3(5) + 2)
# 21

print(Base3(5) - 2)
# 10

print(Base3(5) * 2)
# 101

print(Base3(5) / 3)
# 1.2
```
