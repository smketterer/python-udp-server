import logging, socket, json

log = logging.getLogger('client')
FORMAT_CONS = '%(asctime)s %(name)-12s %(levelname)-5s %(message)s'
logging.basicConfig(level=logging.DEBUG,format=FORMAT_CONS)

def send_test_datagram(host='127.0.0.1', port=1234):
    header = '\x01' # Plaintext header for testing purposes.
    data = {
        'text': 'hello world'
    }
    MESSAGE = (header + json.dumps(data)).encode()
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # Internet, UDP settings
    s.sendto(MESSAGE, (host, port))
    log.debug("Sent: %s" % (MESSAGE))

send_test_datagram()
