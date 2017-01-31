import unittest
from startingFunctions import *

class TestStartFunctions(unittest.TestCase):
    #Write tests in here
    def test_get_pi(self):
        """Testing the get_pi function."""
        self.assertTrue(3.1415926 == get_pi(),
                        "Is not returning 3.1415927")
        self.assertFalse(3 == get_pi())
        self.assertEqual(get_pi(),3.1415926)

    def test_max(self):
        self.assertEqual(get_max(3,5),5,
                         "Basic maximum functionality")
        self.assertEqual(get_max(5,3),5,
                         "Ensure order of arguments doens't matter")
        self.assertEqual(get_max(3,3),3,
                         "Equal arguments")
        self.assertEqual(get_max(-1,-2),-1, "Negative input")
        self.assertEqual(get_max(1,-2),1,"Pos/neg input")



    def test_is_prime(self):
        self.assertTrue(is_prime(5));
        self.assertFalse(is_prime(4), "4 should not be prime")
        self.assertTrue(is_prime(2));
        self.assertFalse(is_prime(9));
        self.assertFalse(is_prime(1));
        

unittest.main();


    
