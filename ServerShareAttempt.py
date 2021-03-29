import socket
import threading
import tkinter as tk
import zlib
from PIL import ImageTk, Image
import io

host = '192.168.1.42'
port = 5000
WIDTH = 1900
HEIGHT = 1000

def threadedServerCall(sock):
    print('hello')
    conn, address = sock.accept()
    try:
            while True:
                # Retreive the size of the pixels length, the pixels length and pixels
                size = conn.recv(1024).decode()
                size = int(size)
                # Create the Surface from raw pixels
                
                photo = conn.recv(size)
                img = Image.frombytes('RGB', (WIDTH, HEIGHT), photo)
                img.save('screenshot.png')
                # Display the picture
                new_img = PhotoImage(file ='screenshot.png')
                canvas.itemconfig(imgArea, image = img)
                canvas.photo_ref = img
                clock.tick(60)
    finally:
        sock.close()

def recvall(conn, length):
    """ Retreive all pixels. """

    buf = b''
    while len(buf) < length:
        data = conn.recv(length - len(buf))
        if not data:
            return data
        buf += data
    return buf

def main():
    sock = socket.socket()
    sock.bind((host, port))
    print('start connection...')
    sock.listen()
    thread = threading.Thread(target = threadedServerCall, args = (sock,))
    thread.daemon = True
    thread.start()
    root = tk.Tk()
    root.geometry('800x600')
    canvas = tk.Canvas(root, width = 800, height = 480)
    new_canvas = canvas
    imgArea = canvas.create_image(0, 0, anchor = 'nw', image = r'C:\Users\jerusalem\Documents\Attempt\Screenshot.jpg')
    canvas.pack()
    root.mainloop()
if __name__ == '__main__':
    main()
