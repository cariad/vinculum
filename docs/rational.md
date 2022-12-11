# Rational class

A `Rational` class instance represents a rational number.

## Initialisation

A new `Rational` requires a _numerator_ and _denominator_.

For example, to create the rational number `2/3`:

```python
two_thirds = Rational(2, 3)  # 2/3
```

### From a floating-point number

A `Rational` can also be created from a `float` by calling `from_float`.

```python
two_and_a_half = Rational.from_float(2.5)  # 5/2
```

### From a string

Finally, a `Rational` can also be created by passing a string to `from_string`.

The string is expected to be either:

- a fraction in the form `x/y` or `-x/y`, or:
- a decimal in the form `x`, `-x`, `x.y` or `-x.y`, where `.` is your local culture's decimal marker.

```python
two_thirds = Rational.from_string("2/3")  # 2/3
two_and_a_half = Rational.from_string("2.5")  # 5/2
```

## Mathematic operations

The following operations can be performed between a `Rational` and:

- `int`
- `float`
- `str`
- other `Rational` instances

### Addition

```python
Rational(1, 3) + Rational(1, 4)  # 7/12
Rational(1, 3) + 0.25            # 7/12
Rational(1, 3) + "0.25"          # 7/12
Rational(1, 3) + "1/4"           # 7/12
```

### Subtraction

```python
Rational(2, 3) - Rational(1, 4)  # 5/12
Rational(2, 3) - 0.25            # 5/12
Rational(2, 3) - "0.25"          # 5/12
Rational(2, 3) - "1/4"           # 5/12
```

### Multiplication

```python
Rational(2, 4) * Rational(3, 6)  # 1/4
Rational(2, 4) * 0.5             # 1/4
Rational(2, 4) * "0.5"           # 1/4
Rational(2, 4) * "4/8"           # 1/4
```

### True division

```python
Rational(20, 4) / Rational(17, 8)  # 40/17
Rational(20, 4) / 2.125            # 40/17
Rational(20, 4) / "2.125"          # 40/17
Rational(20, 4) / "17/8"           # 40/17
```

### Floor division

Floor division returns a `Rational` that describes the integral result of the division.

```python
Rational(20, 4) // Rational(17, 8)  # 2/1
Rational(20, 4) // 2.125            # 2/1
Rational(20, 4) // "2.125"          # 2/1
Rational(20, 4) // "17/8"           # 2/1
```

### Comparison

#### Equality

```python
Rational(2, 4) == Rational(3, 6)  # True
Rational(2, 4) == 0.5             # True
Rational(2, 4) == "0.5"           # True
Rational(2, 4) == "4/8"           # True
```

#### Greater than

```python
Rational(2, 3) > Rational(1, 4)  # True
Rational(2, 3) > 0.25            # True
Rational(2, 3) > "0.25"          # True
Rational(2, 3) > "1/4"           # True
```

#### Greater than or equal to

```python
Rational(2, 3) >= Rational(1, 4)  # True
Rational(2, 3) >= 0.25            # True
Rational(2, 3) >= "0.25"          # True
Rational(2, 3) >= "1/4"           # True
```

#### Less than

```python
Rational(2, 3) < Rational(1, 4)  # False
Rational(2, 3) < 0.25            # False
Rational(2, 3) < "0.25"          # False
Rational(2, 3) < "1/4"           # False
```

#### Less than or equal to

```python
Rational(2, 3) <= Rational(1, 4)  # False
Rational(2, 3) <= 0.25            # False
Rational(2, 3) <= "0.25"          # False
Rational(2, 3) <= "1/4"           # False
```

## Integral and fractional parts

The `integral` property returns the integral part of the number, and `fractional` returns the fractional part.

For example, given `3/2`, the integral part is 1 (i.e. `2/2`) and the fractional part is `1/2`.

## Decimal string

The `decimal` function returns the `Rational` as a decimal string.

```python
Rational(33, 8).decimal()  # "4.125"
```

By default, `decimal` will return no more than 100 decimal places. To adjust this, set the `max_dp` argument. This is limited only by your available memory and patience.

```python
Rational(355, 113).decimal(max_dp=6)  # "3.141592"
```

By default, `decimal` will monitor for recurring digits and represent them with an overhead dot.


```python
Rational(1, 3).decimal()  # "0.̇3"
```

If you prefer, you can disable recursion tracking by setting `recursion=False`.

```python
Rational(1, 3).decimal(max_dp=6, recursion=False)  # "0.333333"
```

Also, if you prefer, you can change the overhead dot to any string by setting `recurring_prefix`. For example, `\u0305` is an overhead line.

```python
Rational(1, 3).decimal(recurring_prefix="\u0305")  # "0.̅3"
```

!!! tip

    To get the true floating-point value of a `Rational`, convert it to a `float` via Python's built-in `float()` function.

    ```python
    float(Rational(4, 3))  # 1.3333333333333333
    ```

## Reciprocals

The `reciprocal` property returns the reciprocal of the `Rational`.

```python
Rational(1, 3).reciprocal  # 3/1
```

## Reduction

The `reduced` property returns the `Rational` in its most-simplified form.

```python
Rational(25767, 34356).reduced  # 3/4
```

## Converting to floating-point and integer numbers

To get the true floating-point value of a `Rational`, convert it to a `float` via Python's built-in `float()` function.

```python
float(Rational(4, 3))  # 1.3333333333333333
```

Likewise, use the built-in `int()` function to get the integral value as an `int`.

```python
int(Rational(4, 3))  # 1
```
