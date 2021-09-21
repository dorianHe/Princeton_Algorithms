import os
import unittest
from solutions import ReaderFactory, DutchFlag


class DutchFlagTest(unittest.TestCase):
    def test_general_input(self):
        file_path = os.path.join('data', 'dutch_flag', 'general_input.txt')
        reader_factory = ReaderFactory()
        reader = reader_factory.create_reader(3)
        arr = reader.read(file_path)
        solution = DutchFlag()

        res = solution.sort(arr)

        self.assertEqual(res, [1, 1, 1, 2, 2, 2, 3, 3, 3])

    def test_only_one(self):
        file_path = os.path.join('data', 'dutch_flag', 'only_one.txt')
        reader_factory = ReaderFactory()
        reader = reader_factory.create_reader(3)
        arr = reader.read(file_path)
        solution = DutchFlag()

        res = solution.sort(arr)

        self.assertEqual(res, [1, 1, 1, 1, 1, 1, 1])

    def test_only_two(self):
        file_path = os.path.join('data', 'dutch_flag', 'only_two.txt')
        reader_factory = ReaderFactory()
        reader = reader_factory.create_reader(3)
        arr = reader.read(file_path)
        solution = DutchFlag()

        res = solution.sort(arr)

        self.assertEqual(res, [2, 2, 2, 2, 2])

    def test_only_three(self):
        file_path = os.path.join('data', 'dutch_flag', 'only_three.txt')
        reader_factory = ReaderFactory()
        reader = reader_factory.create_reader(3)
        arr = reader.read(file_path)
        solution = DutchFlag()

        res = solution.sort(arr)

        self.assertEqual(res, [3, 3, 3, 3, 3, 3])

    def test_one_two(self):
        file_path = os.path.join('data', 'dutch_flag', 'one_two.txt')
        reader_factory = ReaderFactory()
        reader = reader_factory.create_reader(3)
        arr = reader.read(file_path)
        solution = DutchFlag()

        res = solution.sort(arr)

        self.assertEqual(res, [1, 1, 1, 2, 2, 2])


if __name__ == '__main__':
    unittest.main()
