from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import cv2
import os
import numpy as np


class Train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1366x768+0+0")
        self.root.title("Train Data Set")

        # Title
        title = Label(self.root, text="*TRAIN DATA SET*", 
                      font=("times new roman", 35, "bold"),
                      bg="white", fg="green")
        title.place(x=0, y=5, width=1366, height=40)

        # Background Image
        img3 = Image.open(r"pimages/download (15).jpg")
        img3 = img3.resize((1366, 700), Image.LANCZOS)
        self.photo3 = ImageTk.PhotoImage(img3)

        bg = Label(self.root, image=self.photo3)
        bg.place(x=0, y=50, width=1366, height=700)

        # Button Image
        img5 = Image.open(r"pimages/download21.jpg")
        img5 = img5.resize((250, 250), Image.LANCZOS)
        self.photo5 = ImageTk.PhotoImage(img5)

        b1 = Button(bg, image=self.photo5, command=self.train_classifier, cursor="hand2")
        b1.place(x=550, y=100, width=250, height=250)

        b2 = Button(bg, text="Train Face Data", command=self.train_classifier,
                    cursor="hand2", font=("times new roman", 20, "bold"),
                    bg="white", fg="dark blue")
        b2.place(x=550, y=360, width=250, height=40)

    # ================= TRAIN FUNCTION =================
    def train_classifier(self):
        data_dir = "data"

        if not os.path.exists(data_dir):
            messagebox.showerror("Error", "Data folder not found!")
            return

        path = [os.path.join(data_dir, file) for file in os.listdir(data_dir)]

        faces = []
        ids = []

        # Load Haarcascade
        face_detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

        for image_path in path:
            try:
                img = Image.open(image_path).convert("L") # grayscale
                img_np = np.array(img, 'uint8')

                # Extract ID (user.ID.imgno.jpg)
                file_name = os.path.split(image_path)[1]
                id = int(file_name.split('.')[1])

                # Detect face
                faces_detected = face_detector.detectMultiScale(img_np, 1.3, 5)

                for (x, y, w, h) in faces_detected:
                    face = img_np[y:y+h, x:x+w]
                    faces.append(face)
                    ids.append(id)

                    cv2.imshow("Training", face)

                print(f"Processed: {file_name} -> ID: {id}")

            except Exception as e:
                print(f"Error processing {image_path}: {e}")

            cv2.waitKey(1)

        if len(faces) == 0:
            messagebox.showerror("Error", "No faces found for training!")
            return

        ids = np.array(ids)

        # Train LBPH Model
        clf = cv2.face.LBPHFaceRecognizer_create(
            radius=1,
            neighbors=8,
            grid_x=8,
            grid_y=8
        )

        clf.train(faces, ids)
        clf.write("classifier.xml")

        cv2.destroyAllWindows()
        messagebox.showinfo("Success", "Training dataset completed successfully!")


# ================= MAIN =================
if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()