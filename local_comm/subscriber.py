import queue

from local_comm.pub_sub import PubSub


class Subscriber:
    def __init__(self, name):
        self.name = name
        self.queue = queue.Queue()
        PubSub.add_subscriber(self)

    def notify(self, message):
        print(f"{self.name} received: {message}")
        self.queue.put(message)

    def get(self, timeout=1):
        msg = None
        try:
            msg = self.queue.get(timeout=timeout)
        except queue.Empty:
            pass
        return msg
