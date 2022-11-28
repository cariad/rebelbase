# RebelBase

[![codecov](https://codecov.io/gh/cariad/rebelbase/branch/main/graph/badge.svg?token=3YgEtYwvmb)](https://codecov.io/gh/cariad/rebelbase)

**RebelBase** is a Python package for working with numbers of different bases.

Full documentation is online at **[rebelbase.dev](https://rebelbase.dev)**.

## What does RebelBase do?

Want to work with base 3 numbers? We've got you covered.

```python
from rebelbase import Base3

# Create the base 3 value of decimal 42:
n = Base3(42)

print("n:    ", n)      #  1120
print("n + 1:", n + 1)  #  1121
print("n - 1:", n - 1)  #  1112
print("n / 2:", n / 2)  #   210
print("n * 2:", n * 2)  # 10010

# Create the base 3 value 212:
n = Base3("212")

print(int(n))           #    23
```

Need to make your own bonkers base 5 system with vowels for digits? No problem.

```python
from rebelbase.number import Number

class Base5(Number):
    @classmethod
    def digits(cls) -> tuple[str, ...]:
        return ("A", "E", "I", "O", "U")

# Create the base 5 value of decimal 42:
n = Base5(42)

print("n:    ", n)      # EOI
print("n + 1:", n + 1)  # EOO
print("n - 1:", n - 1)  # EOE
print("n / 2:", n / 2)  #  UE
print("n * 2:", n * 2)  # OEU

# Create the base 5 value OOO:
n = Base5("OOO")

print(int(n))           #  93
```

A [`rebelbase.Number`](https://rebelbase.dev/number/) can be [created](https://rebelbase.dev/create/) with [optional zero support](https://rebelbase.dev/optional-zero/) for any base.

Numbers can be initialised with their decimal value or string representation.

Support for a ton of Python [operations](https://rebelbase.dev/number/#math-operations) -- including addition, subtraction, floor and true division, multiplication, modulo and exponentiation -- works out of the box.

## Installation

**RebelBase** requires Python 3.9 or later.

```console
pip install rebelbase
```

## Support

Please raise bugs, request new features and ask questions at [github.com/cariad/rebelbase/issues](https://github.com/cariad/rebelbase/issues).

## Contributions

See [CONTRIBUTING.md](https://github.com/cariad/rebelbase/blob/main/CONTRIBUTING.md) for contribution guidelines.

In a nutshell: bugs and feature requests are gratefully received at [github.com/cariad/rebelbase/issues](https://github.com/cariad/rebelbase/issues) and I don't accept unplanned pull requests.

## The Project

**RebelBase** is &copy; 2022 Cariad Eccleston and released under the [MIT License](https://github.com/cariad/rebelbase/blob/main/LICENSE) at [cariad/rebelbase](https://github.com/cariad/rebelbase).

## The Author

Hello! 👋 I'm **Cariad Eccleston** and I'm a freelance backend and infrastructure engineer in the United Kingdom. You can find me at [cariad.earth](https://cariad.earth), [github.com/cariad](https://github.com/cariad), [linkedin.com/in/cariad](https://linkedin.com/in/cariad) and on Mastodon at [@cariad@tech.lgbt](https://tech.lgbt/@cariad).
