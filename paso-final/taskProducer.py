import pika
import random

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declarar la cola
channel.queue_declare(queue='task_queue', durable=True)

# Enviar varias tareas
for i in range(10):
    message = f"Realiza la operación correspondiente a estos dos numeros {random.randint(0,9)} y {random.randint(0,9)}"
    channel.basic_publish(exchange='',
                        routing_key='task_queue',
                        body=message,
                        properties=pika.BasicProperties(
                            delivery_mode=2,  # Hacer el mensaje persistente
                        ))
    print(" [x] Sent %r" % message)

connection.close()
