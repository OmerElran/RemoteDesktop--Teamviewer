import pyautogui as PAG
import socket
import os
import tkinter as tkn
from PIL import Image
from PIL import ImageGrab

port = 5000
host = input('Host ip address is: ')

pyautogui.alert('Are you sure you want to establish connection with ' + host + '? by doing so, they will be able to control your computer.')

sock = socket.socket()
sock.connect((host,port))

def findXY(xy):
    xy = '180 564'
    x = ''
    y = ''
    xy = xy.replace(' ', 'X')
    print(xy)
    space = False
    c= 0
    for l in xy:
        if l == 'X':
            space = True
        else:
            if space == True:
                y +=l
            if space == False:
                x +=l
    return x, y

y = int(float(y))
x = int(float(x))


def exitpanel():
    Panel.destroy()
    sock.close()

def Control_Panel():
    Panel = tkn.Tk()
    exit_button = tkn.Button(Panel, text = 'exit?', command = exitpanel)
    Panel.geometry('20x30')
    exit_button.pack()
    Panel.mainloop()

while true:
    cmd = sock.recv(1024).decode()

    if cmd == 'Motion':
        xy = sock.recv(1024).decode()
        x, y = findXY(xy)
        PAG.moveTo(x, y)

    if cmd == 'left_click':
        PAG.click(x,y,1)

    elif cmd == 'right_click':
        PAG.click(x ,y ,1 ,0 , button = "Right")

    elif cmd == 'ScrnShot':
        img = ImageGrab.grab(bbox=(10, 10, 500, 500))
        photo_to_send = img.tobytes()
        size = len(photo_to_send)
        client_socket.send(bytes(str(size), 'utf-8'))
        client_socket.send(photo_to_send)

    elif cmd== 'del':
        PAG.press('backspace') #לפי פייתוןאוטוגוי, באקספייס מוחק ולכן הפקודה היא ללחוץ על המוחק
    elif cmd.contains('sent:'):
        txt = cmd.replace('sent:', '')
        PAG.write(txt)
