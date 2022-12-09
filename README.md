# Vinculum

[![codecov](https://codecov.io/gh/cariad/vinculum/branch/main/graph/badge.svg?token=qo774jjX0W)](https://codecov.io/gh/cariad/vinculum)

**Vinculum** is a Python package for handling large numbers with high precision.

## Examples

Numbers are recorded as fractions rather than floating-point decimals, so `1.2 - 1.0` really does equal `0.2`.

Using native `float`:

```python
a = 1.2
b = 1.0
c = a - b

print(c)  # 0.19999999999999996
```

Using Vinculum [`Fraction`](https://vinculumpy.dev/fraction/):

```python
from vinculum import Fraction

a = Fraction.from_float(1.2)
b = Fraction.from_float(1.0)
c = a - b

print(c)            # 1/5
print(c.decimal())  # 0.2
```

A `Fraction` can be rendered to any arbitrary number of decimal places, but repeating digits will be noted and rendered with overhead dots:


```python
from vinculum import Fraction

print(Fraction(1146408, 364913).decimal(max_dp=999))
# 3.141592653591403978482542414219279663919893234825835199074847977463121346731
# 96076873117702027606580198567877822933137487565529317947017508282796173334466
# 02340831924321687635134949974377454352133248198885761811719505745205021470871
# 13914823533280535360483183662955279751612028072444664892727855680669090988811
# 03167056257244877546154836906331098097354711945038954490522398489502977422015
# 65852682694231227717291518800371595421374409790826854620142335296358310062946
# 51053812826618947529959195753508370488308172084853101972250920082320991578814
# 67637491676098138460400150172780909422245850380775691740223012060408919386264
# 67130521521568154601233718721996749910252580752124478985401999928750140444434
# 70087390693124114514966581075489226199121434424095606350006713929073505191648
# 42030840227670705072167886592146621249448498683247787828879760381241556206547
# 86209315645098968795301893876074571199162540112300740176425613776434382989918
# 14487288751017365783077062203867771222181725507175682971009528298525950020963

print(Fraction(1, 3).decimal())
# 0.̇3
```

Note that the latter output is `0.̇3` with a dot and not `0.3`.

Full documentation is online at **[vinculumpy.dev](https://vinculumpy.dev)**.

## Installation

**Vinculum** requires Python 3.9 or later:

```console
pip install vinculum
```

## Support

Please raise bugs, feature requests and ask questions at [github.com/cariad/vinculum/issues](https://github.com/cariad/vinculum/issues).

## The Project

**Bounden** is &copy; 2022 Cariad Eccleston and released under the [MIT License](https://github.com/cariad/vinculum/blob/main/LICENSE) at [github.com/cariad/vinculum](https://github.com/cariad/vinculum).

## The Author

Hello! 👋 I'm **Cariad Eccleston** and I'm a freelance backend and infrastructure engineer in the United Kingdom. You can find me at [cariad.earth](https://cariad.earth), [github/cariad](https://github.com/cariad), [linkedin/cariad](https://linkedin.com/in/cariad) and on Mastodon at [@cariad@tech.lgbt](https://tech.lgbt/@cariad).
