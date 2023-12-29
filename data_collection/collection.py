import queue
import threading

from data_collection.inactivity_time import detect_inactivity_worker
from data_collection.screen_lock_check import screen_lock_check_worker
from data_collection.screenshot_collector import screenshot_collector_worker
from log_manager import log_info_msg


def data_collection_process():
    log_info_msg("collection process started")
    # service_bus = queue.Queue()

    threads = []

    thread1 = threading.Thread(target=screenshot_collector_worker, args=('service_bus',))
    threads.append(thread1)

    thread2 = threading.Thread(target=detect_inactivity_worker, args=('service_bus',))
    threads.append(thread2)

    thread3 = threading.Thread(target=screen_lock_check_worker, args=('service_bus',))
    threads.append(thread3)

    thread1.start()
    thread2.start()
    thread3.start()

    # Wait for all threads to finish
    for thread in threads:
        thread.join()
