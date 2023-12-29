import ctypes
import time

from helper import read_config_file
from local_comm.subscriber import Subscriber
from log_manager import log_info_msg


def is_screen_locked_windows():
    user32 = ctypes.windll.User32
    return user32.GetForegroundWindow() == 0


def screen_lock_check_worker(service_bus):
    log_info_msg(f"screen_lock_check_worker started")
    subscriber = Subscriber("Screen Lock Checker Worker Subscriber")
    process_run = False
    process_kill = True
    while True and process_kill:
        msg = subscriber.get()
        if msg:
            log_info_msg("get message in screen lock thread" + str(msg) + str(type(msg)))
            device_inactivity = msg.get('device_inactivity', False)
            process_run = True if device_inactivity else False
        if process_run:
            result = is_screen_locked_windows()
            if result:
                log_info_msg("result is True")
                process_kill = False
            else:
                log_info_msg("result is False")
            time.sleep(read_config_file('screen_lock_check_frequency'))
