import sys
import socket
import tkinter as tkn
from PIL import Image

def cmdbox():
    KeyBoard = tkn.Tk()
    KeyBoard.title('Python Remote Keyboard')
    txt_box = tkn.Entry(KeyBoard, width=100)
    txt_box.pack()
    send = tkn.Button(KeyBoard, text="Type Text", command=lambda: client_socket.send(('sent:'+txt_box.get()).encode()))
    delete = tkn.Button(KeyBoard, text="Delete", command=lambda: client_socket.send(('del'.encode())))
    scrn_shot = tkn.Button(KeyBoard, text="Take screen shot", command = ScreenShot())
    share_file = tkn.Button(KeyBoard, text = "Share File", command = ShareFile(Path))
    delete_button.pack()
    send_button.pack()
    scrn_shot.pack()
    KeyBoard.mainloop()

wall = tkn.Tk()
wall.geometry('960x540') #רבע ממסך רגיל ולכן האופציה הטובה ביותר לניסיון (חצי גם באורך וגם ברוחב). הערה
global x , y, info
 
port = 5000
host = socket.gethostname()

sock = socket.socket()
sock.bind((host,port))
sock.listen(2)

(client_socket, client_address) = sock.accept()

def Share_File(Path): #ניסיון לשיתוף קבצים מצידו של הסרבר אל הלקוח. בנוגע ל-'לקיחה' של קבצים מן הלקוח אל השרת יש לחשוב על מציאת פתרון. הערה
    pass

def ScreenShot():
    client_socket.send('ScrnShot'.encode())
    size = int(my_socket.recv(10).decode('utf-8'))
    the_photo = my_socket.recv(size)
    img_to_save = Image.frombytes("RGB", (490, 490), the_photo)
    img_to_save.save("D:\omer and asaf\screenshotattempt.png")

def movement(event):
    x = event.x
    y = event.y
    info = sock.recv(1024).decode()

    xyinfo = str(x*2.5) + " " + str(y*2.5)
    
    client_socket.send('Motion'.encode())
    client_socket.send(xyinfo.encode())

wall.bind('<Motion>', movement)

def left_click(event):
    client_socket.send('left_click'.encode())

def right_click(event):
    client_socket.send('right_click'.encode())

wall.bind("<Button-1>", left_click)
wall.bind("<Button-2>", right_click)
wall.bind("<Button-3>", right_click) #שני הגדרות ללחיצה ימנית כיוון שללחיצה ימינה יכול להיות שני ערכים שונים 
#בחלק מהמחשבים ולכן יש צורך בשני המקרים. הערה

menubar = tk.Menu(wall)
menubar.add_command(label="Type", command=type_box)
wall.config(menu = menubar)
wall.mainloop()



