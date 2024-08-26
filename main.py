import time, pyautogui

def useItem(itemName):
    return itemName

def teleportSpawn():
    return

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