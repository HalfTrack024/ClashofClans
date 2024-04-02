from pynput.mouse import Controller as mController, Button
from pynput.keyboard import Controller as kController, Key
from time import sleep
from screeninfo import get_monitors
import random
import math
import pygetwindow as gw

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
    val = 1 + randomizer(.25, 3)
    sleep(val)

def attack():
    #Attach Button
    mouseCMD(5, 88, 3, 3)
    #Find Button
    mouseCMD(74, 64, 3, 3)
    sleep(3)
    #Troop 1
    kGUI.press('q')
    kGUI.release('q')
    mouseCMD(95, 42, 2, 15)
    #Troop 2
    kGUI.press('1')
    kGUI.release('1')
    mouseCMD(95, 42, 2, 15)
    #Troop 3
    kGUI.press('2')
    kGUI.release('2')
    mouseCMD(95, 42, 2, 15)
    #Troop 4
    kGUI.press('3')
    kGUI.release('3')
    mouseCMD(95, 42, 2, 15)
    #Troop 5
    mouseCMD(95, 42, 2, 15)
    sleep(1)


def collect():
    launch()
    mouseCMD(69, 0.1, 0, 0)
    mouseCMD(75, 82, 2,2)
    mouseCMD(5, 88, 3, 3)
    close()

def launch():
    mouseCMD(20, 58, 3,3)
    sleep(10)


def close():
    act_W = gw.getActiveWindow().title
    if act_W == "Clash of Clans":
        with kGUI.pressed(Key.alt):
            kGUI.press(Key.f4)
    else:
        print('not on write app')
    sleep(1)

def cycleAttack():
    for i in range(2):
        launch()
        attack()
        close()
        print(i)

def main():
    #Start 
    findSize()
    mouseCMD(94, 1, 0,0)
    #mouseCMD(1940, 19)
    for j in range(5):
        cycleAttack()
        collect()
        print(j)


# Run Code
main()
