import time

from local_comm.subscriber import Subscriber

new_subs = Subscriber('')

def start_subscriber():
    while True:
        msg = new_subs.get()
        print("Received ", msg)
        time.sleep(2)
