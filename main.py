import cv2
from core.camera import CameraStream

cam = CameraStream()

while True:
    frame = cam.read()
    
    if frame is None:
        break

    cv2.imshow("Gesture Controller", frame)

    # Press q on the window to close 
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()