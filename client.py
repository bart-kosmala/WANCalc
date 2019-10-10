import socket as skt
from definitions import *


class Client:
    def __init__(self):
        self.socket = skt.socket(skt.AF_INET, skt.SOCK_DGRAM)

    def run(self):
        self.socket.sendto(self.std_client_response(Operation.MODULO, 'xdxdxdxdx'), (L_HOST, L_PORT))

        data, addr = self.socket.recvfrom(1024)

        print('Connected with:', addr[0], 'on port:', addr[1])
        print("msg =", repr(data)[1:])


    def std_client_response(self, operation: str, session_id: str) -> str:
        return Header(operation, Status.OK, session_id, create_timestamp()).to_send()

a = Client()
a.run()