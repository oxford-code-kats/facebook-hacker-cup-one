import unittest
from cooking import cook

class CookingTest(unittest.TestCase):

    def test_single_input_unchanged(self):
        number = 5
        expected_output = (5, 5)
        output = cook(number)
        self.assertEqual(output, expected_output)

    def test_two_digit_no_swap(self):
        number = 22
        expected_output = (22, 22)
        output = cook(number)
        self.assertEqual(output, expected_output)


    def test_two_digit_swap_max(self):
        number = 12
        expected_output = (12, 21)
        output = cook(number)
        self.assertEqual(output, expected_output)

    def test_two_digit_swap_min(self):
        number = 31
        expected_output = (13, 31)
        output = cook(number)
        self.assertEqual(output, expected_output)

    def test_three_digit_swap_both(self):
        number = 897
        expected_output = (798, 987)
        output = cook(number)
        self.assertEqual(output, expected_output)

    def test_five_digit_swap_both(self):
        number = 31524
        expected_output = (13524, 51324)
        output = cook(number)
        self.assertEqual(output, expected_output)

    def test_three_digit_repeat(self):
        number = 211
        expected_output = (112, 211)
        output = cook(number)
        self.assertEqual(output, expected_output)

    def test_three_digit_repeat_max(self):
        number = 122
        expected_output = (122, 221)
        output = cook(number)
        self.assertEqual(output, expected_output)        

    def test_three_digit_max_first_highest(self):
        number = 918
        expected_output = (198, 981)
        output = cook(number)
        self.assertEqual(output, expected_output)        

    def test_seven_digit_max_third_highest(self):
        number = 9982369
        expected_output = (2989369, 9992368)
        output = cook(number)
        self.assertEqual(output, expected_output)    

    def test_three_digit_min_first_position(self):
        number = 132
        expected_output = (123, 312)
        output = cook(number)
        self.assertEqual(output, expected_output)

    def test_number_with_zero(self):
        number = 101
        expected_output = (101, 110)
        output = cook(number)
        self.assertEqual(output, expected_output)

    def test_number_with_zeroes(self):
        number = 1010
        expected_output = (1001, 1100)
        output = cook(number)
        self.assertEqual(output, expected_output)

    def test_number_with_more_zeroes(self):
        number = 1000
        expected_output = (1000, 1000)
        output = cook(number)
        self.assertEqual(output, expected_output)

if __name__ == '__main__':
    unittest.main()