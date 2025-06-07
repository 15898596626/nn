class PIDController:
    def __init__(self):
        self.kp = 0.5
        self.ki = 0.1
        self.kd = 0.2
        
    def compute(self, target, current):
        return (target - current) * self.kp