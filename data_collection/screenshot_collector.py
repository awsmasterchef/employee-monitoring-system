import io
import os
import time
from datetime import datetime
from queue import Empty

from PIL import ImageGrab

from helper import read_config_file
from local_comm.subscriber import Subscriber
from log_manager import log_info_msg


def screenshot_collector_worker(service_bus):
    subscriber = Subscriber("screenshot Collector Worker Subscriber")
    log_info_msg(f"screen_shot_collector_worker started")
    process_run = True
    while True:
        msg = subscriber.get()
        if msg:
            log_info_msg("get message" + str(msg) + str(type(msg)))
            device_inactivity = msg.get('device_inactivity', None)
            process_run = False if device_inactivity else True
        if process_run:
            log_info_msg("process Running")
            take_screenshot_and_save("data_store")
        else:
            log_info_msg("process stopped")
        time.sleep(read_config_file("screenshot_interval"))


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

    log_info_msg(f"Screenshot saved in binary format to: {file_path}")

# def convert_binary_to_png(binary_file_path, output_png_path):
#     # Read binary data from the file
#     with open(binary_file_path, 'rb') as binary_file:
#         binary_data = binary_file.read()
#
#     # Create an in-memory binary stream
#     binary_stream = io.BytesIO(binary_data)
#
#     # Open the image using PIL
#     image = Image.open(binary_stream)
#
#     # Save the image in PNG format
#     image.save(output_png_path, format='PNG')
#     print(f"Converted binary to PNG and saved to: {output_png_path}")
