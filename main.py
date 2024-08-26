import time, pyautogui, pytesseract

def useItem(itemName):
    pyautogui.leftClick(menuCoords)
    time.sleep(0.5)
    pyautogui.leftClick(searchbarCoords)
    time.sleep(0.5)
    pyautogui.typewrite(itemName)
    time.sleep(0.5)
    pyautogui.press('enter')
    time.sleep(0.5)
    pyautogui.leftClick(firstItemCoords)

def teleportSpawn():
    pyautogui.leftClick(teleporterCoords)

def teleportBestArea():
    return

def locationInit():
    with open("config.txt", "w") as conf:
        menuCoords = pyautogui.locateOnScreen("./images/menu.png", grayscale=True)
        if menuCoords is not None: 
            conf.write(str(menuCoords))  # Convert the coordinates to a string
        else:
            conf.write("no coords found")

time.sleep(2)
locationInit()