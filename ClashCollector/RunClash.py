from pynput.mouse import Controller as mController, Button
from pynput.keyboard import Controller as kController, Key
from time import sleep
from screeninfo import get_monitors
import random
import math

kGUI = kController()
mGUI = mController()
height : int = 0
width : int = 0
def findSize():
    for m in get_monitors():
        if m.is_primary:
            global height, width
            height = m.height
            width = m.width
            
def randomizer(value, bound):
    min_value = value - bound
    max_value = value + bound
    min_value = max(0, min(min_value, 100))
    max_value = max(0, min(max_value, 100))

    rand_num = random.uniform(min_value, max_value)

    return rand_num

def mouseCMD(x_scaled, y_scaled, bound_x, bound_y):
    x : int = round(randomizer(x_scaled, bound_x)/100*width)
    y : int = round(randomizer(y_scaled, bound_y)/100*height)
    mGUI.position = (x, y)
    mGUI.click(Button.left)
    val = 1 + randomizer(.5, 3)
    sleep(val)

def attack():
    #Attach Button
    mouseCMD(5, 88, 3, 3)
    #Find Button
    mouseCMD(74, 64, 3, 3)
    sleep(3)
    #Troop 1
    mouseCMD(18, 94, 1, 1)
    mouseCMD(95, 48, 2, 90)
    mouseCMD(95, 48, 2, 90)
    #Troop 2
    mouseCMD(29, 94, 1, 1)
    mouseCMD(95, 48, 2, 90)
    #Troop 3
    mouseCMD(36, 94, 1, 1)
    mouseCMD(95, 48, 2, 80)
    #Troop 4
    #mouseCMD(13, 94, 1, 1)
    mouseCMD(95, 48, 2, 90)
    sleep(1)


def collect():
    pass

def launch():
    mouseCMD(20, 58, 3,3)
    #mGUI.position = (500, 760)
    #mGUI.click(Button.left)
    sleep(randomizer(10, 2))


def close():
    with kGUI.pressed(Key.alt):
        kGUI.press(Key.f4)

def main():
    #Start 
    findSize()
    mouseCMD(94, 1, 0,0)
    #mouseCMD(1940, 19)

    for i in range(12):
        launch()
        attack()
        sleep(1)
        close()
        sleep(1)
        print(i)

# Run Code
main()
