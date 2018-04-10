from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
from random import randrange
import json

class IoT:

    def __init__(self, serialnumber, topic=None, message="Can you see me"):
        self.host = 'a3u5wn9s3a3oaw.iot.eu-west-2.amazonaws.com'
        self.certificatePath = '13f1341faa-private.pem.crt'
        self.privateKeyPath = '13f1341faa-private.pem.key'
        self.rootCAPath = 'rootCA.crt'
        self.topic = 'lcd/data'
        self.port = 8883
        self.client = self.client_connect(serialnumber)
        self.message = message
        self.serialnumber = serialnumber


    def client_connect(self, serialnumber):

        myMQTTClient = AWSIoTMQTTClient(serialnumber)        
        myMQTTClient.configureEndpoint(self.host, self.port)
        myMQTTClient.configureCredentials(self.rootCAPath, self.privateKeyPath, self.certificatePath)
        return(myMQTTClient)

    def connect(self):

        self.client.connect()
        message = {}
        message['message'] = self.message
        message['sequence'] = randrange(0, 10) 
        messageJson = json.dumps(message)

        self.client.publish(self.topic, self.message, 0)
        self.client.disconnect()
        print('Published topic %s: %s\n' % (self.topic, messageJson))
        print(self.serialnumber)

if __name__ == "__main__":

    instance = IoT(serialnumber='a2138789127398', message = 'something else')
    instance.connect()
