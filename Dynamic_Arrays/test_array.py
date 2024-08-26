from Dynamic_Arrays import DynamicArray
from unittest import TestCase


class TestFunction(TestCase):
    def test_array_init(self):
        arr = DynamicArray()
        self.assertEqual(arr.length, 0)
        self.assertEqual(arr.data, {})
