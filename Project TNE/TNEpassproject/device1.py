import paho.mqtt.client as mqtt
import time
import random

broker = "rule28.i4t.swin.edu.au"
username = "<104482107>"
password = "<104482107>"
port = 1883
private_topic = f"{username}/temperature"

client = mqtt.Client(client_id="Device1")
client.username_pw_set(username, password)
client.connect(broker, port, 60)

client.loop_start()

try:
    while True:
        temperature = random.uniform(15, 35)
        format_temperature = f"{temperature:.2f}"
        client.publish(private_topic, f"Temperature: {format_temperature} °C")
        print(f"Published: Forecast Temperature: {format_temperature} °C to topic: {private_topic}")
        time.sleep(5)
finally:
    client.loop_stop()
    client.disconnect()