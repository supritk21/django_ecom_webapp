# Django E-Commerce Project

## 🚀 Project Overview
This is a simple e-commerce website built using Django. The project currently includes features such as:
- User Authentication (Signup, Login, Logout)
- Email Verification using Gmail SMTP (with App Passwords)
- Adding Products
- User Details & Address Management

### 🔜 Future Enhancements:
- Shopping Cart
- Order Details
- Password Reset Functionality

---

## 📌 Setup & Installation

### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/supritk21/django_ecom_webapp.git
cd django_ecom_webapp
```

### **2️⃣ Create a Virtual Environment**
```bash
python -m venv env
source env/bin/activate  # On macOS/Linux
env\Scripts\activate  # On Windows
```

### **3️⃣ Install Dependencies**
```bash
pip install -r requirements.txt
```

### **4️⃣ Configure Environment Variables**
1. Generate an **App Password** for Gmail SMTP authentication.
   - Go to **Google Account** → **Security** → **App Passwords**
   - Generate an app password and store it securely.

2. Create a `.env` file in the `ecomm/` directory and add:
```env
EMAIL_HOST_USER="your-email@gmail.com"
EMAIL_HOST_PASSWORD="your-app-password"
```

### **5️⃣ Apply Migrations**
```bash
python manage.py makemigrations
python manage.py migrate
```

### **6️⃣ Create a Superuser**
```bash
python manage.py createsuperuser
```
Provide your email, username, and password when prompted.

### **7️⃣ Run the Development Server**
```bash
python manage.py runserver
```
Visit **http://127.0.0.1:8000/** in your browser.

---

## 📁 Project Structure
```
/ECOMM                  # Base Directory
│── /accounts           # User Authentication Module
│── /base               # Base Application Configurations
│── /ecomm              # Main Django Application
│── /home               # Homepage Application
│── /product            # Product Management Module
│── /public             # Static Files (CSS, JS, Images)
│── /templates          # HTML Templates
│── manage.py           # Django Management Script
│── README.md           # Project Documentation
```

---

## ✨ Contributions
Feel free to contribute by raising issues or submitting pull requests. 🚀

---

## 📜 License
This project is licensed under the **MIT License**.
