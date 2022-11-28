# Optional zero support

In **RebelBase**, a `Number` doesn't have to support the value _zero_.

But why would you want to disable it?

## Why?

Let's take spreadsheets for example. Spreadsheets have two axes:

1. Integer _y_ axes that runs from 1 to infinity
1. String _x_ axes that runs from `A` to `Z`, then `AA`-`ZZ`, then `AAA`-`ZZZ`, and so on to infinity.

At first glance, that _x_ axis might feel like a base 26 number with digits `A`=0, `B`=1, through to `Z`=25:

```
Decimal: | 0 | 1 | 2 | 3 | 4 | ... | 23 | 24 | 25
Digits:  | A | B | C | D | E | ... |  X |  Y |  Z
```

...but consider the consequences of that approach:

- _x_ axes would start at decimal 0, which is inconsistent with _y_ axes starting at decimal 1.
- Given that decimal 25 would be represented by`Z`, we'd want decimal 26 to be `AA` -- but decimal 26 would _actually_ be `BA`:

    ```
    Powers:  | 26^1 | 26^0 |
    Digits:  |    B |    A | = BA
    Decimal: |    1 |    0 |
    Value:   | 1x26 |  0x1 | = 26
    ```

The solution is to create a base 26 system without zero.

The digits and their decimal values look like this:

```
Decimal: | 1 | 2 | 3 | 4 | 5 | ... | 24 | 25 | 26
Digits:  | A | B | C | D | E | ... |  X |  Y |  Z
```

In this system, `Z` represents decimal 26 and `AA` correct represents decimal 26&plus;1:

```
Powers:  | 26^1 | 26^0 |
Digits:  |    A |    A | = AA
Decimal: |    1 |    1 |
Value:   | 1x26 |  1x1 | = 27
```

## Implementation

To create a `Number` without zero, see [the `Number` class / "Numeric bases without zero"](./create.md#numeric-bases-without-zero).
