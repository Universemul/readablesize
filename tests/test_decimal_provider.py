import unittest

from readablesize import ReadableSize


class ReadableSizeWithDecimalTest(unittest.TestCase):

    def test_simple_values(self):
        self.assertEqual("0 B", ReadableSize(0).compute())
        self.assertEqual("1 KB", ReadableSize(1000).compute())
        self.assertEqual("1.02 KB", ReadableSize(1023).compute())
        self.assertEqual("5.50 KB", ReadableSize(5500).compute())

    def test_long_unit(self):
        self.assertEqual("0 Byte", ReadableSize(0, short_unit=False).compute())
        self.assertEqual("1 Kilobyte", ReadableSize(1000, short_unit=False).compute())
        self.assertEqual("10.02 Kilobytes", ReadableSize(10023, short_unit=False).compute())
        self.assertEqual("10.50 Kilobytes", ReadableSize(10499, short_unit=False).compute())

    def test_negative_values(self):
        self.assertEqual("-400 B", ReadableSize(-400, allow_negative=True).compute())

    def test_precision(self):
        self.assertEqual("100.04800 KB", ReadableSize(100048, precision=5).compute())
        self.assertEqual("100 KB", ReadableSize(100048, precision=0).compute())

    def test_suffix(self):
        self.assertEqual("10 KB/s", ReadableSize(10000, suffix="/s").compute())

if __name__ == "__main__":
    unittest.main()
