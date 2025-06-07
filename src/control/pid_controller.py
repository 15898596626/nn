import numpy as np

class PIDController:
    def __init__(self, kp=0.5, ki=0.1, kd=0.2):
        self.kp = kp
        self.ki = ki
        self.kd = kd
        self.prev_error = 0
        self.integral = 0
        
    def compute(self, target, current, dt=0.1):
        error = target - current
        self.integral += error * dt
        derivative = (error - self.prev_error) / dt
        output = self.kp*error + self.ki*self.integral + self.kd*derivative
        self.prev_error = error
        return np.clip(output, -1.0, 1.0)