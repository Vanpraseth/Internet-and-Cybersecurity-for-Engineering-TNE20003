import paho.mqtt.client as mqtt

broker = "rule28.i4t.swin.edu.au"
username = "<104482107>"
password = "<104482107>"
port = 1883
public_topic = "public/#"
private_topic = f"{username}/temperature"

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("The Device 2 connected successfully")
        client.subscribe(public_topic)
        client.subscribe(private_topic)
    else:
        print(f"The Device 2 failed to connect, return code {rc}")

def on_message(client, userdata, msg):
    print(f"The Device 2 received a message: {msg.topic} - {msg.payload.decode()}")

client = mqtt.Client(client_id="Device2")
client.username_pw_set(username, password)
client.on_connect = on_connect
client.on_message = on_message

client.connect(broker, port, 60)

client.loop_forever()