import customtkinter as ctk
from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import os

# Import modules (no change)
from studentnew import student
from train import Train
from face_recognition1 import Face_Recognition
from attendace import attendace
from help import helpdesk
from profile import DeveloperProfile


class face_r_system:
    def __init__(self, root):
        self.root = root
        self.root.geometry("12000x768+0+0")
        
       

        # =============================
        # LIGHT THEME SETTINGS
        # =============================
        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("blue")

        # -------------------------------
        # TOP HEADER BAR
        # -------------------------------
        self.header = ctk.CTkFrame(
            self.root, height=100,
            fg_color="#E8EEF5"
        )
        self.header.pack(fill="x")

        title = ctk.CTkLabel(
            self.header,
            text="FACE RECOGNITION ATTENDANCE SYSTEM",
            font=("Impactt", 36, "bold"),
            text_color="#003B73"
        )
        title.place(relx=0.5, rely=0.5, anchor="center")

        # -------------------------------
        # Light background
        # -------------------------------
        bg_frame = ctk.CTkFrame(
            self.root,
            fg_color="#F5F7FA",
            corner_radius=0
        )
        bg_frame.place(x=0, y=100, relwidth=1, relheight=1)

        # -------------------------------
        # Main Card Container
        # -------------------------------
        self.main_frame = ctk.CTkFrame(
            bg_frame,
            width=1280,
            height=600,
            corner_radius=25,
            fg_color="#FFFFFF",
            border_width=2,
            border_color="#ADB5C2"
        )
        self.main_frame.place(relx=0.5, y=20, anchor="n")

        # Load Dashboard Tiles
        self.dashboard_tiles()


    # =============================
    # Dashboard Button Tiles
    # =============================
    def dashboard_tiles(self):

        buttons_data = [
            ("Student Data", self.student_details, "👨‍🎓"),
            ("Face Detector", self.face_data, "📷"),
            ("Attendance", self.attendance, "📝"),
            ("Chat Bot", self.Help_data, "💬"),
            ("Train Data", self.train_data, "⚙"),
            ("Photos", self.open_img, "🖼"),
            ("Developer",self.devloper, "💻"),
            ("Exit", self.exite, "❌")
        ]

        x_positions = [100, 400, 700, 1000]
        y_positions = [60, 340]

        index = 0
        for row in range(2):
            for col in range(4):
                name, command, icon = buttons_data[index]

                self.create_light_tile(
                    x_positions[col],
                    y_positions[row],
                    name,
                    icon,
                    command
                )
                index += 1

    # =============================
    # Light Theme Modern Tile
    # =============================
    def create_light_tile(self, x, y, text, icon, command):
        tile = ctk.CTkButton(
            self.main_frame,
            width=200,
            height=200,
            corner_radius=25,
            text=f"{icon}\n\n{text}",
            font=("Arial", 24, "bold"),
            fg_color="#F0F4FA",
            hover_color="#CFE1FF",
            text_color="#003B73",
            border_width=2,
            border_color="#B4C5D8",
            command=command
        )
        tile.place(x=x, y=y)

    # ============================
    # Existing Functions (NO CHANGE)
    # ============================
    def open_img(self):
        os.startfile("data")

    def exite(self):
        exite_tkinter = messagebox.askyesno(
            "Exit",
            "Are you sure you want to exit?",
            parent=self.root
        )
        if exite_tkinter:
            self.root.destroy()

    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = student(self.new_window)

    def train_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)

    def face_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Face_Recognition(self.new_window)

    def attendance(self):
        self.new_window = Toplevel(self.root)
        self.app = attendace(self.new_window)

    def Help_data(self):
        self.new_window = Toplevel(self.root)
        self.app = helpdesk(self.new_window)

    def devloper(self):
        self.new_window = Toplevel(self.root)
        self.app = DeveloperProfile(self.new_window)

 


# ====================
# MAIN WINDOW
# ====================
if __name__ == "__main__":
    root = ctk.CTk()
    obj = face_r_system(root)
    root.mainloop()
