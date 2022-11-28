# Base26C class

The `Base26C` class extends and simplifies [the `Number` class](./number.md) to represent a base 26 number with continuous, non-zero representation.

```python
from rebelbase import Base26C

print(Base26C(5))
# E

print(int(Base26C("ZC")))
# 679

print(Base26C("Z") + 1)
# AA

print(Base26C(5) + 2)
# G

print(Base26C(5) - 2)
# C

print(Base26C(5) * 2)
# A

print(Base26C(5) / 4)
# A.FM
```
