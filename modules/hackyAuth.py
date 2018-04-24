from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient

class IoTAuth:

    def __init__(self, serialnumber="12343256"):

        self.host = 'a3u5wn9s3a3oaw.iot.eu-west-2.amazonaws.com'
        self.certificatePath = 'modules/certs/13f1341faa-private.pem.crt'
        self.privateKeyPath = 'modules/certs/13f1341faa-private.pem.key'
        self.rootCAPath = 'modules/certs/rootCA.pem'
        self.port = 8883
        self.serialnumber = serialnumber

    def client_connect(self, serialnumber):

        myMQTTClient = AWSIoTMQTTClient(self.serialnumber)        
        myMQTTClient.configureEndpoint(self.host, self.port)
        myMQTTClient.configureCredentials(self.rootCAPath, self.privateKeyPath, self.certificatePath)
        return(myMQTTClient)
