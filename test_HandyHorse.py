


import unittest
from HandyHorse import amount_of_possible_numbers

class Test_amount_of_possible_numbers_start(unittest.TestCase):
    
    def test_amount_of_possible_numbers_start1_movecount0(self):
        self.assertEqual(amount_of_possible_numbers(1, 0), 1)

    def test_amount_of_possible_numbers_start1_movecount1(self):
        self.assertEqual(amount_of_possible_numbers(1, 1), 2)

    def test_amount_of_possible_numbers_start1_movecount2(self):
        self.assertEqual(amount_of_possible_numbers(1, 2), 5)

    def test_amount_of_possible_numbers_start1_movecount3(self):
        self.assertEqual(amount_of_possible_numbers(1, 3), 10)

    def test_amount_of_possible_numbers_start1_movecount8(self):
        self.assertEqual(amount_of_possible_numbers(1, 8), 712)

    def test_amount_of_possible_numbers_start5_movecount0(self):
        self.assertEqual(amount_of_possible_numbers(5, 0), 1)

    def test_amount_of_possible_numbers_start5_movecount3(self):
        self.assertEqual(amount_of_possible_numbers(5, 3), 0)

    def test_amount_of_possible_numbers_start0_movecount1(self):
        self.assertEqual(amount_of_possible_numbers(0, 1), 2)  

    def test_amount_of_possible_numbers_char_number_of_moves(self):
        with self.assertRaises(TypeError):
            amount_of_possible_numbers(1,'R')

    def test_amount_of_possible_numbers_char_start_number(self):
        with self.assertRaises(TypeError):
            amount_of_possible_numbers('s', 1)

    def test_amount_of_possible_numbers_negative_number_of_moves(self):
        with self.assertRaises(TypeError):
            amount_of_possible_numbers(1,-5)
    
    def test_amount_of_possible_numbers_start_number_too_high(self):
        with self.assertRaises(TypeError):
            amount_of_possible_numbers(10,1)

    def test_amount_of_possible_numbers_negative_start_number(self):
        with self.assertRaises(TypeError):
            amount_of_possible_numbers(-1,3)

    
    

if __name__ == '__main__':
    unittest.main()