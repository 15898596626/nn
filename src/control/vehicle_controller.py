import numpy as np

class VehicleController:
    def __init__(self):
        self.speed = 0
        self.steering = 0
        
    def update(self, target_speed, target_angle):
        """PID控制逻辑简化版"""
        self.speed = 0.8 * target_speed + 0.2 * self.speed
        self.steering = np.clip(target_angle, -1, 1)
        return self.speed, self.steering