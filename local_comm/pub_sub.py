import threading

class PubSub:
    subscribers = []
    lock = threading.Lock()

    @classmethod
    def unsubscribe(cls,subscriber):
        with cls.lock:
            PubSub.subscribers.remove(subscriber)

    @classmethod
    def publish(cls, message):
        with cls.lock:
            for subscriber in cls.subscribers:
                subscriber.notify(message)

    @classmethod
    def add_subscriber(cls, subscriber):
        with cls.lock:
            cls.subscribers.append(subscriber)
        return subscriber

# instantiate
# pub_sub_obj = PubSub()

# Example usage:
# if __name__ == "__main__":


# subscriber1 = pub_sub_obj.subscriber("Subscriber-1")
# subscriber2 = pub_sub_obj.subscriber("Subscriber-2")
#
# pub_sub_obj.publish("Hello, subscribers!")
