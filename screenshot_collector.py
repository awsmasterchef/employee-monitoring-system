import io
import json
import time
from datetime import datetime
from PIL import Image
from PIL import ImageGrab
import os


def screenshot_collector_worker():
    print(f"screen_shot_collector_worker started")
    while True:
        take_screenshot_and_save(f"{os.getcwd()}\screenshots")
        with open(f"{os.getcwd()}/config.json", "r") as file:
            data = json.load(file)
        time.sleep(data["screenshot_interval"])


# def take_screenshot_and_save(directory):
#     os.makedirs(directory, exist_ok=True)
#     screenshot = ImageGrab.grab()
#
#     current_timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
#     file_path = os.path.join(directory, f"screenshot_{current_timestamp}.png")
#     screenshot.save(file_path)
#     print(f"Screenshot saved to: {file_path}")

def take_screenshot_and_save(directory):
    os.makedirs(directory, exist_ok=True)
    screenshot = ImageGrab.grab()
    binary_stream = io.BytesIO()

    screenshot.save(binary_stream, format='PNG')

    current_timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    file_path = os.path.join(directory, f"screenshot_{current_timestamp}.bin")

    # Save the binary stream to a file
    with open(file_path, 'wb') as file:
        file.write(binary_stream.getvalue())

    print(f"Screenshot saved in binary format to: {file_path}")

def convert_binary_to_png(binary_file_path, output_png_path):
    # Read binary data from the file
    with open(binary_file_path, 'rb') as binary_file:
        binary_data = binary_file.read()

    # Create an in-memory binary stream
    binary_stream = io.BytesIO(binary_data)

    # Open the image using PIL
    image = Image.open(binary_stream)

    # Save the image in PNG format
    image.save(output_png_path, format='PNG')
    print(f"Converted binary to PNG and saved to: {output_png_path}")

# screenshot_collector_worker()

convert_binary_to_png('D:\project\monitoring\screenshots/screenshot_2023-12-17_16-48-27.bin','test.png')