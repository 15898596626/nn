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
        # 修改vehicle_controller.py
def update(self, target_speed, target_angle):
    # 新增加速度限制
    speed_change = np.clip(target_speed - self.speed, -2.0, 2.0)
    self.speed += speed_change * 0.5
    self.steering = np.clip(target_angle, -1, 1)
    return self.speed, self.steering