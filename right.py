import pyautogui
import pydirectinput
from ahk import AHK
from ahk.directives import NoTrayIcon
import time

ahk = AHK(directives=[NoTrayIcon]) 

pyautogui.FAILSAFE = True
pydirectinput.FAILSAFE = True

rightColor = (249, 57, 63)
rightHoldColor = (249, 57, 63, 0.5)

rightX = 1177

y = 186

rightKey = 'right'

print("Ready! Load a song.")

while True:
	if pyautogui.pixelMatchesColor(rightX, y, (rightColor), tolerance = 80):
		print("RIGHT")
		ahk.key_press(rightKey)
	'''
	elif pyautogui.pixelMatchesColor(rightX, y, (rightHoldColor), tolerance = 80):
		print("RIGHT HOLD")
		ahk.key_down(rightKey)
		time.sleep(10)
		ahk.key_up(rightKey)
	'''
		