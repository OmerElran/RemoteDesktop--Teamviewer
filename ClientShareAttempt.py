import socket
import threading
from PIL import Image
import mss

WIDTH = 1900
HEIGHT = 1000
host = '192.168.1.42'
port=5000

def retreive_screenshot(sock):
    with mss.mss() as sct:
        # The region to capture
        rect = {'top': 0, 'left': 0, 'width': WIDTH, 'height': HEIGHT}

        while 'recording':
            sct_img = sct.grab(rect)
            img = Image.frombytes('RGB',sct_img.size, sct_img.rgb)
            byte_img = img.tobytes()
            size = len(byte_img)
            sock.send(str(size).encode())
            # Send pixels
            sock.sendall(byte_img)

def main():
    sock = socket.socket()
    sock.connect((host, port))
    try:
        thread = threading.Thread(target=retreive_screenshot, args=(sock,))
        thread.start()
        while 'recording':
            x = 1
    finally:
        sock.close()
if __name__ == '__main__':
    main()
