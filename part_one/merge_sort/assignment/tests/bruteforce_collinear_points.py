import os
import unittest
from solution import Reader, Point, BruteCollinearPoints


class BruteCollinearPointsTest(unittest.TestCase):
    def test_general_input(self):
        file_path = os.path.join('data', 'general_input.txt')
        data = Reader.read(file_path)
        solution = BruteCollinearPoints(data)

        res = solution.number_of_segments()

        self.assertEqual(res, 1)


if __name__ == '__main__':
    unittest.main()
