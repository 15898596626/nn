import unittest
from src.control.vehicle_controller import VehicleController

class TestVehicle(unittest.TestCase):
    def test_control_update(self):
        ctrl = VehicleController()
        speed, angle = ctrl.update(10.0, 0.5)
        self.assertAlmostEqual(speed, 8.0)  # 10*0.8 + 0*0.2

if __name__ == "__main__":
    unittest.main()
    