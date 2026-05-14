from tkinter import *
from tkinter import messagebox
import mysql.connector

class SignupPage:
    def __init__(self, root):
        self.root = root
        self.root.title("Sign Up")
        self.root.state("zoomed")
        self.root.configure(bg="#020617")

        frame = Frame(self.root, bg="#020617")
        frame.place(relx=0.5, rely=0.5, anchor=CENTER)

        Label(frame, text="CREATE ACCOUNT",
              font=("Arial", 28, "bold"),
              fg="white", bg="#020617").pack(pady=20)

        Label(frame, text="Username", fg="#94a3b8",
              bg="#020617").pack(anchor="w")
        self.username = Entry(frame, font=("Arial", 14))
        self.username.pack(fill=X, pady=5)

        Label(frame, text="Password", fg="#94a3b8",
              bg="#020617").pack(anchor="w", pady=(10, 0))
        self.password = Entry(frame, show="*", font=("Arial", 14))
        self.password.pack(fill=X, pady=5)

        Button(frame, text="REGISTER",
               font=("Arial", 14, "bold"),
               bg="#22c55e", fg="white",
               bd=0, command=self.register).pack(fill=X, pady=20)

        Button(frame, text="BACK TO LOGIN",
               bg="#020617", fg="#38bdf8",
               bd=0, command=self.back).pack()

    def register(self):
        user = self.username.get()
        pwd = self.password.get()

        if user == "" or pwd == "":
            messagebox.showerror("Error", "All fields required")
            return

        con = mysql.connector.connect(
            host="localhost",
            user="root",
            password="sujal@15",
            database="face_recognition_db"
        )
        cur = con.cursor()

        try:
            cur.execute("INSERT INTO users (username, password) VALUES (%s, %s)",
                        (user, pwd))
            con.commit()
            messagebox.showinfo("Success", "Account Created Successfully")
            self.back()
        except:
            messagebox.showerror("Error", "Username already exists")

        con.close()

    def back(self):
        self.root.destroy()
        from login import LoginPage
        root = Tk()
        LoginPage(root)
        root.mainloop()
