import unittest
from src.control.pid_controller import PIDController

class TestPID(unittest.TestCase):
    def test_pid_output(self):
        pid = PIDController()
        self.assertAlmostEqual(pid.compute(10, 5), 2.5)  # 0.5*(10-5)

if __name__ == "__main__":
    unittest.main()
    