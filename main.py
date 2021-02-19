#Script maked by Querix <3

import os
import string
import time
from datetime import datetime



now = datetime.now()
currect_timeH = now.strftime("%H")
currect_timeM = now.strftime("%M")
timetoclick = 0
timetoclick2 = 0
timetoclick3 = 0
odp1 = 0
odp2 = 0
odp3 = 0
n = 0

try:
    f= open("sfgamesettings.ini")
except IOError:
    f= open("sfgamesettings.ini","w+")
finally:
    f= open("sfgamesettings.ini", "r")
filetext= f.readline()

if filetext != "installed components":
    print("")
    print("the first run will install the necessary components! if you don't have one, the script will either crash or end with an error after a while, it's best to restart the script after installing the components!")
    print("")
    input("ready to install?(do not type anythink just click enter!):")
    print("")
    os.system("pip install pyautogui")
    f= open("sfgamesettings.ini", "a")
    f.write("installed components")
    f.close()
import pyautogui



print("")
print("Hello! this script is supposed to automatically collect what you point to after some hours / at a given time")
print("Turn on SFgame and hover over the building and click Enter, the script will catch where you clicked, the script will display coordinates to you and you will type them, then the script will know where to click at the given time")
input("ready?(do not type anythink just click enter!):")

def getmousepos():
    mousepos = pyautogui.position()
    print(mousepos)

def main():
    odp1 = "yes"
    odp2 = ""
    odp3 = ""
    x1 = ""
    x2 = ""
    x3 = ""
    getmousepos()
    x1 = input("enter the coordinate x: ")
    y1 = input("enter the coordinate y: ")
    odp1 = input("want to add more points? max 3 points (yes/No): ")
    if odp1 == "yes":
            input("ready?(do not type anythink just click enter!):")
            getmousepos()
            x2 = input("enter the coordinate x: ")
            y2 = input("enter the coordinate y: ")
            odp2 = input("want to add more points? max 3 points (yes/No): ")
            if odp2 == "yes":
                input("ready?(do not type anythink just click enter!):")
                getmousepos()
                x3 = input("enter the coordinate x: ")
                y3 = input("enter the coordinate y: ")
                print("entered max points")
                time.sleep(5)
    timeclickonepointH = int(input("enter the time after which I should click point number 1(hours): "))
    timeclickonepoint1H = timeclickonepointH
    timeclickonepointH += int(currect_timeH)
    timeclickonepointM = int(currect_timeM)
    print("i will click point 1 on: %s" % (timeclickonepointH))
    if odp1 == "yes":
        timeclickonepoint2H = int(input("enter the time after which I should click point number 2(hours): "))
        timeclickonepoint22H = timeclickonepoint2H
        timeclickonepoint2H += int(currect_timeH)
        timeclickonepoint2M = int(currect_timeM)
        print("i will click point 1 on: %s" % (timeclickonepoint2H))
        if odp2 == "yes":
            timeclickonepoint3H = int(input("enter the time after which I should click point number 3(hours): "))
            timeclickonepoint3H += int(currect_timeH)
            timeclickonepoint33H = timeclickonepointH
            timeclickonepoint3M = int(currect_timeM)
            print("i will click point 1 on: %s" % (timeclickonepoint3H))
    while n == 0:
        time.sleep(5)
        if x2 == "":
            print("-------------------")
            print("Currect time: %s" % now)
            timetoclick = int(timeclickonepointH) - int(currect_timeH)
            print("Left time to click point 1: %s hours" % (timetoclick))
            if currect_timeH == timeclickonepointH:
                timeclickonepointH = int(timeclickonepoint1H) + int(currect_timeH)
                pyautogui.click(x1, y1)
                print("clicked")
                print("-------------------")
        if odp1 == "yes" and odp2 == "":
            print("-------------------")
            print("Currect time: %s" % now)
            timetoclick = int(timeclickonepointH) - int(currect_timeH)
            print("Left time to click point 1: %s hours" % (timetoclick))
            timetoclick2 = int(timeclickonepoint2H) - int(currect_timeH)
            print("Left time to click point 2: %s hours" % (timetoclick2))
            if currect_timeH == timeclickonepointH:
                timeclickonepointH = int(timeclickonepoint1H) + int(currect_timeH)
                pyautogui.click(x1, y1)
                print("clicked")
            elif currect_timeH == timeclickonepoint2H:
                timeclickonepoint2H = int(timeclickonepoint22H) + int(currect_timeH)
                pyautogui.click(x2, y2)
                print("clicked")
                print("-------------------")
        if odp2 == "yes":
            print("-------------------")
            print("Currect time: %s" % now)
            timetoclick = int(timeclickonepointH) - int(currect_timeH)
            print("Left time to click point 1: %s hours" % (timetoclick))
            timetoclick2 = int(timeclickonepoint2H) - int(currect_timeH)
            print("Left time to click point 2: %s hours" % (timetoclick2))
            timetoclick3 = int(timeclickonepoint3H) - int(currect_timeH)
            print("Left time to click point 3: %s hours" % (timetoclick3))
            if currect_timeH == timeclickonepointH:
                timeclickonepointH = int(timeclickonepoint1H) + int(currect_timeH)
                pyautogui.click(x1, y1)
                print("clicked")
            elif currect_timeH == timeclickonepoint2H:
                timeclickonepoint2H = int(timeclickonepoint22H) + int(currect_timeH)
                pyautogui.click(x2, y2)
                print("clicked")
            elif currect_timeH == timeclickonepoint3H:
                timeclickonepoint3H = int(timeclickonepoint33H) + int(currect_timeH)
                pyautogui.click(x3, y3)
                print("clicked")
                print("-------------------")

main()
