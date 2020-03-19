import paho.mqtt.client as mqtt
import json

#Group Integration Common Variable
motionValue = 0
lumenValue = 1


# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):

    print("Connected with result code "+str(rc))

    client.subscribe("ACT")
    client.subscribe("Trigger")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):

    global motionValue 
    global lumenValue 

    if(msg.topic == "ACT"):
        jsonToDic = json.loads(msg.payload)
        lumenValue = jsonToDic['SensorData']
        print("Lumen value from (SLS): " + str(lumenValue))  
    elif(msg.topic == "Trigger") :
        jsonToDic = json.loads(msg.payload)
        motionValue = jsonToDic['SensorData']
        print("Presence data from (SHoLS):  " + str(motionValue))
    else:
        print("NOK. Incorrect data")            
    groupIntegration()
    

def groupIntegration():

    global motionValue 
    global lumenValue 

    if(lumenValue < 3):
        if(motionValue == 0):
            print("Turn OFF the light")
        else:
            print("Turn ON the light")
            
    elif(lumenValue > 3):
        if(motionValue == 0):
            print("Turn OFF the light")
        else:
            print("Turn ON the light")
                

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("iot.eclipse.org", 1883, 60)
client.loop_forever()
client.disconnect()