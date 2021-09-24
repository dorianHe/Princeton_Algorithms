import os
import unittest
from solutions.counting_inversions import CountingInversion
from solutions.fileio import ReaderFactory


class CountingInversionTest(unittest.TestCase):
    def test_general_input(self):
        question_id = 2
        file_path = os.path.join('data', 'counting_inversions', 'general_input.txt')
        reader_factory = ReaderFactory()
        reader = reader_factory.create_reader(question_id)
        array = reader.read(file_path)
        solution = CountingInversion(array)

        solution.count_inversions(array)
        res = solution.count

        self.assertEqual(res, 6)


if __name__ == '__main__':
    unittest.main()
