# ZeroMQ client - server test implementation

Whilst the documentation of ZeroMQ is very good, it took me a while for me to find the ZeroMQ setup for a common network architecture: many clients to one server (asynchronous) communication. Turns out this is easily possible: a ROUTER (server) - DEALER (client) setup. This repository contains a reference implementation.

### References

- http://wiki.zeromq.org/tutorials:dealer-and-router
- https://gist.github.com/anopheles/3706633
