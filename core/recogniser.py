from core.tracker import HandTracker

class GestureRecogniser(HandTracker):
    def __init__ (self):
        super().__init__()

    def get_gesture(self, frame):
        landmarks = self.get_landmarks(frame)
        
        if not landmarks:
            return None
        
        fingers = self._get_extended_fingers(landmarks)
        
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
        tips =    [4,  8,  12, 16, 20]
        middle =  [3,  6,  10, 14, 18]
        fingers = []

        for i, (tip, mid) in enumerate(zip(tips, middle)):
            if i == 0:
                fingers.append(1 if landmarks[tip][0] > landmarks[mid][0] else 0)
            else:
                fingers.append(1 if landmarks[tip][1] < landmarks[mid][1] else 0)

        return fingers