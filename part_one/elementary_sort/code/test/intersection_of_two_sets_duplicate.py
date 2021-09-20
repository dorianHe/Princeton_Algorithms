import os
import unittest
from solutions import Reader, SolutionDuplicate


class IntersectionDuplicateTest(unittest.TestCase):
    def test_general_input(self):
        file_path = os.path.join('data', 'intersection_of_two_sets', 'general_input.txt')
        a, b = Reader.read(file_path)
        solution = SolutionDuplicate()

        res = solution.find(a, b)

        self.assertEqual(res, 2)

    def test_zero_count(self):
        file_path = os.path.join('data', 'intersection_of_two_sets', 'zero_count.txt')
        a, b = Reader.read(file_path)
        solution = SolutionDuplicate()

        res = solution.find(a, b)

        self.assertEqual(res, 0)

    def test_duplicate_count(self):
        file_path = os.path.join('data', 'intersection_of_two_sets', 'duplicate.txt')
        a, b = Reader.read(file_path)
        solution = SolutionDuplicate()

        res = solution.find(a, b)

        self.assertEqual(res, 3)


if __name__ == '__main__':
    unittest.main()
