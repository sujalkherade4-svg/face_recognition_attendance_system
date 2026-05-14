from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
from student1 import student
from train import train
import os
from face_recognition1 import face_recognition
from attendace import attendace
from help import helpdesk
import customtkinter as ctk

class face_r_system:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1366x768+0+0")
        self.root.title("face recognizetion system")
        #fist
        img=Image.open(r"C:\Users\admin\Desktop\myproject\pimages\first.webp")
        img=img.resize((500,130),Image.LANCZOS)
        self.photo=ImageTk.PhotoImage(img)

        lbl=Label(self.root,image=self.photo)
        lbl.place(x=0,y=0,width=450,height=130)

 
        #second
        img1=Image.open(r"C:\Users\admin\Desktop\myproject\pimages\download.jpg")
        img1=img1.resize((500,130),Image.LANCZOS)
        self.photo1=ImageTk.PhotoImage(img1)

        bg1=Label(self.root,image=self.photo1)
        bg1.place(x=455,y=0,width=450,height=130)

       #third
        img2=Image.open(r"C:\Users\admin\Desktop\myproject\pimages\first.webp")
        img2=img2.resize((500,130),Image.LANCZOS)
        self.photo2=ImageTk.PhotoImage(img2)

        bg=Label(self.root,image=self.photo2)
        bg.place(x=910,y=0,width=450,height=130)

       #four
        img3=Image.open(r"pimages/wp10281364.webp")
        img3=img3.resize((1366,700),Image.LANCZOS)
        self.photo3=ImageTk.PhotoImage(img3)

        bg=Label(self.root,image=self.photo3)
        bg.place(x=0,y=130,width=1366,height=700)

        
        
        title=Label(bg,text="FACE  RECOGNITION  ATTENDENCE  SYSTEM",font=("Impact",35,"bold"),bg="#121212",fg="white")
        title.place(x=0,y=5,width=1366,height=40)

    
        #student
        img4=Image.open(r"C:\Users\admin\Desktop\myproject\pimages\download (2).jpg")
        img4=img4.resize((150,150),Image.LANCZOS)
        self.photo4=ImageTk.PhotoImage(img4)

        b1=Button(bg,image=self.photo4,command=self.student_details,cursor="hand2")
        b1.place(x=100,y=100,width=150,height=150)

        b2=Button(bg,text="Student Data",command=self.student_details,cursor="hand2",font=("time new roman",15,"bold"),bg="light blue",fg="black")
        b2.place(x=100,y=250,width=150,height=30)

    #student detect 
        img5=Image.open(r"pimages/download21.jpg")
        img5=img5.resize((150,150),Image.LANCZOS)
        self.photo5=ImageTk.PhotoImage(img5)

        b1=Button(bg,image=self.photo5,command=self.face_data,cursor="hand2")
        b1.place(x=400,y=100,width=150,height=150)

        b2=Button(bg,text="Face Detector",command=self.face_data,cursor="hand2",font=("time new roman",15,"bold"),bg="light blue",fg="black")
        b2.place(x=400,y=250,width=150,height=30)

    #Attendace
        img6=Image.open(r"C:\Users\admin\Desktop\myproject\pimages\download (8).jpg")
        img6=img6.resize((150,150),Image.LANCZOS)
        self.photo6=ImageTk.PhotoImage(img6)

        b1=Button(bg,image=self.photo6,cursor="hand2",command=self.attendance)
        b1.place(x=700,y=100,width=150,height=150)

        b2=Button(bg,text="Attendnce",cursor="hand2",command=self.attendance,font=("time new roman",15,"bold"),bg="light blue",fg="black")
        b2.place(x=700,y=250,width=150,height=30)

    #help
        img7=Image.open(r"C:\Users\admin\Desktop\myproject\pimages\download (10).jpg")
        img7=img7.resize((150,150),Image.LANCZOS)
        self.photo7=ImageTk.PhotoImage(img7)

        b1=Button(bg,image=self.photo7,cursor="hand2",command=self.Help_data)
        b1.place(x=1000,y=100,width=150,height=150)

        b2=Button(bg,text="Chat Bot",cursor="hand2",command=self.Help_data,font=("time new roman",15,"bold"),bg="light blue",fg="black")
        b2.place(x=1000,y=250,width=150,height=30)

        #train data
        img8=Image.open(r"C:\Users\admin\Desktop\myproject\pimages\download (1).png")
        img8=img8.resize((150,150),Image.LANCZOS)
        self.photo8=ImageTk.PhotoImage(img8)

        b1=Button(bg,image=self.photo8,command=self.train_data,cursor="hand2")
        b1.place(x=100,y=350,width=150,height=150)

        b2=Button(bg,text="Train Data",cursor="hand2",command=self.train_data,font=("time new roman",15,"bold"),bg="light blue",fg="black")
        b2.place(x=100,y=500,width=150,height=30)

        #photos
        img9=Image.open(r"C:\Users\admin\Desktop\myproject\pimages\images (2).jpg")
        img9=img9.resize((150,150),Image.LANCZOS)
        self.photo9=ImageTk.PhotoImage(img9)

        b1=Button(bg,image=self.photo9,cursor="hand2",command=self.open_img)
        b1.place(x=400,y=350,width=150,height=150)

        b2=Button(bg,text="Photos",cursor="hand2",command=self.open_img,font=("time new roman",15,"bold"),bg= "light blue",fg="black")
        b2.place(x=400,y=500,width=150,height=30)


        #devloper
        img10=Image.open(r"C:\Users\admin\Desktop\myproject\pimages\download (7).jpg")
        img10=img10.resize((150,150),Image.LANCZOS)
        self.photo10=ImageTk.PhotoImage(img10)

        b1=Button(bg,image=self.photo10,cursor="hand2")
        b1.place(x=700,y=350,width=150,height=150)

        b2=Button(bg,text="Devloper",cursor="hand2",font=("time new roman",15,"bold"),bg="light blue",fg="black")
        b2.place(x=700,y=500,width=150,height=30)

       #exit
        img11=Image.open(r"C:\Users\admin\Desktop\myproject\pimages\download (6).jpg")
        img11=img11.resize((150,150),Image.LANCZOS)
        self.photo11=ImageTk.PhotoImage(img11)

        b1=Button(bg,image=self.photo11,cursor="hand2",command=self.exite)
        b1.place(x=1000,y=350,width=150,height=150)

        b2=Button(bg,text="Exit",cursor="hand2",command=self.exite,font=("time new roman",15,"bold"),bg="light blue",fg="black")
        b2.place(x=1000,y=500,width=150,height=30)


    #
    def open_img(self):
        os.startfile("data")

    def exite(self):
        exite_tkinter=messagebox.askyesno("Face Rcognition","Are you sure exit this project",parent=self.root)
        if exite_tkinter >0:
            self.root.destroy()
        else:
            return    

        

        #function buttons
    def student_details(self):
        self.new_window=Toplevel(self.root) 
        self.app=student(self.new_window)   

    def train_data(self):
        self.new_window=Toplevel(self.root) 
        self.app=train(self.new_window)   

    def face_data(self):
        self.new_window=Toplevel(self.root) 
        self.app=face_recognition(self.new_window)   

    def attendance(self):
        self.new_window=Toplevel(self.root) 
        self.app=attendace(self.new_window)   

    def Help_data(self):
        self.new_window=Toplevel(self.root) 
        self.app=helpdesk(self.new_window)  

    # main.py



# main.py
import customtkinter as ctk
def open_main_app():
    root = ctk.CTk()
    app = face_r_system(root)
    root.mainloop()
  

if __name__ == "__main__":
    root=Tk()
    obj=face_r_system(root) 
    root.mainloop()

