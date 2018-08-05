import logging
import socketserver

log = logging.getLogger('udp_server')
FORMAT_CONS = '%(asctime)s %(name)-12s %(levelname)-5s %(message)s'
logging.basicConfig(level=logging.DEBUG, format=FORMAT_CONS)

class UDPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        data = self.request[0].strip()
        socket = self.request[1]
        log.debug("%s: %r" % (self.client_address[0],data))
        socket.sendto(data.upper(), self.client_address)

def udp_server(host='127.0.0.1', port=1234):
    with socketserver.UDPServer((host, port), UDPHandler) as server:
        log.info("Listening on UDP %s:%s" % (host, port))
        log.info("Press CTRL-C to shut down server.")
        server.serve_forever()

udp_server()
