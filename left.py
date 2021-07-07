import pyautogui
import pydirectinput
from ahk import AHK
from ahk.directives import NoTrayIcon
import time

ahk = AHK(directives=[NoTrayIcon]) 

pyautogui.FAILSAFE = True
pydirectinput.FAILSAFE = True

leftColor = (194, 75, 153)
leftHoldColor = (194, 75, 153, 0.5)

leftX = 731

y = 186

leftKey = 'left'

print("Ready! Load a song.")

while True:
	if pyautogui.pixelMatchesColor(leftX, y, (leftColor), tolerance = 80): #i also made the tolerance at 80 at one point
		print("LEFT")
		ahk.key_press(leftKey)
	'''
	elif pyautogui.pixelMatchesColor(leftX, y, (leftHoldColor), tolerance = 80): 
		print("LEFT HOLD")
		ahk.key_down(leftKey)
		time.sleep(10)
		ahk.key_up(leftKey)
	'''
		