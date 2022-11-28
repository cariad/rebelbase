# Optional zero support

A `Number` doesn't have to support zero values.

But why would you _not_ want to?

## Why?

Spreadsheets, for example, have two axes:

1. Integer _y_ axes that run from 1 to infinity
1. String _x_ axes that run from `A` to `Z`, then `AA` to `ZZ`, then `AAA` to `ZZZ`, and so on to infinity

At first glance, that _x_ axis might feel like a base 26 number with digits `A`=0, `B`=1, through to `Z`=25:

```
Decimal: | 0 | 1 | 2 | 3 | 4 | ... | 23 | 24 | 25
Digits:  | A | B | C | D | E | ... |  X |  Y |  Z
```

...but consider the consequences of that approach:

- _x_ axes would start at decimal 0, which is inconsistent with _y_ axes starting at decimal 1.
- If `Z` represented decimal value 25 then we'd want `AA` to represent decimal value 25 &plus; 1 -- but decimal 26 would _actually_ be `BA`:

    ```
    Powers:  | 26^1 | 26^0 |
    Value:   | 1x26 |  0x1 | = 26
    Digits:  | B    |  A   | = BA
    ```

The solution is to create a base 26 system without zero.

The digits and their decimal values look like this:

```
Decimal: | 1 | 2 | 3 | 4 | 5 | ... | 24 | 25 | 26
Digits:  | A | B | C | D | E | ... |  X |  Y |  Z
```

In this system, when we're forced to work without zero, `Z` represents decimal 26 and `AA` correctly represents decimal 26&plus;1:

```
Powers:  | 26^1 | 26^0 |
Value:   | 1x26 |  1x1 | = 27
Digits:  | A    |  A   | = AA
```

## Implementation

To create a `Number` without zero, see [the `Number` class / "Numeric bases without zero"](./create.md#numeric-bases-without-zero).
