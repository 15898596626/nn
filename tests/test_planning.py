import unittest
import numpy as np
from src.planning.path_planner import PathPlanner

class TestPathPlanner(unittest.TestCase):
    def test_path_generation(self):
        planner = PathPlanner()
        path = planner.generate_path(np.array([0,0]), np.array([2,2]))
        self.assertEqual(len(path), 3)

if __name__ == "__main__":
    unittest.main()