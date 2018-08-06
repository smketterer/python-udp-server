import logging
import socketserver
import struct

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
        decoded_data = data
        # decoded_data = data.decode('utf-8','ignore')
        log.debug("%s: %r" % (self.client_address[0], decoded_data))
        socket.sendto(data.upper(), self.client_address)

    def finish(self):
        """ Called after the handle() method to perform any clean-up actions required. """
        pass

def udp_server(host='127.0.0.1', port=1234):
    with socketserver.UDPServer((host, port), UDPHandler) as server:
        log.info("Listening on UDP %s:%s" % (host, port))
        log.info("Press CTRL-C to shut down server.")
        server.serve_forever()

udp_server()
