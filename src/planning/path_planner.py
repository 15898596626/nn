import numpy as np
from typing import List

class PathPlanner:
    def __init__(self):
        self.waypoints: List[np.ndarray] = []
    
    def generate_path(self, start: np.ndarray, goal: np.ndarray) -> List[np.ndarray]:
        """A* 路径规划算法简化实现"""
        return [start, (start + goal)/2, goal]