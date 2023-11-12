import unittest
from math_quiz import generate_random_integer, generate_random_operator, perform_operation
# Jin Huang / an46ykim /23079099

class TestMathGame(unittest.TestCase):

    def test_generate_random_integer(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = generate_random_integer(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_generate_random_operator(self):
        operator = generate_random_operator()
        valid_operators = {'+', '-', '*'}
        self.assertIn(operator, valid_operators, f"Generated operator '{operator}' is not in {valid_operators}")

    def test_perform_operation(self):

        test_cases = [(5, 2, '+', '5 + 2', 7), (5, 3, '-', '5 - 3', 2)]
        # TODO add more test cases here
        # for num1, num2, operator, expected_problem, expected_answer in test_cases:
        for num1, num2, operator, expected_problem, expected_answer in test_cases:
            # Use subTest to identify specific test cases when multiple are present
            with self.subTest(num1=num1, num2=num2, operator=operator):

                # Call the perform_operation function with current test case parameters
                problem_expression, result = perform_operation(num1, num2, operator)

                # Check if the generated problem expression matches the expected one
                self.assertEqual(problem_expression, expected_problem, f"Test failed for {num1} {operator} {num2}")

                # Check if the calculated result matches the expected answer
                self.assertEqual(result, expected_answer, f"Test failed for {num1} {operator} {num2}")


if __name__ == "__main__":
    unittest.main()
