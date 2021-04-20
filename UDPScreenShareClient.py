import socket
import zlib

import mss

WIDTH = 1900
HEIGHT = 1000
host = '192.168.1.42'
port=5000

LocalHost = ((host,port))

def split_img(seq, chunk, skip_tail=False):
    lst = []
    if chunk <= len(seq):
        lst.extend([seq[:chunk]])
        lst.extend(split_img(seq[chunk:], chunk, skip_tail))
    elif not skip_tail and seq:
        lst.extend([seq])
    return lst

def retreive_screenshot(sock):
    with mss.mss() as sct:
        # The region to capture
        rect = {'top': 0, 'left': 0, 'width': WIDTH, 'height': HEIGHT}

        while True:
            sliced_image = []
            img = sct.grab(rect)
            pixels = zlib.compress(img.rgb, 6)
            sliced_image = split_img(pixels,int(len(pixels)/10))
            break
            size = len(pixels)
            size_len = (size.bit_length() + 7) // 8
            sock.sendto(bytes([size_len]), LocalHost)

            # Send the actual pixels length
            size_bytes = size.to_bytes(size_len, 'big')
            sock.sendto(size_bytes, LocalHost)
            # Send pixels
            for i in sliced_image:
                sock.sendto(sliced_image.pop(0), LocalHost)

def main():
    watching = True

    UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    try:
        while 'connected':
            retreive_screenshot(UDPClientSocket)
    finally:
        UDPClientSocket.close()


if __name__ == '__main__':
    main()
