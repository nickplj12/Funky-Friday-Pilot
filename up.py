import pyautogui
import pydirectinput
from ahk import AHK
from ahk.directives import NoTrayIcon
import time

ahk = AHK(directives=[NoTrayIcon]) 

pyautogui.FAILSAFE = True
pydirectinput.FAILSAFE = True

upColor = (18, 250, 5)
upHoldColor = (18, 250, 5, 0.5)

upX = 1024

y = 186

upKey = 'up'

print("Ready! Load a song.")

while True:
	if pyautogui.pixelMatchesColor(upX, y, (upColor), tolerance = 80):
		print("UP")
		ahk.key_press(upKey)
	'''
	elif pyautogui.pixelMatchesColor(upX, y, (upHoldColor), tolerance = 80):
		print("UP HOLD")
		ahk.key_down(upKey)
		time.sleep(10)
		ahk.key_up(upKey)
	'''
		