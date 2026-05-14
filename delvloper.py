from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import mysql.connector
import cv2



class devloper:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1366x768+0+0")
        self.root.title("student detials")

        title=Label(self.root,text="DEVLOPER INFORMATION",font=("time new roman",35,"bold"),bg="white",fg="ORANGE")
        title.place(x=0,y=5,width=1366,height=40)



        img1=Image.open(r"pimages/software-developer-g1372d020e_1280.jpg")
        img1=img1.resize((1360,700),Image.LANCZOS)
        self.photo1=ImageTk.PhotoImage(img1)

        bg1=Label(self.root,image=self.photo1)
        bg1.place(x=0,y=45,width=1360,height=700)

        #FRAME
        right_frame=LabelFrame(bg1,bd=5,bg="Black")
        right_frame.place(x=800,y=5,width=550,height=580)

        side_frame=Frame(right_frame,bd=5,bg="silver")
        side_frame.place(x=0,y=0,width=200,height=580)

        
        img2=Image.open(r"pimages/3fbec748-1e22-40e3-b6d5-7dd8a9075377.jpg")
        img2=img2.resize((400,400),Image.LANCZOS)
        self.photo2=ImageTk.PhotoImage(img2)

        bg1=Label(side_frame,image=self.photo2)
        bg1.place(x=0,y=0,width=190,height=200)

        data_frame=Frame(right_frame,bd=2,bg="pink")
        data_frame.place(x=205,y=5,width=350,height=500)

        data=Label(data_frame,text="NAME:SUJAL KHERADE \nDEPARTMENT:IT \nCLASS:TYIT \nC_NAME:I.C.S. COLLEGE KHED \nEMAIL_ID:sujalkherade4@gmail.com  ",font=("time new roman",15,"bold"),bg="black",fg="white",justify="left",anchor="nw")
        data.place(x=0,y=0,width=500,height=200)




       






if __name__ == "__main__":
    root=Tk()
    obj=devloper(root) 
    root.mainloop()      
