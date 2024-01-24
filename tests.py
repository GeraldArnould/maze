import unittest
from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 20)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    def test_maze_create_empty(self):
        num_cols = 0
        num_rows = 0
        
        with self.assertRaises(Exception) as e:
            Maze(0, 0, num_rows, num_cols, 10, 20)
        self.assertTrue(f"cannot create a maze with {num_rows} row(s)" in str(e.exception))



if __name__ == "__main__":
    unittest.main()
