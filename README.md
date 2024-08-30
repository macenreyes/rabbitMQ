# RabbitMQ

Para el ejemplo de Rabbit MQ en el folder paso-final tenemos en cuenta que se crearon un productor y dos consumidores que se explican a continuación:

    #taskProducer.py:
        Inmediatamente después de crear la conexión al servidor de RabbitMQ, se declara la cola 'task_queue', con la opción durable=True, que asegura que la cola sobreviva a reinicios del servidor de RabbitMQ.

        Durante el envío de mensajes, se declara la propiedad 'delivery_mode=2' para que el envío de mensajes sea persistente, se almacene en el disco evitando perdida de información en caso de fallos en el servidor.

    #taskConsumer[Operation].py:
        de igual manera que en el productor, se crearon dos consumidores que declaran la cola 'task_queue', asegurando que reciban la mensajería enviada por taskProducer.

        Se maneja posteriormente la función Callback para que cada que reciba un mensaje realice la operación correspondiente a cada consumidor.
        
        La propiedad body.decode() convierte el mensaje en una cadena de texto
        Una vez obtenida la cadena de texto, se obtienen valores numéricos del mensaje y se operan según el consumidor que opere.
        ch.basic_ack(delivery_tag=method.delivery_tag) envía una confirmación de que el mensaje ha sido procesado correctamente. Esto permite que RabbitMQ elimine el mensaje de la cola.

        channel.basic_qos(prefetch_count=1) asegura que RabbitMQ no envíe más de un mensaje a la vez a un consumidor. Esto ayuda a evitar que un consumidor se sobrecargue y garantiza que las tareas se procesen una por una.

        channel.basic_consume(queue='task_queue', on_message_callback=callback) configura el consumidor para recibir mensajes de la cola task_queue y procesarlos con la función callback().


Durante el proceso de estudio de la herramienta, revisé ejemplos de envío de mensajes en paralelo, trabajo con intercambiadores (exchanges) para envíos a múltiples consumidores.