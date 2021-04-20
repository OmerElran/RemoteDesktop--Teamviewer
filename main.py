from tkinter import *
from PIL import ImageTk
class Log_In:
    def __init__(self, root):
        self.root = root
        self.root.title('Log-in System')
        self.root.geometry('480x320')

        self.bg = ImageTk.PhotoImage(file = 'D:/TeamViewerOEL/ScreenShareLogo.jpg')
        self.user_photo = ImageTk.PhotoImage(file ='D:/TeamViewerOEL/Username.jpg')
        self.password_photo = ImageTk.PhotoImage(file='D:/TeamViewerOEL/Passwordlock.jpg')

        bg_label = Label(self.root, image = self.bg).pack()
        userEntry = Entry(master = root, )

        self.Add_Button = Button(self.root, text='Add Contact', command=lambda x: self.Open_Contact_window())
        

    def Open_Contact_window(self): #opens new window which takes values for new Contact in db and checks if values were not already in db.
        pass
def main():
    # creates a Tk() object
    root = Tk()
    login = Log_In(root)
    root.mainloop()
if __name__ == '__main__':
    main()