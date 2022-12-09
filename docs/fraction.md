# Fraction class

A `Fraction` class instance represents a rational number.

## Initialisation

A new `Fraction` requires a _numerator_ and _denominator_.

For example, to create the fraction `2/3`:

```python
two_thirds = Fraction(2, 3)  # 2/3
```

### From a floating-point number

A `Fraction` can also be created from a `float` by calling `from_float`.

```python
two_and_a_half = Fraction.from_float(2.5)  # 5/2
```

### From a string

Finally, a `Fraction` can also be created by passing a string to `from_string`.

The string is expected to be either:

- a fraction in the form `x/y` or `-x/y`, or:
- a decimal in the form `x`, `-x`, `x.y` or `-x.y`, where `.` is your local culture's decimal marker.

```python
two_thirds = Fraction.from_string("2/3")  # 2/3
two_and_a_half = Fraction.from_string("2.5")  # 5/2
```

## Mathematic operations

The following operations can be performed between a `Fraction` and:

- `int`
- `float`
- `str`
- other `Fraction` instances

### Addition

```python
Fraction(1, 3) + Fraction(1, 4)  # 7/12
Fraction(1, 3) + 0.25            # 7/12
Fraction(1, 3) + "0.25"          # 7/12
Fraction(1, 3) + "1/4"           # 7/12
```

### Subtraction

```python
Fraction(2, 3) - Fraction(1, 4)  # 5/12
Fraction(2, 3) - 0.25            # 5/12
Fraction(2, 3) - "0.25"          # 5/12
Fraction(2, 3) - "1/4"           # 5/12
```

### Multiplication

```python
Fraction(2, 4) * Fraction(3, 6)  # 1/4
Fraction(2, 4) * 0.5             # 1/4
Fraction(2, 4) * "0.5"           # 1/4
Fraction(2, 4) * "4/8"           # 1/4
```

### True division

```python
Fraction(20, 4) / Fraction(17, 8)  # 40/17
Fraction(20, 4) / 2.125            # 40/17
Fraction(20, 4) / "2.125"          # 40/17
Fraction(20, 4) / "17/8"           # 40/17
```

### Floor division

Floor division returns a `Fraction` that describes the integral result of the division.

```python
Fraction(20, 4) // Fraction(17, 8)  # 2/1
Fraction(20, 4) // 2.125            # 2/1
Fraction(20, 4) // "2.125"          # 2/1
Fraction(20, 4) // "17/8"           # 2/1
```

### Comparison

#### Equality

```python
Fraction(2, 4) == Fraction(3, 6)  # True
Fraction(2, 4) == 0.5             # True
Fraction(2, 4) == "0.5"           # True
Fraction(2, 4) == "4/8"           # True
```

#### Greater than

```python
Fraction(2, 3) > Fraction(1, 4)  # True
Fraction(2, 3) > 0.25            # True
Fraction(2, 3) > "0.25"          # True
Fraction(2, 3) > "1/4"           # True
```

#### Greater than or equal to

```python
Fraction(2, 3) >= Fraction(1, 4)  # True
Fraction(2, 3) >= 0.25            # True
Fraction(2, 3) >= "0.25"          # True
Fraction(2, 3) >= "1/4"           # True
```

#### Less than

```python
Fraction(2, 3) < Fraction(1, 4)  # False
Fraction(2, 3) < 0.25            # False
Fraction(2, 3) < "0.25"          # False
Fraction(2, 3) < "1/4"           # False
```

#### Less than or equal to

```python
Fraction(2, 3) <= Fraction(1, 4)  # False
Fraction(2, 3) <= 0.25            # False
Fraction(2, 3) <= "0.25"          # False
Fraction(2, 3) <= "1/4"           # False
```

## Integral and fractional parts

The `integral` property returns the integral part of the number, and `fractional` returns the fractional part.

For example, given `3/2`, the integral part is 1 (i.e. `2/2`) and the fractional part is `1/2`.

## Decimal string

The `decimal` function returns the `Fraction` as a decimal string.

```python
Fraction(33, 8).decimal()  # "4.125"
```

By default, `decimal` will return no more than 100 decimal places. To adjust this, set the `max_dp` argument. This is limited only by your available memory and patience.

```python
Fraction(355, 113).decimal(max_dp=6)  # "3.141592"
```

By default, `decimal` will monitor for recurring digits and represent them with an overhead dot.


```python
Fraction(1, 3).decimal()  # "0.̇3"
```

If you prefer, you can disable recursion tracking by setting `recursion=False`.

```python
Fraction(1, 3).decimal(max_dp=6, recursion=False)  # "0.333333"
```

Also, if you prefer, you can change the overhead dot to any string by setting `recurring_prefix`. For example, `\u0305` is an overhead line.

```python
Fraction(1, 3).decimal(recurring_prefix="\u0305")  # "0.̅3"
```

## Reciprocals

The `reciprocal` property returns the reciprocal of the `Fraction`.

```python
Fraction(1, 3).reciprocal  # 3/1
```

## Reduction

The `reduced` property returns the `Fraction` in its most-simplified form.

```python
Fraction(25767, 34356).reduced  # 3/4
```
