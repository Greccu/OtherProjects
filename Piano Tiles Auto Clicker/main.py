import numpy
from PIL import ImageGrab
import cv2
import time
from pynput.mouse import Button, Controller
import keyboard

mouse = Controller()
gameCoords = [670, 50, 1260, 1040]
#ImageGrab.grab(bbox=gameCoords).show()
screen = numpy.array(ImageGrab.grab(bbox=gameCoords))
screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)  # 730,880,1030,1200
columns = [60, 210, 340, 530]
#columns = [730,880,1030,1200]
#
while True:
    if keyboard.is_pressed('q'):
        break
    else:
        screen = numpy.array(ImageGrab.grab(bbox=gameCoords))
        screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
        for y in range(50,len(screen),30):
            for x in columns:
                if screen[y][x] < 40 and mouse.position[0] != x+gameCoords[0]:
                    mouse.position = (x+gameCoords[0], y+gameCoords[1])
                    mouse.press(Button.left)
                    mouse.release(Button.left)
