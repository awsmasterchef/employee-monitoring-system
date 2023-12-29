import ctypes
import json
import os
import time

from local_comm.pub_sub import PubSub
from log_manager import log_info_msg


class LASTINPUTINFO(ctypes.Structure):
    _fields_ = [("cbSize", ctypes.c_uint), ("dwTime", ctypes.c_ulong)]


def get_last_input_time():
    lii = LASTINPUTINFO()
    lii.cbSize = ctypes.sizeof(LASTINPUTINFO)

    ctypes.windll.user32.GetLastInputInfo(ctypes.byref(lii))

    millis = ctypes.windll.kernel32.GetTickCount() - lii.dwTime
    return millis / 1000.0  # Convert to seconds


def detect_inactivity_worker(service_bus):
    log_info_msg("detect_inactivity_worker started")
    alert_send = False
    while True:
        with open(f"{os.getcwd()}/config.json", "r") as file:
            data = json.load(file)
        inactivity_threshold = data["inactivity_threshold"]
        inactivity_check_frequency = data["inactivity_check_frequency"]
        inactive_time = get_last_input_time()
        if inactive_time > inactivity_threshold and not alert_send:
            alert_send = True
            PubSub.publish({"device_inactivity": True})
            log_info_msg("Alert send true")
        if inactive_time < inactivity_threshold and alert_send:
            alert_send = False
            PubSub.publish({"device_inactivity": False})
            log_info_msg("Alert send false")
        time.sleep(inactivity_check_frequency)

# if __name__ == "__main__":
#     detect_inactivity_worker('')
