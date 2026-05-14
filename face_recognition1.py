from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import mysql.connector
import cv2
import os
import numpy as np
from datetime import datetime


class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1366x768+0+0")
        self.root.title("Face Recognition System")

        title = Label(self.root, text="*FACE RECOGNITION*",
                      font=("times new roman", 35, "bold"),
                      bg="white", fg="green")
        title.place(x=0, y=5, width=1366, height=40)

        img1 = Image.open(r"pimages/wp10281364.webp")
        img1 = img1.resize((1360, 700), Image.LANCZOS)
        self.photo1 = ImageTk.PhotoImage(img1)

        bg1 = Label(self.root, image=self.photo1)
        bg1.place(x=0, y=45, width=1360, height=700)

        b2 = Button(bg1, text="START FACE RECOGNITION",
                    command=self.face_recog, cursor="hand2",
                    font=("Impact", 30, "bold"),
                    bg="black", fg="white")
        b2.place(x=395, y=575, width=580, height=50)

    # ================= ATTENDANCE =================
    def mark_attendance(self, pi, c, r, n, d):
        now = datetime.now()
        date = now.strftime("%Y-%m-%d")
        time = now.strftime("%H:%M:%S")

        if not os.path.exists("log.csv"):
            with open("log.csv", "w") as f:
                f.write("ID,Class,Department,Name,Roll,Time,Date,Status\n")

        with open("log.csv", "r+") as f:
            data = f.readlines()
            name_list = []

            for line in data:
                entry = line.split(",")
                if len(entry) > 6:
                    name_list.append((entry[0], entry[6]))

            if (str(pi), date) not in name_list:
                f.write(f"\n{pi},{c},{d},{n},{r},{time},{date},Present")

    # ================= FACE RECOGNITION =================
    def face_recog(self):

        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        # 🔥 DB connection once
        conn = mysql.connector.connect(
            host="localhost",
            username="root",
            password="sujal@15",
            database="face_recognizer"
        )
        cursor = conn.cursor()

        video_cap = cv2.VideoCapture(0)

        # 🔥 FULL SCREEN WINDOW
        cv2.namedWindow("Face Recognition", cv2.WND_PROP_FULLSCREEN)
        cv2.setWindowProperty("Face Recognition",
                              cv2.WND_PROP_FULLSCREEN,
                              cv2.WINDOW_FULLSCREEN)

        while True:
            ret, img = video_cap.read()
            if not ret:
                break

            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = faceCascade.detectMultiScale(gray, 1.3, 5)

            for (x, y, w, h) in faces:

                face = gray[y:y+h, x:x+w]
                face = cv2.resize(face, (200, 200))

                id, predict = clf.predict(face)

                print("ID:", id, "Distance:", predict)

                # 🔥 STRICT FILTER
                if 20 < predict < 50:

                    cursor.execute(
                        "SELECT student_id, Name, Roll, Dep, class FROM student WHERE student_id=%s",
                        (str(id),)
                    )
                    result = cursor.fetchone()

                    if result:
                        pi, name, roll, dep, cls = result

                        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 3)

                        cv2.putText(img, f"ID: {pi}", (x, y-75),
                                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 255), 2)
                        cv2.putText(img, f"Name: {name}", (x, y-50),
                                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 255), 2)
                        cv2.putText(img, f"Roll: {roll}", (x, y-25),
                                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 255), 2)
                        cv2.putText(img, f"Dept: {dep}", (x, y),
                                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 255), 2)

                        self.mark_attendance(pi, cls, roll, name, dep)

                    else:
                        cv2.putText(img, "Not Found", (x, y-10),
                                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)

                else:
                    # 🔥 FORCE UNKNOWN
                    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 3)
                    cv2.putText(img, "Unknown Face", (x, y-10),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)

            cv2.imshow("Face Recognition", img)

            # 🔥 PRESS ESC TO EXIT
            if cv2.waitKey(1) == 27:
                break

        video_cap.release()
        cursor.close()
        conn.close()
        cv2.destroyAllWindows()


# ================= MAIN =================
if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()