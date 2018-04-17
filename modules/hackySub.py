
'''
/*
 * Copyright 2010-2017 Amazon.com, Inc. or its affiliates. All Rights Reserved.
 *
 * Licensed under the Apache License, Version 2.0 (the "License").
 * You may not use this file except in compliance with the License.
 * A copy of the License is located at
 *
 *  http://aws.amazon.com/apache2.0
 *
 * or in the "license" file accompanying this file. This file is distributed
 * on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either
 * express or implied. See the License for the specific language governing
 * permissions and limitations under the License.
 */
 '''

from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
import logging
import time

class IotSubscribe:

    def __init__(self, topic=None, message="Can you see me"):
        self.host = 'a3u5wn9s3a3oaw.iot.eu-west-2.amazonaws.com'
        self.certificatePath = 'modules/certs/13f1341faa-private.pem.crt'
        self.privateKeyPath = 'modules/certs/13f1341faa-private.pem.key'
        self.rootCAPath = 'modules/certs/rootCA.pem'
        self.topic = 'lcd/data'
        self.port = 8883
        #self.clientId = "basicPubSub"
        self.clientId = "a2138789127398"

    def Dmain(self):
        # Custom MQTT message callback
        def customCallback(client, userdata, message):
            print("Received a new message: ")
            print(message.payload)
            print("from topic: ")
            print(message.topic)
            print("--------------\n\n")

        # Init AWSIoTMQTTClient
        myAWSIoTMQTTClient = None
        myAWSIoTMQTTClient = AWSIoTMQTTClient(self.clientId)
        myAWSIoTMQTTClient.configureEndpoint(self.host, 8883)
        myAWSIoTMQTTClient.configureCredentials(self.rootCAPath, self.privateKeyPath, self.certificatePath)

        # AWSIoTMQTTClient connection configuration
        myAWSIoTMQTTClient.configureAutoReconnectBackoffTime(1, 32, 20)
        myAWSIoTMQTTClient.configureOfflinePublishQueueing(-1)  # Infinite offline Publish queueing
        myAWSIoTMQTTClient.configureDrainingFrequency(2)  # Draining: 2 Hz
        myAWSIoTMQTTClient.configureConnectDisconnectTimeout(10)  # 10 sec
        myAWSIoTMQTTClient.configureMQTTOperationTimeout(5)  # 5 sec

        # Connect and subscribe to AWS IoT
        while True:
            myAWSIoTMQTTClient.connect()
            myAWSIoTMQTTClient.subscribe(self.topic, 1, customCallback)
            time.sleep(2)


if __name__ == "__main__":

    instance = IotSubscribe()
    instance.Dmain()
