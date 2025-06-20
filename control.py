from pynput.mouse import Controller
from pynput.keyboard import Controller
#controlling your mouse
#mouse will move left to right to top to bootm 
def controlmouse():
    mouse=Controller()
    mouse.position=(200,200)
controlmouse()
#listening to your mouse
def controlkeyboard():
    keyboard=Controller()
    keyboard.type=("helloasdasdasdasd world")
controlkeyboard()
#controlling your keyboard 
#listening to your keyboard(used in key logger) 