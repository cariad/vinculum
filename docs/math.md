# Mathematic functions

## greatest_common_divisor

The `greatest_common_divisor` function returns the greatest common divisor (GCD) -- also known as the _greatest common factor_ (GCF), _highest common divisor_ (HCD), and _highest common factor_ (HCF) -- of two integers.

```python
greatest_common_divisor(25767, 34356)  # 8589
```

## int_to_buffer

The `int_to_buffer` function writes an integer to a string buffer, avoiding the [CVE-2020-10735](https://github.com/python/cpython/issues/95778) vulnerabilty and breaking change for direct conversion of integers to strings.

## string_to_int

The `string_to_int` converts a string to an integer, avoiding the [CVE-2020-10735](https://github.com/python/cpython/issues/95778) vulnerabilty and breaking change for direct conversion of integers to strings.
