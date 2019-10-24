import unittest
import get_column_stats
import random
import numpy as np

class TestMean(unittest.TestCase):
    def test_no_input(self):
        self.assertRaises(TypeError,get_column_stats.calculate_mean,None)
    def test_wrong_types(self):
        self.assertRaises(TypeError,get_column_stats.calculate_mean,1)
        self.assertRaises(TypeError,get_column_stats.calculate_mean,'text')
        self.assertRaises(TypeError,get_column_stats.calculate_mean,1.0000)
    def test_empty_list(self):
        self.assertRaises(IndexError,get_column_stats.calculate_mean,[])
    def test_bad_list_value(self):
        self.assertRaises(TypeError,get_column_stats.calculate_mean,[1,2,3,'text'])
    def test_fixed_value(self):
        self.assertEqual(get_column_stats.calculate_mean([1,1,1,1,1]),1)
    def test_random_values(self):
        for i in range(100):
            length = random.randint(1,1000)
            rand = []
            for j in range(length):
                rand.append(random.randint(1,1000))
            self.assertEqual(get_column_stats.calculate_mean(rand),np.mean(rand))
            
        
    