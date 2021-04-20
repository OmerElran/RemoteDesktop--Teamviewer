from socket import socket
from zlib import compress

import mss

WIDTH = 1900
HEIGHT = 1000
host = '192.168.1.42'  # currrently static, will be changed later to become based on user input.
port = 5000


def retreive_screenshot(sock):
    with mss.mss() as sct:
        # The region to capture
        rect = {'top': 0, 'left': 0, 'width': WIDTH, 'height': HEIGHT}

        while True:
            img = sct.grab(rect)
            pixels = compress(img.rgb, 6)

            size = len(pixels)
            size_len = (size.bit_length() + 7) // 8
            sock.send(bytes([size_len]))

            # Send the actual pixels length
            size_bytes = size.to_bytes(size_len, 'big')
            sock.send(size_bytes)

            # Send pixels
            sock.sendall(pixels)


def main():
    watching = True

    sock = socket()
    sock.connect((host, port))
    try:
        while 'connected':
            retreive_screenshot(sock)
    finally:
        sock.close()


if __name__ == '__main__':
    main()
