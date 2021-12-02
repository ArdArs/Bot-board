import socket

Colors = {
    "red": '-65536',
    "green": '-16711936',
    "blue": '-16776961',
    "yellow": '-256',
    "white": '-1',
    "black": '-16777216',
    "orange": '-32024',
    "purple": '-8453889'
}


class Draw:
    def __init__(self, port: int, addr: str = '127.0.0.1'):
        self.cl = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.col = Colors["red"]
        self.cl.connect((addr, port))

    def set(self, x, y):
        self.cl.send((x + ' ' + y + ' ' + self.col + '\n').encode('utf-8'))

    def clear(self, x, y):
        self.cl.send((x + ' ' + y + ' ' + Colors['black'] + '\n').encode('utf-8'))

    def setColor(self, color: str):
        self.col = color
