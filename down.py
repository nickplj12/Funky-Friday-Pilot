import pyautogui
import pydirectinput
from ahk import AHK
from ahk.directives import NoTrayIcon
import time

ahk = AHK(directives=[NoTrayIcon]) 

pyautogui.FAILSAFE = True
pydirectinput.FAILSAFE = True

downColor = (0, 255, 255)
downHoldColor = (0, 255, 255, 0.5)

downX = 888

y = 186

downKey = 'down'

print("Ready! Load a song.")

while True:
	if pyautogui.pixelMatchesColor(downX, y, (downColor), tolerance = 80):
		print("DOWN")
		ahk.key_press(downKey)
	'''
	elif pyautogui.pixelMatchesColor(downX, y, (downHoldColor), tolerance = 80): 
		print("DOWN HOLD")
		ahk.key_down(downKey)
		time.sleep(10)
		ahk.key_up(downKey)
	'''
		