import unittest
from math_quiz import generateRandomInteger, getRandomOperator, calculateExpression


class TestMathGame(unittest.TestCase):

    def test_generateRandomInteger(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = generateRandomInteger(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_getRandomOperator(self):
        # Test if the operators are identified properly
        possibleOperators = ['+', '-', '*', '/']
        for _ in range(1000):  # Test a large number of random operator generations
            operator = getRandomOperator()
            self.assertIn(operator, possibleOperators)

    def test_calculateExpression(self):
        # Test 
        test_cases = [
            (5, 2, '+', '5 + 2', 7),
            (10, 5, '-', '10 - 5', 5),
            (3, 4, '*', '3 * 4', 12)
        ]

        for num1, num2, operator, expected_problem, expected_answer in test_cases:
            problem, answer = calculateExpression(num1, num2, operator)
            self.assertEqual(problem, expected_problem)
            self.assertEqual(answer, expected_answer)
                
if __name__ == "__main__":
    unittest.main()
