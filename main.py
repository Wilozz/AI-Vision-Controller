import cv2
from core.camera import CameraStream
from core.recogniser import GestureRecogniser
from core.controller import KeyboardController

cam = CameraStream()
recogniser = GestureRecogniser()
controller = KeyboardController()

while True:
    frame = cam.read()
    
    if frame is None:
        break

    frame = recogniser.find_hands(frame)
    gesture = recogniser.get_gesture(frame)

    controller.handle(gesture)

    if gesture:
        cv2.putText(frame, gesture, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255, 255, 255), 2)

    cv2.imshow("Gesture Controller", frame)

    # Press q on the window to close 
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()