from enum import Enum
from math import modf
from typing import TypeVar

T = TypeVar('T', int, float)


class UnitEnum(Enum):
    DECIMAL = 1000
    BINARY = 1024


class ReadableSize:
    DECIMAL_SHORT_UNITS = ["B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB"]
    BINARY_SHORT_UNITS = ["B", "KiB", "MiB", "GiB", "TiB", "PiB", "EiB", "ZiB", "YiB"]

    DECIMAL_LONG_UNITS = [
        "Bytes",
        "Kilobytes",
        "Megabytes",
        "Gigabytes",
        "Terabytes",
        "Petabytes",
        "Exabytes",
        "Zettabytes",
        "Yottabytes",
    ]
    BINARY_LONG_UNITS = [
        "Bytes",
        "Kibibytes",
        "Mebibytes",
        "Gibibytes",
        "Tebibytes",
        "Pebibytes",
        "Exbibytes",
        "Zebibytes",
        "Yobibytes",
    ]

    def _validate_options(self):
        errors = list()
        if self.value < 0 and not self.allow_negative:
            errors.append(f"{self.value} cannot be negative. Use allow_negative")
        if len(errors):
            raise Exception(errors)
        return True

    def __init__(self,
                 value: T,
                 allow_negative=False,
                 short_unit=True,
                 unit: UnitEnum = UnitEnum.DECIMAL,
                 precision=2,
                 suffix=None
    ):
        self.value = value
        self.allow_negative = allow_negative
        self._validate_options()
        self.unit = unit
        self.short_unit = short_unit
        self.precision = precision
        self.suffix = "" if suffix is None else suffix

    def _detect_sign(self):
        is_negative = self.value < 0
        return "-" if is_negative else ""

    def _units(self):
        if self.unit == UnitEnum.DECIMAL:
            return self.DECIMAL_SHORT_UNITS if self.short_unit else self.DECIMAL_LONG_UNITS
        return self.BINARY_SHORT_UNITS if self.short_unit else self.BINARY_LONG_UNITS

    def _to_readable_size(self):
        idx = 0  # Use after to choose the right format for representation
        size = abs(self.value)
        while size >= self.unit.value:
            size /= self.unit.value
            idx += 1
        unit = self._units()[idx]
        if int(size) in [0, 1] and not self.short_unit:
            unit = unit[:-1]  # Remove the last s if the value is 1
        precision = self.precision
        if modf(size)[0] == 0:
            precision = 0
        return f"{size:.{precision}f} {unit}{self.suffix}"

    def compute(self):
        sign = self._detect_sign()
        readable_size = self._to_readable_size()
        return f"{sign}{readable_size}"
