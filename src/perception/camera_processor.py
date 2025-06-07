import cv2
import numpy as np

class CameraProcessor:
    def __init__(self):
        self.frame = None
        
    def process(self, image_data):
        """处理CARLA相机数据"""
        self.frame = np.frombuffer(image_data.raw_data, dtype=np.uint8)
        self.frame = cv2.imdecode(self.frame, cv2.IMREAD_COLOR)
        return self.frame