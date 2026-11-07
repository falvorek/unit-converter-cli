#!/usr/bin/env python3
"""Command-line unit converter (length, weight, temperature).

Only the Python standard library is used.

Usage:
    python converter.py length 5 km m
    python converter.py weight 2 lb kg
    python converter.py temp 100 c f
    python converter.py --list
"""

import argparse
import sys

LENGTH = {
    "mm": 0.001, "cm": 0.01, "m": 1.0, "km": 1000.0,
    "in": 0.0254, "ft": 0.3048, "yd": 0.9144, "mi": 1609.344,
}

WEIGHT = {
    "mg": 0.000001, "g": 0.001, "kg": 1.0, "t": 1000.0,
    "oz": 0.028349523125, "lb": 0.45359237,
}

TEMPERATURES = ("c", "f", "k")


def convert_linear(value, from_unit, to_unit, table):
    return value * table[from_unit] / table[to_unit]


def convert_temperature(value, from_unit, to_unit):
    if from_unit == "c":
        celsius = value
    elif from_unit == "f":
        celsius = (value - 32) * 5 / 9
    elif from_unit == "k":
        celsius = value - 273.15
    else:
        raise ValueError(f"Unknown temperature unit: {from_unit}")
    if to_unit == "c":
        return celsius
    if to_unit == "f":
        return celsius * 9 / 5 + 32
    if to_unit == "k":
        return celsius + 273.15
    raise ValueError(f"Unknown temperature unit: {to_unit}")


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="Convert length, weight and temperature units."
    )
    parser.add_argument("--list", action="store_true",
                        help="List the supported units and exit")
    parser.add_argument("kind", nargs="?", choices=["length", "weight", "temp"],
                        help="What to convert: length, weight or temp")
    parser.add_argument("value", nargs="?", type=float, help="Value to convert")
    parser.add_argument("from_unit", nargs="?", help="Unit to convert from")
    parser.add_argument("to_unit", nargs="?", help="Unit to convert to")
    args = parser.parse_args(argv)
    if args.list:
        print("length:", ", ".join(sorted(LENGTH)))
        print("weight:", ", ".join(sorted(WEIGHT)))
        print("temp:", ", ".join(TEMPERATURES))
        return 0
    if args.kind is None or args.value is None or not args.from_unit or not args.to_unit:
        parser.print_usage(sys.stderr)
        print("Example: python converter.py length 5 km m", file=sys.stderr)
        return 2
    from_unit = args.from_unit.lower()
    to_unit = args.to_unit.lower()
    if args.kind == "length":
        result = convert_linear(args.value, from_unit, to_unit, LENGTH)
    elif args.kind == "weight":
        result = convert_linear(args.value, from_unit, to_unit, WEIGHT)
    else:
        result = convert_temperature(args.value, from_unit, to_unit)
    print(f"{args.value} {from_unit} = {result} {to_unit}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
