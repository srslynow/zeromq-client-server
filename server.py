import json
from collections import defaultdict

import zmq

context = zmq.Context()
socket = context.socket(zmq.ROUTER)
socket.bind("tcp://*:5556")

poll = zmq.Poller()
poll.register(socket, zmq.POLLIN)
counter = defaultdict(int)

print('Starting server...')
try:
    while True:
        # handle input
        sockets = dict(poll.poll(1000))
        if sockets:
            identity, message = socket.recv_multipart()
            counter[identity.decode('utf-8')] += 1
            socket.send_multipart([identity, b'Hello Client!'])
except KeyboardInterrupt:
    print(json.dumps(counter, indent=2))
