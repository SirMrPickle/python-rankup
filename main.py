import time
import pyautogui
import json

def useItem(itemName):
    coords = loadCoords()
    pyautogui.leftClick(coords['menuCoords'])
    time.sleep(0.5)
    pyautogui.leftClick(coords['searchbarCoords'])
    time.sleep(0.5)
    pyautogui.typewrite(itemName)
    time.sleep(0.5)
    pyautogui.press('enter')
    time.sleep(0.5)
    pyautogui.leftClick(coords['firstItemCoords'])

def teleportSpawn():
    coords = loadCoords()
    pyautogui.leftClick(coords['teleporterCoords'])

def teleportBestArea():
    # Implementation for finding and clicking the best area teleport goes here
    pass

def locationInit():
    coords = {}
    coords['menuCoords'] = locateAndSaveCoords('./images/menu.png')
    coords['searchbarCoords'] = locateAndSaveCoords('./images/searchbar.png')
    coords['firstItemCoords'] = locateAndSaveCoords('./images/first_item.png')
    coords['teleporterCoords'] = locateAndSaveCoords('./images/teleporter.png')
    
    with open("config.json", "w") as conf_file:
        json.dump(coords, conf_file)

def locateAndSaveCoords(image_path):
    coords = pyautogui.locateOnScreen(image_path, grayscale=True)
    if coords is not None:
        return (coords.left, coords.top)  # Save as a tuple
    else:
        return "no coords found"

def loadCoords():
    with open("config.json", "r") as conf_file:
        return json.load(conf_file)

time.sleep(2)
locationInit()