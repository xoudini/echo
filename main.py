import os, sys, socketserver, logging


BUFFER_SIZE = 4096
HOST = os.environ.get('HOST', '')
PORT = int(os.environ.get('PORT', '8000'))


logger = logging.getLogger('echo')
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)


class EchoHandler(socketserver.BaseRequestHandler):
    def handle(self):
        self.data = self.request.recv(BUFFER_SIZE)
        client = ':'.join(map(str, self.client_address))
        message = f'{client} - {len(self.data)} bytes'
        logger.debug(message)
        self.request.sendall(self.data)


if __name__ == '__main__':
    address = (HOST, PORT)

    with socketserver.TCPServer(address, EchoHandler) as server:
        logger.debug(f'Serving on {":".join(map(str, address))}')
        server.serve_forever()
