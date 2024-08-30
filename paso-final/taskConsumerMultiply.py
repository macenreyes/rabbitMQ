import pika
import time
import re

# Conectar a RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declarar la cola 'task_queue'
channel.queue_declare(queue='task_queue', durable=True)

def callback(ch, method, properties, body):
    message = body.decode()
    print(f" [x] Received {message}")
    print("Getting multiply operation")
    numbers = re.findall(r'\d+', message)
    numbers = [int(number) for number in numbers]
    result = 1
    for number in numbers:
        result *= number
    time.sleep(5)  # Simula que se está procesando la tarea
    print(f" [x] Task done. Result gotten: {result}")
    ch.basic_ack(delivery_tag=method.delivery_tag)

# Configurar la cola para que entregue un mensaje a la vez
channel.basic_qos(prefetch_count=1)

# Configurar el consumidor para recibir mensajes de la cola
channel.basic_consume(queue='task_queue', on_message_callback=callback)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
