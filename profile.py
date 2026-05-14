import tkinter as tk
from PIL import Image, ImageTk, ImageDraw


class DeveloperProfile:
    def __init__(self, root):
        self.root = root
        self.root.title("Developer Profile")
        self.root.geometry("900x500")
        self.root.configure(bg="white")

        # ===================== ROUNDED IMAGE FUNCTION =====================
        def rounded_image(image, radius=25):
            image = image.convert("RGBA")
            mask = Image.new("L", image.size, 0)
            draw = ImageDraw.Draw(mask)
            draw.rounded_rectangle(
                (0, 0, image.size[0], image.size[1]),
                radius=radius,
                fill=255
            )
            image.putalpha(mask)
            return image

        # ===================== HEADER =====================
        tk.Label(
            self.root,
            text="Hello!",
            font=("Arial", 32, "bold"),
            bg="white"
        ).pack(pady=(20, 5))

        tk.Label(
            self.root,
            text="I'm a creative Python developer",
            font=("Arial", 14),
            bg="white",
            fg="gray"
        ).pack(pady=(0, 20))

        # ===================== MAIN FRAME =====================
        main_frame = tk.Frame(self.root, bg="white")
        main_frame.pack(fill="both", expand=True, padx=40)

        # ===================== IMAGE =====================
        left = tk.Frame(main_frame, bg="white")
        left.grid(row=0, column=0, padx=20)

        img = Image.open(
            "pimages/WhatsApp Image 2026-01-22 at 4.53.20 PM.jpeg"
        )
        img = img.resize((220, 280))
        img = rounded_image(img)

        self.photo = ImageTk.PhotoImage(img)
        tk.Label(left, image=self.photo, bg="white").pack()

        # ===================== ABOUT =====================
        middle = tk.Frame(main_frame, bg="white")
        middle.grid(row=0, column=1, padx=30, sticky="n")

        tk.Label(
            middle,
            text="About me",
            font=("Arial", 16, "bold"),
            bg="white"
        ).pack(anchor="w")

        tk.Label(
            middle,
            text=(
                "I am an enthusiastic Python developer\n"
                "with interest in GUI applications,\n"
                "automation, and real-world projects.\n\n"
                "I enjoy building useful software\n"
                "and continuously learning new\n"
                "technologies."
            ),
            font=("Arial", 11),
            bg="white",
            justify="left"
        ).pack(anchor="w", pady=10)

        # ===================== DETAILS =====================
        right = tk.Frame(main_frame, bg="white")
        right.grid(row=0, column=2, padx=30, sticky="n")

        tk.Label(
            right,
            text="Details",
            font=("Arial", 16, "bold"),
            bg="white"
        ).pack(anchor="w")

        details = [
            ("Name:", "Sujal Khetade"),
            ("Age:", "21 years"),
            ("Location:", "Khed, Maharashtra")
        ]

        for label, value in details:
            row = tk.Frame(right, bg="white")
            row.pack(anchor="w", pady=4)

            tk.Label(row, text=label, font=("Arial", 11, "bold"), bg="white").pack(side="left")
            tk.Label(row, text=value, font=("Arial", 11), bg="white").pack(side="left", padx=5)


# ===================== RUN FILE DIRECTLY =====================
if __name__ == "__main__":
    root = tk.Tk()
    app = DeveloperProfile(root)
    root.mainloop()
