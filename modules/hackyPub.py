from hackyAuth import IoTAuth
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
from random import randrange
import json

class IoTPublish():

    def __init__(self, serialnumber, topic, message):
        self.topic = topic
        self.client = IoTAuth().client_connect(self)
        self.message = message
        self.serialnumber = serialnumber

    def connect(self):

        self.client.connect()
        message = {}
        message['message'] = self.message
        message['sequence'] = 1 
        messageJson = json.dumps(message)

        self.client.publish(self.topic, self.message, 0)
        self.client.disconnect()
        print('Published topic %s: %s\n' % (self.topic, messageJson))
        print(self.serialnumber)
