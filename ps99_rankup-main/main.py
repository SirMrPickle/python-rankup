import pyautogui
import json
import pytesseract
from PIL import ImageGrab
import time

def load_coordinates(config_file):
    with open(config_file, 'r') as f:
        coords = json.load(f)
    return coords

def click_location(location):
    """
    Click at the specified screen coordinates.
    """
    pyautogui.click(location)
    print(f"Clicked at {location}")

def use_item(coords, item_name):
    """
    Simulate the action of using an item by clicking its location.
    """
    if item_name in coords:
        location = coords[item_name]
        if location != "not found":
            click_location(location)
        else:
            print(f"{item_name} coordinates not found in config.")
    else:
        print(f"{item_name} not in config.")

def teleport_to_location(coords, location_name):
    """
    Teleport to a specific location.
    """
    use_item(coords, location_name)

def read_text_from_screen(region):
    """
    Use OCR to read text from a specific screen region.
    """
    screenshot = ImageGrab.grab(bbox=region)
    text = pytesseract.image_to_string(screenshot)
    return text

def perform_quest_action(coords):
    """
    Perform actions based on quest text read from the screen.
    """
    # Example region for quest area (adjust as needed)
    quest_region = (100, 100, 500, 300)  # Example coordinates for the quest area
    quest_text = read_text_from_screen(quest_region)
    print("Quest Text:", quest_text)

    if "break" in quest_text:
        # Example action based on quest text
        use_item(coords, "coin_jar")  # Replace with actual item name

def main():
    config_file = "config.json"
    coords = load_coordinates(config_file)
    
    # Example usage
    teleport_to_location(coords, "teleport_spawn")
    time.sleep(2)  # Wait for 2 seconds
    teleport_to_location(coords, "teleport_best_area")
    time.sleep(2)  # Wait for 2 seconds
    
    # Perform quest action
    perform_quest_action(coords)

if __name__ == "__main__":
    main()
