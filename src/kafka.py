from uuid import uuid1
from confluent_kafka import Consumer, KafkaError, Producer

def read(servers, topic):
    """ Generates messages to consume.
        You must consume promptly or the connection will stall """
    settings = {
        'bootstrap.servers': servers,
        'group.id': f'consumer-{uuid1().hex}',
        'default.topic.config': {'auto.offset.reset': 'smallest'}
    }

    reader = Consumer(settings)
    reader.subscribe([topic])

    while True:
        message = reader.poll(1000)
        if not message:
            pass
        if not message.error():
            yield message.value().decode('utf-8')
        elif message.error().code() != KafkaError._PARTITION_EOF: # pylint: disable=protected-access
            raise IOError(message.error())


def write(servers, topic, source):
    """ Writes messages from the generator """
    writer = Producer({'bootstrap.servers': servers})

    for message in source:
        writer.produce(topic, message.encode('utf-8'))
        print(f'Queued: {message}')
    writer.flush()
    print('Wrote outstanding messages')
