import unittest
from binary_search import binary_search  # assuming your function is in binary_search.py

class TestBinarySearch(unittest.TestCase):

    def test_found(self):
        arr = [1, 3, 5, 7, 9, 11]
        target = 7
        self.assertEqual(binary_search(arr, target), 3)  # index of 7 is 3

    def test_not_found(self):
        arr = [1, 3, 5, 7, 9, 11]
        target = 8
        self.assertEqual(binary_search(arr, target), -1)  # 8 is not in the list

    def test_empty_list(self):
        arr = []
        target = 5
        self.assertEqual(binary_search(arr, target), -1)

    def test_single_element_found(self):
        arr = [10]
        target = 10
        self.assertEqual(binary_search(arr, target), 0)

    def test_single_element_not_found(self):
        arr = [10]
        target = 5
        self.assertEqual(binary_search(arr, target), -1)

    def test_duplicates(self):
        arr = [1, 2, 2, 2, 3, 4]
        target = 2
        index = binary_search(arr, target)
        self.assertIn(index, [1, 2, 3])  # any index of the duplicates is acceptable

if __name__ == "__main__":
    unittest.main()