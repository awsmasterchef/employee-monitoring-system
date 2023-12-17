import json
import time
from datetime import datetime

from PIL import ImageGrab
import os


def screenshot_collector_worker():
    print(f"screen_shot_collector_worker started")
    while True:
        take_screenshot_and_save(f"{os.getcwd()}\screenshots")
        with open(f"{os.getcwd()}/config.json", "r") as file:
            data = json.load(file)
        time.sleep(data["screenshot_interval"])


def take_screenshot_and_save(directory):
    os.makedirs(directory, exist_ok=True)
    screenshot = ImageGrab.grab()
    current_timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    file_path = os.path.join(directory, f"screenshot_{current_timestamp}.png")
    screenshot.save(file_path)
    print(f"Screenshot saved to: {file_path}")


screenshot_collector_worker()
