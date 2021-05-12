import pika
import json

params = pika.ConnectionParameters(host='my-rabbit')

connection = pika.BlockingConnection(params)

channel = connection.channel()
channel.queue_declare('main_queue')

def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(
        exchange='',
        routing_key='main_queue',
        body=json.dumps(body),
        properties=properties
    )
