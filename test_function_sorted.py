import unittest
from function_sorted import is_sorted


class TestSorted(unittest.TestCase):

    def test_leer(self):
        """testet eine leere liste 
            Leere liste gilt als sortiert"""
        lst = []
        result = is_sorted(lst)
        self.assertTrue(result)

    def test_sortiert(self):
        """testet sortierte liste """
        lst = [1,4,67,90]
        result = is_sorted(lst)
        self.assertTrue(result)

    def test_unsortiert(self):
        """testet ob eine liste unsortiert ist """
        lst = [1,4,2,90]
        result = is_sorted(lst)
        self.assertFalse(result)

    def test_SameValues(self):
        """testet ob die liste gleichen werten hat 
            gleichen werten liste gilt als sortiert """
        lst = [4,4,4,4,5]
        result = is_sorted(lst)
        self.assertTrue(result)

if __name__== "__main__":
    unittest.main()
