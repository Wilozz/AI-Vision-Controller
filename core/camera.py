import cv2

class CameraStream:
    def __init__(self, width = 640, height = 480):
        self.cap = cv2.VideoCapture(0)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

    def read(self):
        success, frame = self.cap.read()
        
        if not success:
            return None
        else: 
            return cv2.flip(frame, 1)
    
    def release(self):
        self.cap.release()