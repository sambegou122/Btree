import unittest
from source.Arbreb import *

class TestArbre(unittest.TestCase):
    
    def setUp(self):
        a = Arbreb(2,3)
        liste = [2, 4, 5, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 7, 9, 11, 13]
        for i in liste:
            a.insert(i)
    
    def tearDown(self):
        liste = [2, 4, 5, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 7, 9, 11, 13]
        for i in liste:
            a.delete(i)
    
    def Test_research(self):
        self.assertTrue(a.research(6), "Erreur de recherche")
        self.assertFalse(a.research(15), "Erreur de recherche")
    
    




if __name__ == "__main__":
    unittest.main()