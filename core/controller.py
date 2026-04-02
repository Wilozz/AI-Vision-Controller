from pynput.keyboard import Key, Controller

class KeyboardController:
    def __init__(self):
        self.keyboard = Controller()
        self.current_gesture = None

        self.gesture_map = {
            "fist":       Key.space,
            "open_palm":  Key.esc,
            "point":      Key.up,
            "peace":      Key.down,
            "thumbs_up":  Key.enter
        }

    def handle(self, gesture):
        if gesture == self.current_gesture:
            return

        if self.current_gesture and self.current_gesture in self.gesture_map:
            self.keyboard.release(self.gesture_map[self.current_gesture])

        self.current_gesture = gesture

        if gesture and gesture in self.gesture_map:
            self.keyboard.press(self.gesture_map[gesture])