import pika

params = pika.ConnectionParameters(host='my-rabbit')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare('admin_queue')

def callback(ch, method, properties, body):
    print(" [x] received in admin %r" % body)

channel.basic_consume(queue='admin_queue', on_message_callback=callback, auto_ack=True)
print("started consuming")
channel.start_consuming()
channel.close()
