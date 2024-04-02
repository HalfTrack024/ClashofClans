from pynput.mouse import Listener
import logging
import pygetwindow as gw

logging.basicConfig(filename="mouse_log.txt", level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_move(x, y):
    pass
    #logging.info("Mouse moved to ({0}, {1})".format(x, y))

def on_click(x, y, button, pressed):
    if pressed:
        act_W = gw.getActiveWindow()
        logging.info('Mouse clicked at ({0}, {1}) with {2} on {3}'.format(x, y, button, act_W.title))

def on_scroll(x, y, dx, dy):
    pass
    #logging.info('Mouse scrolled at ({0}, {1})({2}, {3})'.format(x, y, dx, dy))

with Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll) as listener:
    listener.join()
