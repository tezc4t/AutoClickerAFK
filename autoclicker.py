import time
import threading
from pynput.mouse import Controller, Button
from pynput.keyboard import Listener, KeyCode


TOGGLE_KEY = KeyCode(char='c')
EXIT_KEY = KeyCode(char='x')

DELAY = 0.1

clicking = False
mouse = Controller()

class ClickMouse(threading.Thread):
    def __init__(self, delay, button):
        super(ClickMouse, self).__init__()
        self.delay = delay
        self.button = button
        self.running = True
        self.start()

    def run(self):
        while self.running:
            if clicking:
                mouse.click(self.button)
            time.sleep(self.delay)

    def stop(self):
        self.running = False

def on_press(key):
    global clicking
    if key == TOGGLE_KEY:
        clicking = not clicking
        if clicking:
            print("Autoclicker DÉMARRÉ. Appuyez sur 'x' pour quitter.")
        else:
            print("Autoclicker ARRÊTÉ.")
    elif key == EXIT_KEY:

        click_thread.stop()

print(f"Appuyez sur '{TOGGLE_KEY.char}' pour démarrer/arrêter l'autoclicker.")
print(f"Appuyez sur '{EXIT_KEY.char}' pour quitter le programme.")


click_thread = ClickMouse(DELAY, Button.left)


with Listener(on_press=on_press) as listener:
    listener.join()