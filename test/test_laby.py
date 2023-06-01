import unittest
from labrinth import Labyrinth

class LabyrinthTest(unittest.TestCase):
    def test_load_labyrinth(self):
        labyrinth = Labyrinth("labyrinth.txt")
        self.assertEqual(len(labyrinth._labyrinth), 21)
        self.assertEqual(len(labyrinth._labyrinth[0]), 28)

    def test_find_start_position(self):
        labyrinth = Labyrinth("labyrinth.txt")
        start_x, start_y = labyrinth.find_start_position()
        print(start_x, start_y)
        self.assertEqual(start_x, 0)
        self.assertEqual(start_y, 1)

    def test_find_end_position(self):
        labyrinth = Labyrinth("labyrinth.txt")
        end_x, end_y = labyrinth.find_end_position()
        self.assertEqual(end_x, 22)
        self.assertEqual(end_y, 19)

    def test_solve(self):
        labyrinth = Labyrinth("labyrinth.txt")
        solution = labyrinth.solve()
        expected_solution = None
        self.assertEqual(solution, expected_solution)


if __name__ == '__main__':
    unittest.main()