import pyautogui
import json
import time
import os

def save_coordinates(image_paths, config_file):
    coords = {}
    for name, path in image_paths.items():
        # Check if image file exists
        if not os.path.isfile(path):
            print(f"Error: File not found: {path}")
            coords[name] = "file not found"
            continue
        
        # Attempt to locate the image on the screen
        print(f"Searching for {name} at path: {path}")
        try:
            location = pyautogui.locateCenterOnScreen(path, confidence=0.7, grayscale = True)
            if location:
                coords[name] = (int(location.x), int(location.y))
                print(f"{name} found at {location}")
            else:
                coords[name] = "not found"
                print(f"{name} not found or could not be located")
        except pyautogui.ImageNotFoundException:
            coords[name] = "image not found exception"
            print(f"Error: Could not locate the image for {name}")
    
    # Save the coordinates to the config file
    with open(config_file, 'w') as f:
        json.dump(coords, f, indent=4)
    print("Coordinates saved to config file.")

def main():
    # Define image paths
    image_paths = {
        "menu": "./images/menu.png",
        "teleporter": "./images/teleporter_alt.png",
        "teleport_spawn": "./images/teleport_spawn.png",
        "teleport_best_area": "./images/teleport_best_area.png"
    }
    config_file = "config.json"
    
    # Wait for a moment to switch to the game screen
    print("Waiting for 2 seconds...")
    time.sleep(2)  
    
    # Save the coordinates
    save_coordinates(image_paths, config_file)

if __name__ == "__main__":
    main()