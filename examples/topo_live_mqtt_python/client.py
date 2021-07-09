#!/usr/bin/env python3

import os
import json
import time
import paho.mqtt.client as mqtt

MQTT_SERVER = os.environ.get("MQTT_SERVER", "mqtt.topo-web.com")
MQTT_PORT = os.environ.get("MQTT_PORT", "8883")
MQTT_USERNAME = os.environ.get("MQTT_USERNAME", "YOUR_USERNAME_OR_MAIL")
MQTT_PASSWORD = os.environ.get("MQTT_PASSWORD", "YOUR_PASSWORD")

def on_connect(client, userdata, flags, result_code):
    print(f"connected to mqtt broker (result code: {result_code})")
    mqtt_client.subscribe("#")

def on_disconnect(client, userdata, result_code):
    print("disconnected from mqtt with result code:" + str(result_code), "userdata:", userdata)

    # endless reconnect
    while True:
        time.sleep(3)
        try:
            print("reconnecting ...")
            mqtt_client.reconnect()
            break
        except Exception as ex:
            print("reconnect ex: %s", ex)

def on_message(client, userdata, message):
    print("message:", message.topic, message.payload)
    #print("json:", json.dumps(message.payload))

mqtt_client = mqtt.Client("topo-live-example", clean_session=True)
mqtt_client.enable_logger()
mqtt_client.on_connect = on_connect
mqtt_client.on_disconnect = on_disconnect
mqtt_client.on_message = on_message
mqtt_client.username_pw_set(username=MQTT_USERNAME, password=MQTT_PASSWORD)
mqtt_client.tls_set()
mqtt_client.reconnect_delay_set(min_delay=1, max_delay=120)
mqtt_client.connect_async(MQTT_SERVER, int(MQTT_PORT), keepalive=60)

print("Running MQTT loop")
mqtt_client.loop_forever(retry_first_connection=True)

# async:
# mqtt_client.loop_start()
# while True:
#     time.sleep(10)

