import socket as sock
import time

class API:
    def __init__(self):
        self.socket = sock.socket(sock.AF_INET, sock.SOCK_STREAM)
        self.socket.connect(('localhost', 8057))

    def addBlock(self, position):
        """
        입력 받은 좌표에 모래블록을 생성합니다. \n
        :param position: (x, y, z) \n
        """
        self.socket.send((' '.join(repr(n) for n in position) + '\n').encode('utf-8'))
        time.sleep(0.1)
        print('send : ', ' '.join(repr(n) for n in position))

