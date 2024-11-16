from time import sleep
from threading import Thread
import pyautogui as pag
import keyboard

def clamp(value, min_value, max_value):
    return max(min_value, min(value, max_value))

try:
    clicksPerSecond = int(input('How many clicks per second? (Min = 1, Max = 1000, default = 100): ') or 100)
    clicksPerSecond = clamp(clicksPerSecond, 1, 1000)
except ValueError:
    clicksPerSecond = 100

print('Alt + F1 to activate, Alt + F2 to deactivate')

activated = False

def hotkey(key1, key2):
    return keyboard.is_pressed(key1) and keyboard.is_pressed(key2)

while True:
    if hotkey('alt', 'f1'): 
        activated = True
    elif hotkey('alt', 'f2'):
        activated = False
    
    if activated:
        Thread(target = pag.click).start()
        sleep(1 / clicksPerSecond)