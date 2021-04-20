import socket
import threading
from zlib import decompress

import pygame

WIDTH = 1900
HEIGHT = 1000
host = '192.168.1.42' # currrently static, will be changed later to become based on user input.
port = 5000


def recvall(conn, length):
    """ Retreive all pixels. """

    buf = b''
    while len(buf) < length:
        data = conn.recv(length - len(buf))
        if not data:
            return data
        buf += data
    return buf


def ScreenShare(conn):
    pygame.init()
    screen = pygame.display.set_mode((950, 500))
    clock = pygame.time.Clock()
    watching = True
    while watching:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                watching = False
                break
        # Retreive the size of the pixels length, the pixels length and pixels
        size_len = int.from_bytes(conn.recv(1), byteorder='big')
        size = int.from_bytes(recvall(conn, size_len), byteorder='big')
        pixels = decompress(recvall(conn, size))
        # Create the Surface from raw pixels
        img = pygame.image.fromstring(pixels, (WIDTH, HEIGHT), 'RGB')
        # Display the picture
        screen.blit(img, (0, 0))
        pygame.display.flip()
        clock.tick(60)


def main():
    sock = socket.socket()
    sock.bind((host, port))
    try:
        sock.listen(5)
        print('Server started.')

        while 'connected':
            conn, addr = sock.accept()
            print('Client connected IP:', addr)
            thread = threading.Thread(target=ScreenShare, args=(conn,))
            thread.start()
    finally:
        sock.close()


if __name__ == '__main__':
    main()
