import logging, socketserver, struct, json

log = logging.getLogger('udp_server')
FORMAT_CONS = '%(asctime)s %(name)-12s %(levelname)-5s %(message)s'
logging.basicConfig(level=logging.DEBUG, format=FORMAT_CONS)

class UDPHandler(socketserver.BaseRequestHandler):
    def setup(self):
        """ Called before the handle() method to perform any initialization actions required. """
        pass

    def handle(self):
        data = self.request[0]
        socket = self.request[1]
        # Ignore buffer headers, get the data following the byte header (1, or \x01).
        decoded_data = data.decode(encoding='utf-8', errors='ignore').split('\x01')[1:]
        for data_json in decoded_data:
            data_object = json.loads(data_json)
            log.debug("%s: %r" % (self.client_address[0], data_object))
            self.send_to(socket, self.client_address, data_json)

    def send_to(self, socket, address, message):
        socket.sendto((message).encode(), address)

    def finish(self):
        """ Called after the handle() method to perform any clean-up actions required. """
        pass

def udp_server(host='127.0.0.1', port=1234):
    with socketserver.UDPServer((host, port), UDPHandler) as server:
        log.info("Listening on UDP %s:%s" % (host, port))
        log.info("Press CTRL-C to shut down server.")
        server.serve_forever()

udp_server()
