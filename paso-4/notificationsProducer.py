import pika

def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='notifications')

    for i in range(10):
        message = f"Notification {i}"
        channel.basic_publish(exchange='',
                              routing_key='notifications',
                              body=message)
        print(f" [x] Sent '{message}'")
    connection.close()

if __name__ == '__main__':
    main()