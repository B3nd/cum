from pyautogui import click, position
from time import sleep

print('waiting')
sleep(1)

print('started')

while 1:
    pos_x , pos_y = position()
    click(x = pos_x, y = pos_y - 10)
    sleep(1)
