# unit-converter-cli

A command-line unit converter for length, weight and temperature, written in Python using only the standard library.

## Requirements

- Python 3.8 or later. No third-party packages are needed.

## Usage

```bash
python converter.py length 5 km m
python converter.py weight 2 lb kg
python converter.py temp 100 c f
```

The general form is:

```bash
python converter.py <kind> <value> <from_unit> <to_unit>
```

- `kind`: `length`, `weight` or `temp`
- `value`: the number to convert
- `from_unit` / `to_unit`: the units to convert between

### Examples

```bash
python converter.py length 5 km m      # 5 km = 5000.0 m
python converter.py length 1 mi km      # 1 mi = 1.609344 km
python converter.py weight 2 lb kg      # 2 lb = 0.90718474 kg
python converter.py temp 100 c f        # 100 c = 212.0 f
python converter.py temp 32 f c         # 32 f = 0.0 c
```

List all supported units:

```bash
python converter.py --list
```

### Supported units

- Length: mm, cm, m, km, in, ft, yd, mi
- Weight: mg, g, kg, t, oz, lb
- Temperature: c, f, k
