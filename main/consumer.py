import pika
import json

from main import db, Product

params = pika.ConnectionParameters(host='my-rabbit')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare('main_queue')

def callback(ch, method, properties, body):
    print(" [x] received message in main ")
    data = json.loads(body)
    print(data)

    if properties.content_type == 'product_created':
        product = Product(id=data['id'], title=data['title'], image=data['image'])
        db.session.add(product)
        db.session.commit()
        print("product created")
    elif properties.content_type == 'product_updated':
        product = Product.query.get(data['id'])
        product.title = data['title']
        product.image = data['image']
        db.session.commit()
        print("product updated")
    elif properties.content_type == 'product_deleted':
        product = Product.query.get(data)
        db.session.delete(product)
        db.session.commit()
        print("product deleted")

channel.basic_consume(
    queue='main_queue',
    on_message_callback=callback,
    auto_ack=True)
print("started consuming in main")
channel.start_consuming()
channel.close()
