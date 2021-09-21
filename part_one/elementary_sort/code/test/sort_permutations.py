import os
import unittest
from solutions import ReaderFactory, SortPermutation


class SortPermutationTest(unittest.TestCase):
    def test_general_input(self):
        file_path = os.path.join('data', 'permutations', 'general_input.txt')
        question_id = 2
        reader_factory = ReaderFactory()
        reader = reader_factory.create_reader(question_id)
        a, b = reader.read(file_path)
        solution = SortPermutation()

        res = solution.is_permutation(a, b)

        self.assertTrue(res)

    def test_duplicate_input(self):
        file_path = os.path.join('data', 'permutations', 'duplicate.txt')
        question_id = 2
        reader_factory = ReaderFactory()
        reader = reader_factory.create_reader(question_id)
        a, b = reader.read(file_path)
        solution = SortPermutation()

        res = solution.is_permutation(a, b)

        self.assertTrue(res)


if __name__ == '__main__':
    unittest.main()
