import pyautogui
from PIL import ImageGrab
import time
from colorama import *

# Ścieżka do obrazka, którego szukasz
path_to_map_image = 'CaptureMap/Map.png'
path_to_nexus_image = 'CaptureMap/Nexus.png'
deaths = 'DeathsLimiter/Death.png'
max_deaths = 'DeathsLimiter/MaxDeaths.png'

nexus_position = []

def MapPosition():
    while True:
        print("Searching for Map on screen...")
        found_map = pyautogui.locateOnScreen(path_to_map_image, confidence=0.3)
        time.sleep(0.8)
        if found_map:
            left, top, width, height = found_map
            right = left + width
            bottom = top + height

            screenshot = ImageGrab.grab(bbox=(left, top, right, bottom))

            print(Fore.GREEN +"Map Found" + Style.RESET_ALL)
            
            screenshot.save("Captured/captured_map.png")
            print("Map saved as captured_map.png")
            
            return found_map  # Zwróć znalezioną mapę

def EnemyNexusPos(found_map):
    while True:
        print("Searching for nexus...")
        found_nexus = pyautogui.locateOnScreen(path_to_nexus_image, confidence=0.3, region=found_map)

        if found_nexus:
            # Jeśli obrazek nexusa zostanie znaleziony
            left_n, top_n, width_n, height_n = found_nexus
            right_n = left_n + width_n
            bottom_n = top_n + height_n
            
            center_x = (left_n + right_n) // 2
            center_y = (top_n + bottom_n) // 2

            print(f"Nexus center: ({center_x}, {center_y})")

            time.sleep(0.8)
            nexus_position.append((center_x, center_y))
            break
        else:
            print("Couldnt find nexus")
            time.sleep(0.8)

def DeathsDetector():
    detect_deaths = pyautogui.locateAllOnScreen(deaths, confidence=0.5)
    print(detect_deaths)
    
    
found_map = MapPosition()
EnemyNexusPos(found_map)
while True:
    DeathsDetector()
    break


for i in range(15):
    pyautogui.moveTo(x=1901, y=847)
    pyautogui.click(x=1901, y=847, button='right') 
    print("Running it down...")
    time.sleep(25)
