import paho.mqtt.publish as publish

data_topic = "paradise/presence/data"
notify_topic = "paradise/notify/presence"

def send_presence_event(presence_event):
	data = str(presence_event)

	publish.single(data_topic, data, port=8883, tls={'ca_certs':"ca.crt",'tls_version':2}, hostname="nyx.bjornhaug.net")
	publish.single(notify_topic, data, port=8883, tls={'ca_certs':"ca.crt",'tls_version':2}, hostname="nyx.bjornhaug.net")