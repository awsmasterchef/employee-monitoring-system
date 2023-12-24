import json
import os

from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
from uuid import uuid4

from helper import read_config_file

iot_endpoint = read_config_file('iot_endpoint')
client_id = str(uuid4())
topic = read_config_file('configuration_topic')

# Create an IoT client
client = AWSIoTMQTTClient(client_id)
client.configureEndpoint(iot_endpoint, 8883)
client.configureCredentials('certs/AmazonRootCA1.pem', 'certs/private.pem.key', 'certs/certificate.pem.crt')

# Connect to AWS IoT
client.connect()


def update_configuration(_1, _2, msg):
    # Read json file
    msg = json.loads(msg.payload)
    print("configuration Update Received", msg)
    with open(f"{os.getcwd()}/config.json", "r") as file:
        data = json.load(file)
    for key, value in msg.items():
        data[key] = value
    # Write json file with updated keys
    with open(f"{os.getcwd()}/config.json", 'w') as file:
        json.dump(data, file, indent=2)


client.subscribe(topic, 1, update_configuration)


def configuration_sync_handler():
    try:
        while True:
            pass

    except KeyboardInterrupt:
        client.disconnect()


configuration_sync_handler()
