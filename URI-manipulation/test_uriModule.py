#This is unit test code for the method uriManipulation

import unittest
from uriModule import uriManipulation
import re

class TestUriManipulation(unittest.TestCase):

    #def test(self):
        #self.assertTrue(True)

    # checking ValueError for values out of range
    def test_values(self):
        self.assertRaises(ValueError, uriManipulation, -2)  
        self.assertRaises(ValueError, uriManipulation, 0)   

    # checking TypeError for inputs other than an integer
    def test_types(self):
        self.assertRaises(TypeError, uriManipulation, 1.1)   
 
           
if __name__ == "__main__":
    unittest.main()
