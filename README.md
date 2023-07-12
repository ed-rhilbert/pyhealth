# pyhealth

![](pyhealth.png)
Python package to calculate health indicators

- Renan HILBERT
- v0.0.1 (July 2023)

# Installation

```bash
 pip install git+https://github.com/ed-rhilbert/pyhealth
```

# Getting started

```python
>>> from pyhealth.calculations.calculate import calculate_bmi

>>> heights = [1.75, 1.65, 1.80]
>>> weights = [80, 55, 95.2]

>>> bmis = calculate_bmi(heights, weights)
>>> print(bmis)

[26.122448979591837, 20.202020202020204, 29.382716049382715]
```

# Contribution

```bash
git clone git@github.com:ed-rhilbert/pyhealth.git
cd pyhealth/
python3 -m venv venv
source venv/bin activate
pip install -r requirements.txt
pip install -e .
```

## Tests

```bash
pytest
```

## Test with code coverage

```bash
pytest --cov
```

## Documentation

TO DO
