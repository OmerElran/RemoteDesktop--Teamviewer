import socket
from PIL import ImageGrab

server_address = '0.0.0.0'

my_socket = socket.socket()
my_socket.connect(('192.168.1.42', 5000))
print("Connected to the server")
while True:
    my_socket.send('new'.encode())
    msg = my_socket.recv(1024).decode()
    if msg == 'new':
        while True:
            print('success')
            img = ImageGrab.grab(bbox=(0, 0, 1000, 1000))
            photo_to_send = img.tobytes()

            size = len(photo_to_send)
            print(size)
            my_socket.send(str(size).encode())
            while True:
                reply = my_socket.recv(4096).decode()
                if reply == 'got':
                    my_socket.send(photo_to_send)
                    break
            break
        msg = ''
