from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient

# For certificate based connection
myMQTTClient = AWSIoTMQTTClient("oli")

# For Websocket connection
# myMQTTClient = AWSIoTMQTTClient("myClientID", useWebsocket=True)
# Configurations
# For TLS mutual authentication
myMQTTClient.configureEndpoint("a3u5wn9s3a3oaw.iot.eu-west-2.amazonaws.com", 8883)
# For Websocket
# myMQTTClient.configureEndpoint("YOUR.ENDPOINT", 443)
myMQTTClient.configureCredentials("symantec.pem", "13f1341faa-private.pem.key", "13f1341faa-private.pem.crt")

myMQTTClient.connect()
myMQTTClient.publish("foobar", "hi", 0)
myMQTTClient.disconnect()
