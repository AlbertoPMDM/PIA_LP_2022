from types import GeneratorType
import unittest
from src.python.msws32.msws32 import msws32

class test_msws64(unittest.TestCase):

    def test_randint32(self):
        #test for the func being a generator
        self.assertEqual(
            type((msws32._randint32(1))), 
            GeneratorType
            )
        #test for the func returning int types
        self.assertEqual(
            type(next((msws32._randint32(1)))), 
            int
            )
    
    def test_rand32(self):
        #test for the func being a generator
        self.assertEqual(
            type((msws32._rand32(0, 1, 1))), 
            GeneratorType
            )
        #test for the func returning float types
        self.assertEqual(
            type(next((msws32._rand32(0, 1, 1)))), 
            float
            )