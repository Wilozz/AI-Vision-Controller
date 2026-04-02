import cv2
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision

class HandTracker:
    def __init__(self, model_path="hand_landmarker.task", max_hands=1, detection_confidence=0.7, tracking_confidence=0.7):
        base_options = python.BaseOptions(model_asset_path=model_path)
        options = vision.HandLandmarkerOptions(
            base_options=base_options,
            num_hands=max_hands,
            min_hand_detection_confidence=detection_confidence,
            min_hand_presence_confidence=tracking_confidence
        )
        self.detector = vision.HandLandmarker.create_from_options(options)
        self.results = None

    def find_hands(self, frame):
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb)
        self.results = self.detector.detect(mp_image)

        if self.results.hand_landmarks:
            for hand_landmarks in self.results.hand_landmarks:
                self._draw_landmarks(frame, hand_landmarks)

        return frame

    def _draw_landmarks(self, frame, landmarks):
        h, w, _ = frame.shape
        points = []

        for point in landmarks:
            x = int(point.x * w)
            y = int(point.y * h)
            points.append((x, y))
            cv2.circle(frame, (x, y), 5, (0, 255, 0), -1)

        connections = [
            (0,1),(1,2),(2,3),(3,4),
            (0,5),(5,6),(6,7),(7,8),
            (0,9),(9,10),(10,11),(11,12),
            (0,13),(13,14),(14,15),(15,16),
            (0,17),(17,18),(18,19),(19,20),
            (5,9),(9,13),(13,17)
        ]

        for start, end in connections:
            cv2.line(frame, points[start], points[end], (0, 200, 255), 2)

    def get_landmarks(self, frame):
        landmarks = []

        if self.results and self.results.hand_landmarks:
            for hand_landmarks in self.results.hand_landmarks:
                h, w, _ = frame.shape
                for point in hand_landmarks:
                    # Multiplies the hand coordinates with frame dimensions to get actual size
                    x = int(point.x * w)
                    y = int(point.y * h)
                    landmarks.append((x, y))

        return landmarks