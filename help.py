from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import mysql.connector
import cv2



class helpdesk:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1366x768+0+0")
        self.root.title("Help window")

        title=Label(self.root,text=" HELP  DESK ",font=("Impact",35,"bold"),bg="white",fg="ORANGE")
        title.place(x=0,y=5,width=1366,height=40)



        img1=Image.open(r"pimages/benefits-of-helpdesk-software.png")
        img1=img1.resize((1360,650),Image.LANCZOS)
        self.photo1=ImageTk.PhotoImage(img1)

        bg1=Label(self.root,image=self.photo1)
        bg1.place(x=0,y=50,width=1360,height=650)

        email=Label(bg1,text="EMAIL_ID :- sujalkherade4@gmil.com",font=("",20,"bold"),bg="orange",fg="blue")
        email.place(x=430,y=570,width=520,height=40)


if __name__ == "__main__":
    root=Tk()
    obj=helpdesk(root) 
    root.mainloop()  