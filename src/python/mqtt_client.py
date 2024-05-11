import paho.mqtt.client as mqtt
import argparse


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected successfully.")
        client.subscribe(userdata['topic'])
    else:
        print("Connection failed with code", rc)


def on_message(client, userdata, msg):
    print(f"Received message: {msg.payload.decode()} on topic {msg.topic}")


def parse_args():
    parser = argparse.ArgumentParser(description="MQTT Client Script")
    parser.add_argument("--broker", required=True, help="MQTT broker address")
    parser.add_argument("--port", type=int, default=1883, help="MQTT broker port (default: 1883)")
    parser.add_argument("--topic", required=True, help="Topic to subscribe")
    parser.add_argument("--username", help="Username for MQTT broker", default=None)
    parser.add_argument("--password", help="Password for MQTT broker", default=None)
    return parser.parse_args()


def main():
    args = parse_args()

    client = mqtt.Client()
    client.user_data_set({'topic': args.topic})
    if args.username and args.password:
        client.username_pw_set(args.username, args.password)

    client.on_connect = on_connect
    client.on_message = on_message

    try:
        client.connect(args.broker, args.port, 60)
        client.loop_forever()
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
