import json

from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
from uuid import uuid4

from conf_sync.config_updater import update_configuration
from settings import iot_endpoint, configuration_topic

client_id = str(uuid4())

# Create an IoT client
client = AWSIoTMQTTClient(client_id)
client.configureEndpoint(iot_endpoint, 8883)
client.configureCredentials('conf_sync/certs/AmazonRootCA1.pem', 'conf_sync/certs/private.pem.key',
                            'conf_sync/certs/certificate.pem.crt')

# Connect to AWS IoT
client.connect()


def message_handler(_1, _2, msg):
    msg = json.loads(msg.payload)
    update_configuration(msg)


def config_change_listener():
    client.subscribe(configuration_topic, 1, message_handler)
    try:
        while True:
            pass

    except KeyboardInterrupt:
        client.disconnect()
