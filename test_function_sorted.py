import unittest
from function_sorted import is_sorted


class TestSorted(unittest.TestCase):

    def test_leer(self):
        """testet eine leere liste Leere liste gilt als sortiert"""
        self.assertTrue(is_sorted([]))

    def test_sortiert(self):
        """testet sortierte liste """
        self.assertTrue(is_sorted([1]))            # nur ein Wert 
        self.assertTrue(is_sorted([1,2,3,4,5]))    # positive Werte 
        self.assertTrue(is_sorted([1,2,3,3,5]))    # positive Werte mit 2 gleichen werten
        self.assertTrue(is_sorted([-10,-4,-3]))    # negative Werte
        self.assertTrue(is_sorted([-23,-4,0,6,9])) # gemischte Werte

    def test_unsortiert(self):
        """testet ob eine liste unsortiert ist """
        self.assertFalse(is_sorted([6,5,3,2,1]))    # absteigende Werte
        self.assertFalse(is_sorted([2,-5,3,4,1]))   # gemischte Werte

    def test_SameValues(self):
        """testet ob die liste gleichen werten hat 
            gleichen werten liste gilt als sortiert """
        
        self.assertTrue(is_sorted([4,4,4,4]))        # positive werte 
        self.assertTrue(is_sorted([-1,-1,-1,-1]))    # negative werte 

if __name__== "__main__":
    unittest.main()
