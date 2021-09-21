import os
import unittest
from solutions import ReaderFactory, SolutionDuplicate


class IntersectionDuplicateTest(unittest.TestCase):
    def test_general_input(self):
        file_path = os.path.join('data', 'intersection_of_two_sets', 'general_input.txt')
        question_id = 1
        reader_factory = ReaderFactory()
        reader = reader_factory.create_reader(question_id)
        a, b = reader.read(file_path)
        solution = SolutionDuplicate()

        res = solution.find(a, b)

        self.assertEqual(res, 2)

    def test_zero_count(self):
        file_path = os.path.join('data', 'intersection_of_two_sets', 'zero_count.txt')
        question_id = 1
        reader_factory = ReaderFactory()
        reader = reader_factory.create_reader(question_id)
        a, b = reader.read(file_path)
        solution = SolutionDuplicate()

        res = solution.find(a, b)

        self.assertEqual(res, 0)

    def test_duplicate_count(self):
        file_path = os.path.join('data', 'intersection_of_two_sets', 'duplicate.txt')
        question_id = 1
        reader_factory = ReaderFactory()
        reader = reader_factory.create_reader(question_id)
        a, b = reader.read(file_path)
        solution = SolutionDuplicate()

        res = solution.find(a, b)

        self.assertEqual(res, 3)


if __name__ == '__main__':
    unittest.main()
