from tkinter import *
from tkinter import messagebox
import mysql.connector
from signup import SignupPage
from newmain import face_r_system


class LoginPage:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.state("zoomed")
        self.root.configure(bg="#020617")

        frame = Frame(self.root, bg="#020617")
        frame.place(relx=0.5, rely=0.5, anchor=CENTER)

        Label(frame, text="SIGN IN",
              font=("Arial", 28, "bold"),
              fg="white", bg="#020617").pack(pady=20)

        Label(frame, text="Username",
              fg="#94a3b8", bg="#020617").pack(anchor="w")

        self.username = Entry(
            frame, font=("Arial", 14),
            bg="#020617", fg="white",
            insertbackground="white"
        )
        self.username.pack(fill=X, pady=5)

        Label(frame, text="Password",
              fg="#94a3b8", bg="#020617").pack(anchor="w", pady=(10, 0))

        self.password = Entry(
            frame, show="*", font=("Arial", 14),
            bg="#020617", fg="white",
            insertbackground="white"
        )
        self.password.pack(fill=X, pady=5)

        Button(frame, text="LOGIN",
               font=("Arial", 14, "bold"),
               bg="#2563eb", fg="white",
               bd=0, command=self.login
               ).pack(fill=X, pady=20)

        Button(frame, text="SIGN UP",
               bg="#020617", fg="#38bdf8",
               bd=0, command=self.open_signup
               ).pack()


    def login(self):
        user = self.username.get()
        pwd = self.password.get()

        if user == "" or pwd == "":
            messagebox.showerror("Error", "All fields required")
            return

        try:
            con = mysql.connector.connect(
                host="localhost",
                user="root",
                password="sujal@15",
                database="face_recognition_db"
            )
            cur = con.cursor()
            cur.execute(
                "SELECT * FROM users WHERE username=%s AND password=%s",
                (user, pwd)
            )
            row = cur.fetchone()
            con.close()

            if row:
                messagebox.showinfo("Success", "Login Successful")
                self.root.destroy()

                root = Tk()
                face_r_system(root)
                root.mainloop()

            else:
                messagebox.showerror("Error", "Invalid Username or Password")

        except Exception as e:
            messagebox.showerror("Database Error", str(e))


    def open_signup(self):
        self.root.destroy()
        root = Tk()
        SignupPage(root)
        root.mainloop()


if __name__ == "__main__":
    root = Tk()
    LoginPage(root)
    root.mainloop()
