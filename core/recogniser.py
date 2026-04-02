from core.tracker import HandTracker

class GestureRecogniser(HandTracker):
    def __init__ (self):
        super().__init__()
        self.buffer = []
        self.buffer_size = 8

    def get_gesture(self, frame):
        landmarks = self.get_landmarks(frame)
        
        if not landmarks:
            self.buffer = []
            return None
        
        fingers = self._get_extended_fingers(landmarks)
        gesture = self.classify(fingers, landmarks)
            
        self.buffer.append(gesture)
        if len(self.buffer) > self.buffer_size:
            self.buffer.pop(0)

        if self.buffer.count(self.buffer[-1]) >= 6:
            return self.buffer[-1]

        return None
    
    def classify(self, fingers, landmarks):
        if fingers == [0, 0, 0, 0, 0]:
            return "fist"
        elif fingers == [1, 1, 1, 1, 1]:
            return "open_palm"
        elif fingers == [0, 1, 0, 0, 0]:
            return "point"
        elif fingers == [0, 1, 1, 0, 0]:
            return "peace"
        elif fingers == [1, 0, 0, 0, 0]:
            return "thumbs_up"
        elif fingers == [0, 0, 1, 0, 0]:
            return "fu"
        else:
            return None       
        
    def _get_extended_fingers(self, landmarks):
        tips =   [4,  8,  12, 16, 20]
        middle = [3,  6,  10, 14, 18]
        wrist = landmarks[0]
        fingers = []

        for tip, mid in zip(tips, middle):
            tip_dist = self._distance(landmarks[tip], wrist)
            mid_dist = self._distance(landmarks[mid], wrist)
            fingers.append(1 if tip_dist > mid_dist else 0)

        return fingers
    
    def _distance(self, a, b):
        return ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) ** 0.5