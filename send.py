import pika,json

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='test')
data=json.dumps({"message":"hello world","status":True})
channel.basic_publish(exchange='',
                      routing_key='test',
                      body=data)
print(" [x] Sent %s" % data)
connection.close()
