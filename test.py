import time

from local_comm.pub_sub import PubSub


def start_publisher():
    for i in range(0, 1000):
        time.sleep(5)
        PubSub.publish(f"Hello world sent {i}")
        print("Message sent")
