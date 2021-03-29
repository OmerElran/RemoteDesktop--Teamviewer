from PIL import ImageGrab, Image, ImageTk
import socket
import tkinter as tk
import time

bufferSize = 1024
address = '0.0.0.0'
ip = '0.0.0.0'
port  = 1112

def funcserver(server_socket):
    time.sleep(2)
    conn, addr = server_socket.accept()
    print('Waiting For Connection...')
    print('Connected to: ')
    while True:
        conn.send('new'.encode())
        msg = conn.recv(4096).decode()
        if msg == 'new':
            while True:
                print('success')
                size = int(conn.recv(bufferSize).decode())
                print(size)
                conn.send('got'.encode())
                the_photo = conn.recv(size)
                img_to_save = Image.frombytes("RGB", (490, 490), the_photo)
                img_to_save.save(r'C:\Users\jerusalem\Documents\Attempt\Screenshot.jpg', 'JPEG')
                break
            changeimg(img_to_save)
            msg = ''
            print('cycle complete')
            time.sleep(1)
def changeimg(img):
    def f():
        img = ImageTk.PhotoImage(Image.open(r'C:\Users\jerusalem\Documents\Attempt\Screenshot.jpg'))
        canvas.itemconfig(img)
        canvas.photo_ref = img
def main():
    server_socket = socket.socket()
    server_socket.bind(('192.168.1.42' ,5000))
    server_socket.listen()
    root = tk.Tk()
    root.geometry('800x600')
    startb = tk.Button(root, text = "Start", command= lambda: funcserver(server_socket))
    startb.pack()
    canvas = tk.Canvas(root, width = 800, height = 480)
    canvas.pack()
    img = ImageTk.PhotoImage(Image.open(r'C:\Users\jerusalem\Documents\Attempt\Screenshot.jpg'))
    canvas.create_image(0,0, anchor ="nw", image = img) #imgArea =
    changeimg(canvas)
    root.mainloop()
    time.sleep(1)
if __name__ == '__main__':
    main()
