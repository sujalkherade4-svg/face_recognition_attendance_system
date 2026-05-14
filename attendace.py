# attendance_full.py
# Full Attendance system (GUI + safe present tracking + daily CSV + email)
# Replace DB credentials and email environment variables as needed.

from tkinter import *
from tkinter import ttk, messagebox, filedialog
from PIL import Image, ImageTk
import mysql.connector
import os
import csv
from datetime import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# global data (used mainly for import/export & treeview)
mydata = []

class attendace:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1366x768+0+0")
        self.root.title("Attendance system")

        # text variables
        self.var_atten_id = StringVar()
        self.var_class = StringVar()
        self.var_attend_roll = StringVar()
        self.var_atten_name = StringVar()
        self.var_atten_dep = StringVar()
        self.var_atten_time = StringVar()
        self.var_atten_date = StringVar()
        self.var_atten_atten = StringVar()

        # track present students for today (in-memory)
        # Format: set of student_id strings
        self.today_present = set()

        # ---------------- UI ----------------
        # Safe background image load (if missing, white background)
        try:
            bg_img = Image.open(r"pimages/Attendance matters logo.jpg")
            bg_img = bg_img.resize((1366, 700), Image.LANCZOS)
            self.photo_bg = ImageTk.PhotoImage(bg_img)
            bg = Label(self.root, image=self.photo_bg)
            bg.place(x=0, y=0, width=1366, height=700)
        except Exception:
            bg = Label(self.root, bg="white")
            bg.place(x=0, y=0, width=1366, height=700)

        title = Label(bg, text="ATTENDANCE  MANAGEMENT  SYSTEM", font=("Impact", 30, "bold"), bg="white", fg="orange")
        title.place(x=0, y=5, width=1366, height=40)

        main_frame = Frame(bg, bd=2)
        main_frame.place(x=0, y=55, width=1340, height=650)

        # left frame
        left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Attendance", font=("times new roman", 12, "bold"))
        left_frame.place(x=0, y=5, width=620, height=630)

        # small header image on left (safe)
        try:
            logo_img = Image.open(r"pimages/Attendance matters logo.jpg")
            logo_img = logo_img.resize((600, 130), Image.LANCZOS)
            self.photo_logo = ImageTk.PhotoImage(logo_img)
            logo_lbl = Label(left_frame, image=self.photo_logo)
            logo_lbl.place(x=0, y=0, width=600, height=130)
        except Exception:
            pass

        # student info frame
        class_student_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Attendance", font=("times new roman", 12, "bold"))
        class_student_frame.place(x=0, y=160, width=620, height=400)

        # fields
        Label(class_student_frame, text="Attendance ID:", font=("times new roman", 12, "bold")).grid(row=0, column=0, padx=5, sticky=W)
        ttk.Entry(class_student_frame, width=20, textvariable=self.var_atten_id, font=("times new roman", 12, "bold")).grid(row=0, column=1, padx=5, sticky=W)

        Label(class_student_frame, text="Roll:", font=("times new roman", 12, "bold")).grid(row=0, column=2, padx=10, sticky=W)
        ttk.Entry(class_student_frame, width=20, textvariable=self.var_attend_roll, font=("times new roman", 12, "bold")).grid(row=0, column=3, padx=5, sticky=W)

        Label(class_student_frame, text="Name:", font=("times new roman", 12, "bold")).grid(row=1, column=0, padx=5, pady=10, sticky=W)
        ttk.Entry(class_student_frame, width=20, textvariable=self.var_atten_name, font=("times new roman", 12, "bold")).grid(row=1, column=1, padx=5, pady=10, sticky=W)

        Label(class_student_frame, text="Department:", font=("times new roman", 12, "bold")).grid(row=1, column=2, padx=10, pady=5, sticky=W)
        ttk.Entry(class_student_frame, width=20, textvariable=self.var_atten_dep, font=("times new roman", 12, "bold")).grid(row=1, column=3, padx=5, pady=5, sticky=W)

        Label(class_student_frame, text="Time:", font=("times new roman", 12, "bold")).grid(row=2, column=0, padx=5, pady=5, sticky=W)
        ttk.Entry(class_student_frame, width=20, textvariable=self.var_atten_time, font=("times new roman", 12, "bold")).grid(row=2, column=1, padx=5, pady=5, sticky=W)

        Label(class_student_frame, text="Date:", font=("times new roman", 12, "bold")).grid(row=2, column=2, padx=10, pady=5, sticky=W)
        ttk.Entry(class_student_frame, width=20, textvariable=self.var_atten_date, font=("times new roman", 12, "bold")).grid(row=2, column=3, padx=5, pady=5, sticky=W)

        Label(class_student_frame, text="Attendance status:", font=("times new roman", 12, "bold")).grid(row=6, column=0, padx=5, sticky=W)
        attend_combo = ttk.Combobox(class_student_frame, textvariable=self.var_atten_atten, font=("times new roman", 12, "bold"), state="readonly")
        attend_combo["values"] = ("status", "Present", "Absent")
        attend_combo.current(0)
        attend_combo.grid(row=6, column=1, sticky=W)

        Label(class_student_frame, text="Class Name:", font=("times new roman", 12, "bold")).grid(row=6, column=2, padx=10, sticky=W)
        # Use separate variable for class
        self.var_class.set("select Class")
        class_combo = ttk.Combobox(class_student_frame, textvariable=self.var_class, font=("times new roman", 12, "bold"), state="readonly")
        class_combo["values"] = ("select Class", "FY", "SY", "TY")
        class_combo.current(0)
        class_combo.grid(row=6, column=3, padx=2, pady=10, sticky=W)

        # buttons
        button_frame = Frame(class_student_frame, bd=2, relief=RIDGE, bg="white")
        button_frame.place(x=0, y=200, width=620, height=260)

        Button(button_frame, text="Import CSV", command=self.importCsv, width=16, font=("times new roman", 12, "bold"), bg="blue", fg="white").grid(row=0, column=0)
        Button(button_frame, text="Export CSV", command=self.exportcsv, width=16, font=("times new roman", 12, "bold"), bg="blue", fg="white").grid(row=0, column=1)
        Button(button_frame, text="Update", command=self.update_data, width=16, font=("times new roman", 12, "bold"), bg="blue", fg="white").grid(row=0, column=2)
        Button(button_frame, text="Reset", command=self.resetdata, width=16, font=("times new roman", 12, "bold"), bg="blue", fg="white").grid(row=0, column=3)

        button2_frame = Frame(button_frame, bd=2, relief=RIDGE, bg="white")
        button2_frame.place(x=0, y=33, width=619, height=300)

        daily_csv_button = Button(button2_frame, text="Generate Daily CSV", command=self.generate_daily_attendance_csv, width=68, font=("times new roman", 12, "bold"), bg="green", fg="white")
        daily_csv_button.grid(row=0, column=0)

        # small image inside button2_frame (safe)
        try:
            img8 = Image.open(r"pimages/Attendance matters logo.jpg")
            img8 = img8.resize((550, 200), Image.LANCZOS)
            self.photo8 = ImageTk.PhotoImage(img8)
            bg_img2 = Label(button2_frame, image=self.photo8)
            bg_img2.place(x=0, y=50, width=550, height=200)
        except Exception:
            pass

        # right frame (log)
        right_frame = LabelFrame(main_frame, bd=3, bg="white", relief=RIDGE, text="Attendance log", font=("times new roman", 12, "bold"))
        right_frame.place(x=623, y=5, width=730, height=630)

        log_frame = Frame(right_frame, bd=3, bg="white")
        log_frame.place(x=5, y=5, width=710, height=605)

        # scrollbars
        scroll_x = ttk.Scrollbar(log_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(log_frame, orient=VERTICAL)

        self.Attendancereport = ttk.Treeview(log_frame, columns=("id", "class", "department", "name", "roll", "time", "date", "attendance"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.config(command=self.Attendancereport.xview)
        scroll_y.config(command=self.Attendancereport.yview)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        style = ttk.Style()
        style.theme_use("default")
        # correct Treeview heading config
        style.configure("Threeview.heading",font=("time new roman",15,"bold"),background="red",foreground="orange")

        self.Attendancereport.pack(fill=BOTH, expand=1)

        self.Attendancereport.heading("id", text="Atten_ID")
        self.Attendancereport.heading("class", text="Class")
        self.Attendancereport.heading("department", text="Department")
        self.Attendancereport.heading("name", text="Name")
        self.Attendancereport.heading("roll", text="Roll No")
        self.Attendancereport.heading("time", text="Time")
        self.Attendancereport.heading("date", text="Date")
        self.Attendancereport.heading("attendance", text="Attendance")

        self.Attendancereport["show"] = "headings"

        self.Attendancereport.column("id", width=50)
        self.Attendancereport.column("class", width=50)
        self.Attendancereport.column("department", width=100)
        self.Attendancereport.column("name", width=150)
        self.Attendancereport.column("roll", width=75)
        self.Attendancereport.column("time", width=100)
        self.Attendancereport.column("date", width=100)
        self.Attendancereport.column("attendance", width=100)

        self.Attendancereport.bind("<ButtonRelease>", self.getcurssor)

    # fetch data into treeview
    def face_data(self, rows):
        self.Attendancereport.delete(*self.Attendancereport.get_children())
        for i in rows:
            # ensure 8 columns always
            if len(i) >= 8:
                self.Attendancereport.insert("", "end", values=i[:8])
            else:
                padded = i + [""] * (8 - len(i))
                self.Attendancereport.insert("", "end", values=padded)

    # import CSV (log or any csv)
    def importCsv(self):
        global mydata
        mydata.clear()

        file = filedialog.askopenfilename(parent=self.root, initialdir=os.getcwd(), title="Open CSV", filetypes=(("CSV File", "*.csv"), ("All Files", "*.*")))
        if not file:
            return
        try:
            with open(file, newline='', encoding='utf-8') as myfile:
                csvread = csv.reader(myfile, delimiter=",")
                for i in csvread:
                    if not any(cell.strip() for cell in i):
                        continue
                    mydata.append(i)
            self.face_data(mydata)
            messagebox.showinfo("Import", f"Imported {len(mydata)} rows from {os.path.basename(file)}", parent=self.root)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to import: {e}", parent=self.root)

    # export csv
    def exportcsv(self):
        try:
            if len(mydata) < 1:
                messagebox.showerror("No Data", "Empty data", parent=self.root)
                return False
            file = filedialog.asksaveasfilename(parent=self.root, initialdir=os.getcwd(), title="Save CSV", defaultextension='.csv', filetypes=(("CSV File", "*.csv"), ("All Files", "*.*")))
            if not file:
                return
            with open(file, mode="w", newline="", encoding='utf-8') as myfile:
                exportwrite = csv.writer(myfile, delimiter=",")
                for i in mydata:
                    exportwrite.writerow(i)
            messagebox.showinfo("Data Export", f"Your data exported to {os.path.basename(file)} successfully", parent=self.root)
        except Exception as es:
            messagebox.showerror("Error", f"Due to :{str(es)}", parent=self.root)

    # when user clicks a row
    def getcurssor(self, event=""):
        try:
            cur_item = self.Attendancereport.focus()
            content = self.Attendancereport.item(cur_item)
            rows = content.get('values', [])
            if not rows:
                return
            self.var_atten_id.set(rows[0])
            self.var_class.set(rows[1])
            self.var_atten_dep.set(rows[2])
            self.var_atten_name.set(rows[3])
            self.var_attend_roll.set(rows[4])
            self.var_atten_time.set(rows[5])
            self.var_atten_date.set(rows[6])
            self.var_atten_atten.set(rows[7])
        except Exception:
            pass

    # reset form
    def resetdata(self):
        self.var_atten_id.set("")
        self.var_class.set("select Class")
        self.var_attend_roll.set("")
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_atten.set("")

    # update selected row & mydata
    def update_data(self):
        selected = self.Attendancereport.focus()
        if selected == "":
            messagebox.showerror("Error", "Please select a record to update.", parent=self.root)
            return

        updated_row = [
            self.var_atten_id.get(),
            self.var_class.get(),
            self.var_atten_dep.get(),
            self.var_atten_name.get(),
            self.var_attend_roll.get(),
            self.var_atten_time.get(),
            self.var_atten_date.get(),
            self.var_atten_atten.get()
        ]

        # Update the Treeview
        self.Attendancereport.item(selected, values=updated_row)

        # Also update the `mydata` list to reflect changes safely
        index = self.Attendancereport.index(selected)
        if 0 <= index < len(mydata):
            mydata[index] = updated_row
        else:
            mydata.append(updated_row)

        messagebox.showinfo("Success", "Record updated successfully", parent=self.root)

    # ------------------- Methods for face recognition integration -------------------
    # Call this when a student is recognized by webcam (or other source).
    # This will:
    #  - record student_id in memory (self.today_present)
    #  - append a row to log.csv safely (avoids duplicates)
    def write_present_log(self, student_id, class_n="", roll="", name="", department=""):
        """
        Safe log writing: adds the student to self.today_present and appends to log.csv once.
        student_id: str or int
        class_n, roll, name, department: optional strings
        """
        try:
            student_id_str = str(student_id).strip()
            if student_id_str == "":
                return

            # Prevent duplicates
            if student_id_str in self.today_present:
                return

            now = datetime.now()
            time_now = now.strftime("%H:%M:%S")
            today = now.strftime("%Y-%m-%d")

            # mark present in-memory
            self.today_present.add(student_id_str)

            # append to log.csv
            header_needed = not os.path.exists("log.csv") or os.path.getsize("log.csv") == 0
            with open("log.csv", "a", newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                if header_needed:
                    writer.writerow(["Student_ID", "Class", "Roll", "Name", "Department", "Time", "Date", "Attendance"])
                writer.writerow([student_id_str, class_n, roll, name, department, time_now, today, "Present"])

        except Exception as e:
            # don't crash webcam; just print error
            print("write_present_log error:", e)

    # convenience wrapper to be called by face_recognition1.py
    def mark_present(self, student_id, **kwargs):
        """
        Call mark_present(student_id, class_n='FY', roll='12', name='John', department='IT')
        from your face recognition module when a student is confirmed present.
        """
        self.write_present_log(student_id, kwargs.get("class_n", ""), kwargs.get("roll", ""), kwargs.get("name", ""), kwargs.get("department", ""))

    # ------------------- generate daily attendance CSV & email absentees -------------------
    def generate_daily_attendance_csv(self):
        try:
            today = datetime.now().strftime("%Y-%m-%d")
            folder = "AttendanceReports"
            if not os.path.exists(folder):
                os.makedirs(folder)

            attendance_file = os.path.join(folder, f"Attendance_{today}.csv")
            # allow overwrite (but you can change behavior to skip if exists)
            # if os.path.exists(attendance_file):
            #     return  # already generated

            # Step 1: Connect to MySQL to get all students
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="sujal@15", database="face_recognizer")
                my_cursor = conn.cursor()
                my_cursor.execute("SELECT student_id, class, Roll, Name, Dep, Email FROM student")
                all_students = my_cursor.fetchall()
                conn.close()
            except Exception as db_e:
                # If DB fails, fallback to using mydata (imported CSV) if available
                print("DB error, fallback to imported CSV:", db_e)
                # format fallback rows: student_id, class, roll, name, dep, time, date, attendance
                all_students = []
                for row in mydata:
                    sid = row[0] if len(row) > 0 else ""
                    cls = row[1] if len(row) > 1 else ""
                    roll = row[4] if len(row) > 4 else ""
                    name = row[3] if len(row) > 3 else ""
                    dep = row[2] if len(row) > 2 else ""
                    email = ""
                    all_students.append((sid, cls, roll, name, dep, email))

            # Step 2: Use today's present set (from in-memory, updated by write_present_log)
            present_students = set()
            today = datetime.now().strftime("%Y-%m-%d")

            if os.path.exists("log.csv"):
                with open("log.csv", "r", encoding="utf-8") as f:
                    reader = csv.reader(f)
                    next(reader, None)  # skip header

                    for row in reader:
                        if len(row) >= 8:
                            student_id = row[0].strip()
                            date = row[6].strip()
                            status = row[7].strip()

                            if date == today and status == "Present":
                                present_students.add(student_id)  # set of student_id strings

            final_attendance_data = []
            absentees = []  # list of (student_id, name, email)

            for student in all_students:
                # expected: student -> (student_id, class, Roll, Name, Dep, Email)
                try:
                    student_id, db_class, roll, name, department, email = student
                except Exception:
                    # safeguard - create 6-tuple
                    tmp = list(student) + [""] * 6
                    student_id, db_class, roll, name, department, email = tmp[:6]

                student_id_str = str(student_id).strip()

                if student_id_str in present_students:
                    status = "Present"
                    # time could be read from log.csv or stored in a dict if you prefer; we use "--" here
                    time_val = "--"
                    class_for_row = db_class if db_class else ""
                else:
                    status = "Absent"
                    time_val = ""
                    class_for_row = db_class if db_class else ""

                final_attendance_data.append([student_id_str, class_for_row, roll, name, department, time_val, today, status])

                if status == "Absent" and email:
                    absentees.append((student_id_str, name, email))

            # Step 3: Write CSV
            with open(attendance_file, mode="w", newline="", encoding="utf-8") as file:
                writer = csv.writer(file)
                writer.writerow(["Student_ID", "Class", "Roll", "Name", "Department", "Time", "Date", "Attendance"])
                for row in final_attendance_data:
                    writer.writerow(row)

            print(f"[Auto] Created: {attendance_file}")

            # Step 4: Send emails to absentees
            if absentees:
                self.send_absent_emails(absentees, today)

            messagebox.showinfo("Success", f"Daily attendance generated:\n{attendance_file}", parent=self.root)

        except Exception as e:
            messagebox.showerror("Error", f"Auto CSV generation failed:\n{str(e)}", parent=self.root)

    # send absent emails (absentees: list of (student_id, name, email) or (name,email) depending on source)
    def send_absent_emails(self, absentees, date_str):
        sender_email = "sujalkherade4@gmail.com"
        sender_password = "evpjortigutpajvw"  # Use Gmail app password

        for student_id, name, receiver_email in absentees:
            try:
                message = MIMEMultipart()
                message['From'] = sender_email
                message['To'] = receiver_email
                message['Subject'] = f"Absence Notification - {date_str}"

                body = f"""
    Dear {name},

    This is to inform you that you (Student ID: {student_id}) were marked *Absent* on {date_str}.
    
    If this is a mistake, please contact your class coordinator immediately.

    Regards,
    Attendance Monitoring System
                """

                message.attach(MIMEText(body, 'plain'))

                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.starttls()
                server.login(sender_email, sender_password)
                server.send_message(message)
                server.quit()

                print(f"Email sent to {name} ({student_id}) at {receiver_email}")

            except Exception as e:
                print(f" Failed to send email to {receiver_email}: {e}")


# -------------------- RUN --------------------
if __name__ == "__main__":
    root = Tk()
    app = attendace(root)
    root.mainloop()
