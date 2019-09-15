import paho.mqtt.client as mqtt
import time
broker_url = "192.168.0.1"
broker_port = 1883
user_name = "hackatlon"
password = "!Hackathl0n"


client = mqtt.Client()
client.username_pw_set (user_name, password)

client.connect(broker_url, broker_port)
#client.publish(topic="freq", payload="13", qos=0, retain=False)
#client.publish(topic="move", payload="left", qos=0, retain=False)
#time.sleep(2.5)
client.publish(topic="move", payload="stop", qos=0, retain=False)
#time.sleep(0.2)
#client.publish(topic="move", payload="right", qos=0, retain=False)
#time.sleep(2.2)
#client.publish(topic="move", payload="stop", qos=0, retain=False)
