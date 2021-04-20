import socket
import threading
from zlib import decompress

import pygame

WIDTH = 1900
HEIGHT = 1000
host = '192.168.1.42'
port = 5000


def reunitepixels(lst):
    data = ''
    for i in range(0, 10):
        data = data + string.from_bytes(lst.pop(0), byteorder='big')
    bytedata = bytes(data, 'utf-8')
    return bytedata


def recvall(UDPServerSocket, length):
    """ Retreive all pixels. """

    buf = b''
    while len(buf) < length:
        data = UDPServerSocket.recvfrom(length - len(buf))
        if not data:
            return data
        buf += data
    return buf


def ScreenShare(conn):
    pixels_lst = []  # list of byte chunks
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
        size_len = int.from_bytes(conn.recvfrom(1024), byteorder='big')
        size = int.from_bytes(recvall(conn, size_len), byteorder='big')
        for i in range(1, 11):
            pixels_lst.append(conn.recvfrom(size))
        pixels = decompress(reunitepixels(pixels_lst), 6)
        # Create the Surface from raw pixels
        img = pygame.image.fromstring(pixels, (WIDTH, HEIGHT), 'RGB')
        # Display the picture
        screen.blit(img, (0, 0))
        pygame.display.flip()
        clock.tick(60)


def main():
    UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    UDPServerSocket.bind((host, port))
    try:
        print('Server started.')
        thread = threading.Thread(target=ScreenShare, args=(UDPServerSocket,))
        thread.start()
    finally:
        UDPServerSocket.close()


if __name__ == '__main__':
    main()
