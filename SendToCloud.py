'''
Created on Apr 11, 2018
@author: andrewstito
'''

import ibmiotf
import ibmiotf.device
import paho.mqtt.client as mqtt
import json


'''
IBM Bluemix cloud connection details
'''
organization = "ioc4us"
deviceType   = "MotionSensor"
deviceId     = "MS111"
authMethod   = "token"
authToken    = "jp)TxfqRzcm7wDm-+B"



# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("OK. Connected with result code "+str(rc))
    client.subscribe("Bluemix")


# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print("OK. New data received ")
    try:
        cloudclient.publishEvent("Presence data", "json" , str(msg.payload))
        print("OK. Data sent to Cloud")
    except Exception:
        print("NOK. Data not sent to Cloud")


        
deviceOptions = {"org": organization, "type": deviceType, "id": deviceId, "auth-method": authMethod, "auth-token": authToken}
cloudClient = ibmiotf.device.HttpClient(deviceOptions)    
cloudClient.connect()

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("iot.eclipse.org", 1883, 60)

client.loop_forever()

client.disconnect()
