# RebelBase

[![codecov](https://codecov.io/gh/cariad/rebelbase/branch/main/graph/badge.svg?token=3YgEtYwvmb)](https://codecov.io/gh/cariad/rebelbase)

**RebelBase** is a Python package for working with numbers of any base.

Full documentation is online at **[rebelbase.dev](https://rebelbase.dev)**.

## What does RebelBase do?

Want to work with base 3 numbers? We've got you covered.

```python
from rebelbase import Base3

n = Base3(42)           # Represent decimal 42 in base 3

print("n:    ", n)      #  "1120" (Decimal 42     == base 3  1120)
print("n + 1:", n + 1)  #  "1121" (Decimal 42 + 1 == base 3  1121)
print("n - 1:", n - 1)  #  "1112" (Decimal 42 - 1 == base 3  1112)
print("n / 2:", n / 2)  #   "210" (Decimal 42 / 2 == base 3   210)
print("n * 2:", n * 2)  # "10010" (Decimal 42 * 1 == base 3 10010)

n = Base3("212")        # Create the base 3 value 212

print(int(n))           # "23"    (Base 3 212     == decimal 23)
```

Need to make your own bonkers base 5 system with vowels for digits? No problem.

```python
from rebelbase.number import Number

class Base5(Number):
    @classmethod
    def digits(cls) -> tuple[str, ...]:
        return ("A", "E", "I", "O", "U")

n = Base5(42)           # Represent decimal 42 in base 5

print("n:    ", n)      # "EOI" (Decimal 42     == base 5 EOI)
print("n + 1:", n + 1)  # "EOO" (Decimal 42 + 1 == base 5 EOO)
print("n - 1:", n - 1)  # "EOE" (Decimal 42 - 1 == base 5 EOE)
print("n / 2:", n / 2)  #  "UE" (Decimal 42 / 2 == base 5  UE)
print("n * 2:", n * 2)  # "OEU" (Decimal 42 * 2 == base 5 OEU)

n = Base5("OOO")        # Create the base 5 value OOO

print(int(n))           # "93"  (Base 5 OOO     == decimal 93)
```

A [`Number`](https://rebelbase.dev/number/) can be [created](https://rebelbase.dev/create/) with [optional zero support](https://rebelbase.dev/optional-zero/) for any base.

Numbers can be initialised with their decimal value or string representation.

A ton of Python [operations](https://rebelbase.dev/number/#math-operations) -- including addition, subtraction, floor and true division, multiplication, modulo and exponentiation -- work out of the box.

## Installation

**RebelBase** requires Python 3.9 or later.

```console
pip install rebelbase
```

## Support

Please raise bugs, request new features and ask questions at [github.com/cariad/rebelbase/issues](https://github.com/cariad/rebelbase/issues).

## Contributions

See [CONTRIBUTING.md](https://github.com/cariad/rebelbase/blob/main/CONTRIBUTING.md) for contribution guidelines.

## The Project

**RebelBase** is &copy; 2022 Cariad Eccleston and released under the [MIT License](https://github.com/cariad/rebelbase/blob/main/LICENSE) at [cariad/rebelbase](https://github.com/cariad/rebelbase).

## The Author

Hello! ???? I'm **Cariad Eccleston** and I'm a freelance backend and infrastructure engineer in the United Kingdom. You can find me at [cariad.earth](https://cariad.earth), [github.com/cariad](https://github.com/cariad), [linkedin.com/in/cariad](https://linkedin.com/in/cariad) and on Mastodon at [@cariad@tech.lgbt](https://tech.lgbt/@cariad).
