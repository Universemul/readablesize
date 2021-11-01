import unittest

from readablesize import ReadableSize, UnitEnum


class ReadableSizeWithBinaryTest(unittest.TestCase):

    def setUp(self) -> None:
        self.unit = UnitEnum.BINARY

    def test_simple_values(self):
        self.assertEqual("0 B", ReadableSize(0, unit=self.unit).compute())
        self.assertEqual("999 B", ReadableSize(999, unit=self.unit).compute())
        self.assertEqual("1000 B", ReadableSize(1000, unit=self.unit).compute())
        self.assertEqual("1023 B", ReadableSize(1023, unit=self.unit).compute())
        self.assertEqual("1 KiB", ReadableSize(1024, unit=self.unit).compute())

    def test_long_unit(self):
        params = {
            'unit': self.unit,
            'short_unit': False
        }
        self.assertEqual("0 Byte", ReadableSize(0, **params).compute())
        self.assertEqual("999 Bytes", ReadableSize(999, **params).compute())
        self.assertEqual("1000 Bytes", ReadableSize(1000, **params).compute())
        self.assertEqual("1023 Bytes", ReadableSize(1023, **params).compute())
        self.assertEqual("1 Kibibyte", ReadableSize(1024, **params).compute())

    def test_negative_values(self):
        self.assertEqual("-400 B", ReadableSize(-400, allow_negative=True, unit=self.unit).compute())

    def test_precision(self):
        self.assertEqual("97.70312 KiB", ReadableSize(100048, precision=5, unit=self.unit).compute())
        self.assertEqual("97.703 KiB", ReadableSize(100048, precision=3, unit=self.unit).compute())
        self.assertEqual("98 KiB", ReadableSize(100048, precision=0, unit=self.unit).compute())

    def test_suffix(self):
        self.assertEqual("9.77 KiB/s", ReadableSize(10000, unit=self.unit, suffix="/s").compute())


if __name__ == "__main__":
    unittest.main()
