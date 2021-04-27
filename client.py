import time
import uuid

import zmq

client_identity = str(uuid.uuid4()).encode('utf-8')

context = zmq.Context()
socket = context.socket(zmq.DEALER)
socket.setsockopt(zmq.IDENTITY, client_identity)
socket.connect("tcp://localhost:5556")

print(f'Worker identity: {client_identity.decode("utf-8")}')
try:
    while True:
        socket.send(b'Hello Server!')
        test = socket.recv()
except KeyboardInterrupt:
    print('Stopping client..')
