from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import mysql.connector
import cv2



class student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1366x768+0+0")
        self.root.title("student detials")

    #variable
        self.var_dep=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_class=StringVar()
        self.var_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_rollno=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.search_combo=StringVar()
        self.search_entry=StringVar()






      #four
        img3=Image.open(r"C:\Users\admin\Desktop\myproject\pimages\images (1).jpg")
        img3=img3.resize((1366,700),Image.LANCZOS)
        self.photo3=ImageTk.PhotoImage(img3)

        bg=Label(self.root,image=self.photo3)
        bg.place(x=0,y=0,width=1366,height=700)

        title=Label(bg,text="STUDENT  MANAGMENT  SYSTEM",font=("Impact",30,"bold"),bg="white",fg="orange")
        title.place(x=5,y=5,width=1366,height=40)
         
        main_frame=Frame(bg,bd=2)
        main_frame.place(x=5,y=55,width=1340,height=650)
         
        #left
        left_frame=LabelFrame(main_frame,bd=2,bg="white", relief=RIDGE,text="STUDENT DETAILS",font=("times new roman",12,"bold"))
        left_frame.place(x=10,y=5,width=660,height=620)
       
        img3=Image.open(r"pimages/accomplishment-ceremony-college-education-wallpaper-preview.jpg")
        img3=img3.resize((650,75),Image.LANCZOS)
        self.photo3=ImageTk.PhotoImage(img3)

        bg=Label(left_frame,image=self.photo3)
        bg.place(x=2,y=0,width=653,height=75)
        
        #cource
        current_cource=LabelFrame(main_frame,bd=2,bg="white", relief=RIDGE,text="Current Cource Info",font=("times new roman",12,"bold"))
        current_cource.place(x=10,y=100,width=650,height=150)
        #department
        dep_label=Label(current_cource,text="Department:",font=("times new roman",12,"bold"))
        dep_label.grid(row=0,column=0,padx=5,sticky=W)

        dep_combo=ttk.Combobox(current_cource,textvariable=self.var_dep,font=("times new roman",12,"bold"),state="read only")
        dep_combo["values"]=("Select Department","IT","CS","BMS")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=5,sticky=W)

        year_label=Label(current_cource,text="Acadmic year:",font=("times new roman",12,"bold"))
        year_label.grid(row=0,column=2,padx=10)

        year_combo=ttk.Combobox(current_cource,textvariable=self.var_year,font=("times new roman",12,"bold"),state="read only")
        year_combo["values"]=("Acadmic year","2022-23","2023-24","2024-25")
        year_combo.current(0)
        year_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

        semister_label=Label(current_cource,text="Semister:",font=("times new roman",12,"bold"))
        semister_label.grid(row=1,column=0,padx=5,sticky=W)

        semister_combo=ttk.Combobox(current_cource,textvariable=self.var_semester,font=("times new roman",12,"bold"),state="read only")
        semister_combo["values"]=("Semister","sem 1","sem 2","sem 3","sem 4","sem 5","sem 6")
        semister_combo.current(0)
        semister_combo.grid(row=1,column=1,padx=2,pady=5,sticky=W) 

        class_label=Label(current_cource,text="Class name:",font=("times new roman",12,"bold"))
        class_label.grid(row=1,column=2,padx=10)

        class_combo=ttk.Combobox(current_cource,textvariable=self.var_class,font=("times new roman",12,"bold"),state="read only")
        class_combo["values"]=("Select class","FY","SY","TY")
        class_combo.current(0)
        class_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W) 

        #class student info
        class_student_frame=LabelFrame(main_frame,bd=2,bg="white", relief=RIDGE,text="Class student info",font=("times new roman",12,"bold"))
        class_student_frame.place(x=10,y=250,width=650,height=300)  
        #student_id
        student_id=Label(class_student_frame,text="Student ID:",font=("times new roman",12,"bold"))
        student_id.grid(row=0,column=0,padx=5,sticky=W)  

        student_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_id,width=20,font=("times new roman",12,"bold"))            
        student_entry.grid(row=0,column=1,padx=5,pady=5,sticky=W) 
        #student name
        student_name=Label(class_student_frame,text="Student Name:",font=("times new roman",12,"bold"))
        student_name.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        studentn_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_name,width=20,font=("times new roman",12,"bold"))            
        studentn_entry.grid(row=0,column=3,padx=5,pady=5,sticky=W)

        #roll noroll_no 
        roll_no=Label(class_student_frame,text="Roll Number:",font=("times new roman",12,"bold"))
        roll_no.grid(row=1,column=0,padx=5,pady=10,sticky=W)

        roll_no_entry=ttk.Entry(class_student_frame,textvariable=self.var_rollno,width=20,font=("times new roman",12,"bold"))            
        roll_no_entry.grid(row=1,column=1,padx=5,pady=5,sticky=W) 

        #gender
        gender=Label(class_student_frame,text="Gender:",font=("times new roman",12,"bold"))
        gender.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        gender=ttk.Entry(class_student_frame,textvariable=self.var_gender,width=20,font=("times new roman",12,"bold"))            
        gender.grid(row=1,column=3,padx=5,pady=5,sticky=W)
        #dob
        dob=Label(class_student_frame,text="DOB:",font=("times new roman",12,"bold"))
        dob.grid(row=2,column=0,padx=5,pady=5,sticky=W)

        dob=ttk.Entry(class_student_frame,textvariable=self.var_dob,width=20,font=("times new roman",12,"bold"))            
        dob.grid(row=2,column=1,padx=5,pady=5,sticky=W)   

        #email
        email=Label(class_student_frame,text="Email:",font=("times new roman",12,"bold"))
        email.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        email=ttk.Entry(class_student_frame,textvariable=self.var_email,width=20,font=("times new roman",12,"bold"))            
        email.grid(row=2,column=3,padx=5,pady=5,sticky=W)   

        #phon no  
        phon=Label(class_student_frame,text="Phon no.:",font=("times new roman",12,"bold"))
        phon.grid(row=3,column=0,padx=5,pady=10,sticky=W)

        phon=ttk.Entry(class_student_frame,textvariable=self.var_phone,width=20,font=("times new roman",12,"bold"))            
        phon.grid(row=3,column=1,padx=5,pady=5,sticky=W)  

        #address 
        add=Label(class_student_frame,text="Address:",font=("times new roman",12,"bold"))
        add.grid(row=3,column=2,padx=10,pady=10,sticky=W)
       

        
        add=ttk.Entry(class_student_frame,textvariable=self.var_address,width=20,font=("times new roman",12,"bold"))            
        add.grid(row=3,column=3,padx=5,pady=10,sticky=W) 
        #radio button  
        self.var_radio1=StringVar()
        radio=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="Take photo sample",value="yes")
        radio.grid(row=5,column=0,padx=5,pady=10)
        
        self.var_radio2=StringVar()
        radio1=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="No photo sample",value="no")
        radio1.grid(row=5,column=1,padx=5,pady=10)

        button_frame=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        button_frame.place(x=0,y=200,width=655,height=80)

        save_button=Button(button_frame,text="Save",command=self.add_data,width=17,font=("times new roman",12,"bold"),bg="blue",fg="white")
        save_button.grid(row=0,column=0)

        update_button=Button(button_frame,text="Update",command=self.update_data,width=17,font=("times new roman",12,"bold"),bg="blue",fg="white")
        update_button.grid(row=0,column=1)

        delate_button=Button(button_frame,text="Delete",command=self.delete_data,width=17,font=("times new roman",12,"bold"),bg="blue",fg="white")
        delate_button.grid(row=0,column=2)

        reset_button=Button(button_frame,text="Reset",command=self.reset_data,width=17,font=("times new roman",12,"bold"),bg="blue",fg="white")
        reset_button.grid(row=0,column=3)

        take_button=Button(button_frame,command=self.genret_dataset,text="Take Photo sample",width=17,font=("times new roman",12,"bold"),bg="blue",fg="white")
        take_button.grid(row=1,column=0)

        update1_button=Button(button_frame,text="Update phto sample",command=self.genret_dataset,width=17,font=("times new roman",12,"bold"),bg="blue",fg="white")
        update1_button.grid(row=1,column=1)

        #ririghttake
        right_frame=LabelFrame(main_frame,bd=2,bg="white", relief=RIDGE,text="STUDENT DETAILS",font=("times new roman",12,"bold"))
        right_frame.place(x=670,y=5,width=665,height=620)

        imgr=Image.open(r"pimages/accomplishment-ceremony-college-education-wallpaper-preview.jpg")
        imgr=imgr.resize((650,75),Image.LANCZOS)
        self.photor=ImageTk.PhotoImage(imgr)

        bg=Label(right_frame,image=self.photor)
        bg.place(x=2,y=0,width=653,height=75)

        #serch system
        serch_frame=LabelFrame(right_frame,bd=2,bg="white", relief=RIDGE,text="Serch System",font=("times new roman",12,"bold"))
        serch_frame.place(x=5,y=75,width=650,height=70)        

        search=Label(serch_frame,text="Search by:",font=("times new roman",12,"bold"),bg="red")
        search.grid(row=0,column=0,padx=5,pady=5,sticky=W)   
                  
        self.search_combo=ttk.Combobox(serch_frame,font=("times new roman",12,"bold"),state="read only",width=10)
        self.search_combo["values"]=("select","Roll no","phon no","student ID")
        self.search_combo.current(0)
        self.search_combo.grid(row=0,column=1,padx=2,pady=5,sticky=W)  

        
        self.search_entry=ttk.Entry(serch_frame,width=20,font=("times new roman",12,"bold"))            
        self.search_entry.grid(row=0,column=2,padx=5,pady=10,sticky=W) 

        
        search_button=Button(serch_frame,text="Search",command=self.search_data,width=14,font=("times new roman",10,"bold"),bg="blue",fg="white")
        search_button.grid(row=0,column=3)

        show_button=Button(serch_frame,text="Show All",command=self.fetch_data,width=14,font=("times new roman",10,"bold"),bg="blue",fg="white")
        show_button.grid(row=0,column=4)
        #===table
        tabel_frame=Frame(right_frame,bd=2,bg="white", relief=RIDGE)
        tabel_frame.place(x=5,y=150,width=650,height=450)        

        scroll_x=ttk.Scrollbar(tabel_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(tabel_frame,orient=VERTICAL)
        #new add====================================
        style=ttk.Style()
        style.theme_use("default")
        style.configure("Threeview.heading",font=("time new roman",11,"bold"),background="yellow",foreground="orange")

        self.student_table=ttk.Treeview(tabel_frame,columns=("Dep","year","sem","class","id","name","roll no","gender","dob","email","phone","address","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        self.student_table.pack(fill=BOTH,expand=1)

        self.student_table.heading("Dep",text="Deparment")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semister")
        self.student_table.heading("class",text="class")
        self.student_table.heading("id",text="StudentID*")
        self.student_table.heading("roll no",text="Roll no")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="phone")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("photo",text="PhotoSampleStatus")
        self.student_table["show"]="headings"

        self.student_table.column("Dep",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("class",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("roll no",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("photo",width=150)

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

    # function declare=========
    def add_data(self):
        if self.var_dep.get()=="select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All fileds are requrid",parent=self.root)
        else:
            try:
               conn=mysql.connector.connect(host="localhost",username="root",password="sujal@15",database="face_recognizer")
               my_cursor=conn.cursor()
               my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                            
                                                                                                     self.var_dep.get(),
                                                                                                     self.var_year.get(),
                                                                                                     self.var_semester.get(),
                                                                                                     self.var_class.get(),
                                                                                                     self.var_std_id.get(),
                                                                                                     self.var_std_name.get(),
                                                                                                     self.var_rollno.get(),
                                                                                                     self.var_gender.get(),
                                                                                                     self.var_dob.get(),
                                                                                                     self.var_email.get(),
                                                                                                     self.var_phone.get(),
                                                                                                     self.var_address.get(),
                                                                                                     self.var_radio1.get()
                                                                                                )) 
               conn.commit()
               self.fetch_data()
               conn.close()
               messagebox.showinfo("success","student details has been added succefully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)     

        #==fetch data===
    def fetch_data(self):  
        conn=mysql.connector.connect(host="localhost",username="root",password="sujal@15",database="face_recognizer")
        my_cursor=conn.cursor()   
        my_cursor.execute("Select * from student")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close() 


    #get cursor
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]  

        self.var_dep.set(data[0]),
        self.var_year.set(data[1]),
        self.var_semester.set(data[2]),
        self.var_class.set(data[3]),
        self.var_std_id.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_rollno.set(data[6]),
        self.var_gender.set(data[7]),
        self.var_dob.set(data[8]),
        self.var_email.set(data[9]),
        self.var_phone.set(data[10]),
        self.var_address.set(data[11]),
        self.var_radio1.set(data[12])

    #update function    
 
    def update_data(self):
       if self.var_dep.get() == "select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
           messagebox.showerror("Error", "All fields are required", parent=self.root)
       else:
           try:
               Update = messagebox.askyesno("Update", "Do you want to update this data?", parent=self.root)
               if Update:
                   conn = mysql.connector.connect(host="localhost", username="root", password="sujal@15", database="face_recognizer")
                   my_cursor = conn.cursor()

                   my_cursor.execute("""
                       UPDATE student SET 
                           Dep=%s,
                           Year=%s,
                           Semister=%s,
                           class=%s,
                           Name=%s,
                           Roll=%s,
                           Gender=%s,
                           Dob=%s,
                           Email=%s,
                           Phone=%s,
                           Address=%s,
                           Photosample=%s
                       WHERE student_id=%s
                   """, (
                       self.var_dep.get(),
                       self.var_year.get(),
                       self.var_semester.get(),
                       self.var_class.get(),
                       self.var_std_name.get(),
                       self.var_rollno.get(),
                       self.var_gender.get(),
                       self.var_dob.get(),
                       self.var_email.get(),
                       self.var_phone.get(),
                       self.var_address.get(),
                       self.var_radio1.get(),
                       self.var_std_id.get()
                   ))

                   conn.commit()
                   self.fetch_data()
                   conn.close()
                   messagebox.showinfo("Success", "Student details successfully updated", parent=self.root)
               else:
                   return

           except Exception as es:
               messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)

    # delate function
    def delete_data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("Error","student id must requried",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student delete page","do you want to delet",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="sujal@15",database="face_recognizer")
                    my_cursor=conn.cursor()  
                    sql="delete from student where student_id=%s"
                    val=(self.var_std_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()  
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","successfull deleted student data",parent=self.root)  
            except Exception as es:
                messagebox.showerror("Eroor",f"Due To:{str(es)}",parent=self.root)
    #reset 
    def reset_data(self):
        self.var_dep.set("Select Department"),
        self.var_year.set("Acadmic year"),
        self.var_semester.set("Semister"),
        self.var_class.set("Select class")
        self.var_std_id.set(""),
        self.var_std_name.set(""),
        self.var_rollno.set(""),
        self.var_gender.set(""),
        self.var_dob.set(""),
        self.var_email.set(""),
        self.var_phone.set(""),
        self.var_address.set(""),
        self.var_radio1.set("")
                          

    #take photosample===========================================sample

    def genret_dataset(self):
        if self.var_dep.get() == "select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
            return

        try:
            student_id = int(self.var_std_id.get())

        # ✅ Update database
            conn = mysql.connector.connect(host="localhost", username="root", password="sujal@15", database="face_recognizer")
            my_cursor = conn.cursor()

            my_cursor.execute("""
                UPDATE student SET 
                    Dep=%s, Year=%s, Semister=%s, class=%s, Name=%s, Roll=%s, Gender=%s, Dob=%s,
                    Email=%s, Phone=%s, Address=%s, Photosample=%s 
                WHERE student_id=%s
            """, (
                self.var_dep.get(),
                self.var_year.get(),
                self.var_semester.get(),
                self.var_class.get(),
                self.var_std_name.get(),
                self.var_rollno.get(),
                self.var_gender.get(),
                self.var_dob.get(),
                self.var_email.get(),
                self.var_phone.get(),
                self.var_address.get(),
                self.var_radio1.get(),
                student_id
            ))

            conn.commit()
            self.fetch_data()
            self.reset_data()
            conn.close()

            # ✅ Delete old photos
            import glob, os
            for img_file in glob.glob(f"data/user.{student_id}.*.jpg"):
                os.remove(img_file)

            # ✅ OpenCV face capture
            face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

            def face_cropped(img):
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                faces = face_classifier.detectMultiScale(gray, 1.3, 5)
                for (x, y, w, h) in faces:
                    return img[y:y + h, x:x + w]
                return None

            cap = cv2.VideoCapture(0)
            img_id = 0
            while True:
                ret, my_frame = cap.read()
                if not ret:
                    break

                face = face_cropped(my_frame)
                if face is not None:
                    img_id += 1
                    face = cv2.resize(face, (450, 450))
                    face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                    file_name_path = f"data/user.{student_id}.{img_id}.jpg"
                    cv2.imwrite(file_name_path, face)
                    cv2.putText(face, str(img_id), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
                    cv2.imshow("Capturing Face", face)

                if cv2.waitKey(1) == 13 or img_id == 100:
                    break

            cap.release()
            cv2.destroyAllWindows()
            messagebox.showinfo("Result", "Updated photo samples successfully!", parent=self.root)

        except Exception as es:
            messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)

    def search_data(self):
        search_by = self.search_combo.get()
        search_txt = self.search_entry.get()

        if search_by == "select" or search_txt == "":
            messagebox.showerror("Error", "Please select search option and enter search text", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="sujal@15", database="face_recognizer")
                my_cursor = conn.cursor()

                if search_by == "Roll no":
                    my_cursor.execute("SELECT * FROM student WHERE Roll LIKE %s", ('%' + search_txt + '%',))
                elif search_by == "phon no":
                    my_cursor.execute("SELECT * FROM student WHERE Phone LIKE %s", ('%' + search_txt + '%',))
                elif search_by == "student ID":
                    my_cursor.execute("SELECT * FROM student WHERE student_id LIKE %s", ('%' + search_txt + '%',))

                rows = my_cursor.fetchall()
                if len(rows) != 0:
                    self.student_table.delete(*self.student_table.get_children())
                    for row in rows:
                        self.student_table.insert("", END, values=row)
                else:
                    messagebox.showinfo("Info", "No matching record found", parent=self.root)
                conn.close()
            except Exception as es:
                messagebox.showerror("Error", f"Due To :{str(es)}", parent=self.root)
            


















if __name__ == "__main__":
    root=Tk()
    obj=student(root) 
    root.mainloop()
