import pyautogui
from pynput import keyboard
import sys
import time

# PYAUTOGUI CONSTANTS
pyautogui.PAUSE = 0.5
pyautogui.FAILSAFE = True

response = pyautogui.confirm("Start Program")
esc_pressed = False


def on_press(key):
    global esc_pressed
    if key == keyboard.Key.esc:
        esc_pressed = True
        if listener:
            listener.stop()


listener = keyboard.Listener(on_press=on_press)
listener.start()

if response == "OK":
    # change this to lower number if images are not being found
    accuracy = 0.7
    time.sleep(3)
    posX = 0
    posY = 0
    while True:
        if not esc_pressed:
            # click on breeding cave
            cave_found = False
            while not cave_found:
                try:
                    x, y = pyautogui.locateCenterOnScreen("cave.png", confidence=accuracy)
                    posX = x
                    posY = y
                    pyautogui.click(x, y+50)
                    cave_found = True

                except:
                    print("Breeding Cave not found")

            # click on retry
            time.sleep(0.2)
            retry_found = False
            while not retry_found:
                try:
                    x, y = pyautogui.locateCenterOnScreen("retry.png", confidence=accuracy)
                    pyautogui.click(x, y)
                    retry_found = True
                except:
                    print("retry button not found")

            # click on breed
            breed_found = False
            while not breed_found:
                try:
                    x, y = pyautogui.locateCenterOnScreen("breed.png", confidence=accuracy)
                    pyautogui.click(x, y)
                    breed_found = True
                except:
                    print("Breed Button not found")

            # click on heart
            time.sleep(7)
            heart_found = False
            while not heart_found:
                try:
                    x, y = pyautogui.locateCenterOnScreen("heart.png", confidence=accuracy)
                    pyautogui.click(x, y)
                    heart_found = True
                except:
                    print("Heart not found")
            # pyautogui.click(posX, posY)

            # click on place in nursery
            place_in_nursery = False
            while not place_in_nursery:
                try:
                    x, y = pyautogui.locateCenterOnScreen("place_in_nursery.png", confidence=accuracy)
                    pyautogui.click(x, y)
                    place_in_nursery = True
                except:
                    print("Place button not found")

            # click on nursery
            nursery_found = False
            while not nursery_found:
                try:
                    x, y = pyautogui.locateCenterOnScreen("nursery.png", confidence=0.4)
                    pyautogui.click(x+50, y)
                    nursery_found = True
                except:
                    print("Nursery not found")

            time.sleep(4)

            # click on plant egg hatch
            egg_found = False
            while not egg_found:
                try:
                    x, y = pyautogui.locateCenterOnScreen("egg.png", confidence=0.6)
                    pyautogui.click(x, y)
                    egg_found = True
                except:
                    print("Egg not found")

            # click on sell
            time.sleep(0.2)
            sell_found = False
            while not sell_found:
                try:
                    x, y = pyautogui.locateCenterOnScreen("sell.png", confidence=accuracy)
                    pyautogui.click(x, y)
                    sell_found = True
                except:
                    print("Sell button not found")

            # click on yes
            time.sleep(0.2)
            yes_found = False
            while not yes_found:
                try:
                    x, y = pyautogui.locateCenterOnScreen("yes.png", confidence=accuracy)
                    pyautogui.click(x, y)
                    yes_found = True
                except:
                    print("Yes button not found")

# termination stuff from here
        else:
            sys.exit()
else:
    print("program stopped")
