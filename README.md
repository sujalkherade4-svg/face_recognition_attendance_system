# 🎓 Advanced Face Recognition Attendance System

## 📖 Overview

The **Advanced Face Recognition Attendance System** is an AI-powered attendance management solution designed to automate the process of recording attendance using facial recognition technology. The system combines **Computer Vision, Machine Learning, Database Management, and GUI Design** into a single platform that provides accurate, contactless, and efficient attendance tracking.

Traditional attendance methods such as manual registers and fingerprint scanners are often time-consuming, error-prone, and vulnerable to proxy attendance. This project eliminates these limitations by automatically identifying students through facial recognition and recording attendance in real time.

---

## 🚀 Key Features

### 🔍 Face Recognition Technology

* Uses **Haar Cascade Classifier** for face detection.
* Implements **LBPH (Local Binary Pattern Histogram)** algorithm for face recognition.
* Works effectively under different lighting conditions and face orientations.
* Real-time face detection and recognition.

### 🧑‍🎓 Student Management System

* Add, Update, Delete, and Search student records.
* Stores student information including:

  * Student ID
  * Name
  * Roll Number
  * Department
  * Class
  * Email Address
* Secure storage using MySQL database.

### 📸 Face Dataset Collection & Training

* Captures multiple facial images using a webcam.
* Preprocesses images through grayscale conversion and face cropping.
* Trains facial recognition model using LBPH algorithm.
* Stores trained model as `classifier.xml`.

### ✅ Automated Attendance Recording

* Automatically marks attendance once a face is recognized.
* Prevents duplicate attendance entries for the same student on the same day.
* Stores attendance data in:

  * MySQL Database
  * CSV Files

### 📊 Daily Attendance Reports

* Automatically generates daily attendance reports.
* Exports attendance data in CSV format.
* Simplifies record management and monitoring.

### 📧 Email Notification System

* Sends automatic email notifications to absent students.
* Uses SMTP-based email service.
* Enhances communication between students, parents, and faculty.

### 🔐 Secure Login System

* Username and Password Authentication.
* Role-based Access Control:

  * Admin
  * Teacher
  * Student
* Password Encryption and Recovery Support.

### 🖥 User-Friendly GUI

* Developed using Tkinter / CustomTkinter.
* Easy navigation with interactive buttons.
* Requires minimal technical knowledge.

---

## 🏗️ System Architecture

The project is divided into multiple independent modules for better maintainability and scalability.

### 1. Main Dashboard Module

* Entry point of the application.
* Provides navigation to all modules.

### 2. Student Management Module

* Manages student information.
* Supports CRUD operations.
* Connected with MySQL database.

### 3. Face Training Module

* Captures face samples.
* Trains recognition model.
* Generates classifier file.

### 4. Face Recognition Module

* Detects and recognizes faces.
* Displays student details on live video feed.
* Marks attendance automatically.

### 5. Attendance Management Module

* Maintains attendance records.
* Generates CSV attendance logs.
* Prevents duplicate entries.

### 6. Email Notification Module

* Sends absentee notifications.
* Uses Gmail SMTP server.

### 7. Help Desk Module

* Displays support information.
* Provides troubleshooting assistance.

### 8. Login Module

* Secure authentication.
* Role-based access management.
* Password protection and recovery.

---

## 🛠 Technologies Used

| Technology              | Purpose                      |
| ----------------------- | ---------------------------- |
| Python                  | Core Programming Language    |
| OpenCV                  | Face Detection & Recognition |
| Tkinter / CustomTkinter | GUI Development              |
| MySQL                   | Database Management          |
| NumPy                   | Numerical Operations         |
| Pillow (PIL)            | Image Processing             |
| CSV                     | Attendance Report Storage    |
| SMTP                    | Email Notifications          |

---

## 📂 Project Structure

```text
Advanced-Face-Recognition-Attendance-System/
│
├── data/
├── classifier.xml
├── login.py
├── student.py
├── train.py
├── face_recognition.py
├── attendance.py
├── helpdesk.py
├── main.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/your-username/Advanced-Face-Recognition-Attendance-System.git
```

### Navigate to Project Folder

```bash
cd Advanced-Face-Recognition-Attendance-System
```

### Install Required Packages

```bash
pip install -r requirements.txt
```

### Configure Database

1. Install MySQL.
2. Create the required database.
3. Update database credentials in the source code.

### Run Application

```bash
python main.py
```

---

## 📋 Workflow

1. Login to the system.
2. Register student details.
3. Capture face samples.
4. Train the recognition model.
5. Start face recognition.
6. Automatically mark attendance.
7. Generate attendance reports.
8. Send absentee email notifications.

---

## 🧪 Testing

The system has been successfully tested for:

* User Authentication
* Student Registration
* Face Dataset Collection
* Face Training
* Face Recognition
* Attendance Recording
* Duplicate Attendance Prevention
* CSV Report Generation
* Email Notifications
* Logout Functionality

All test cases passed successfully.

---

## 🔒 Security Features

* User Authentication & Authorization
* Password Encryption
* SQL Injection Protection
* Secure Database Access
* Email Security via SSL/TLS
* Attendance Duplication Prevention

---

## 📈 Future Enhancements

* Deep Learning Based Face Recognition (CNN)
* Cloud-Based Deployment
* Mobile Application Support
* Multi-Camera Integration
* Face Mask Detection
* Advanced Analytics Dashboard
* LMS/ERP Integration
* Enhanced Security Mechanisms

---

## 🎯 Project Outcome

The system successfully automates attendance management using face recognition technology. It improves efficiency, reduces manual effort, prevents proxy attendance, and provides accurate attendance records through a secure and user-friendly platform.

---

## 👨‍💻 Author

**Sujal Kherade**

Bachelor of Computer Applications (BCA)

Academic Project – Advanced Face Recognition Attendance System

---

## 📄 License

This project is developed for educational and academic purposes.

MIT License


## Future Improvements
- Email Notifications
- Cloud Database
- Mobile App Integration

## Author
Sujal Kherade
