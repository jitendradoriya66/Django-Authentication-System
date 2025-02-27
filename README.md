📜 Project Overview

Welcome to the Django Authentication System — a secure and user-friendly authentication platform built with Django. This project provides seamless user registration, login, and password recovery features using OTP-based verification, ensuring data security with robust password hashing and session management.

✨ Features

🔒 User Registration: Collects user details — Name, Phone, Email, Password, and Confirm Password. Validates email uniqueness and password match.

🚪 Login & Logout: Secure user authentication using email and password. Implements Django's login() and logout() functions.

🔐 Forgot Password: OTP-based password reset flow — users verify OTP sent to their email and set a new password.

📊 Password Security: Uses Django’s password hashing system for secure storage.

📦 Database Integration: Built with MySQL for storing user data. Supports CRUD operations for user management.

🏗️ Project Setup

1. Clone the repository
   git clone <repository_url>
cd django-auth-system

2. # Windows
python -m venv env
# Mac/Linux
python3 -m venv env

3.# Windows
env\Scripts\activate
# Mac/Linux
source env/bin/activate

4.pip install -r requirements.txt

5.Configure MySQL database

Update settings.py with your MySQL credentials:
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'your_db_name',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

6. python manage.py makemigrations
python manage.py migrate

7.python manage.py createsuperuser

8.python manage.py runserver

9. 🛠️ Technologies Used

Django

Python

MySQL

HTML & CSS (for templates)

🚀 How to Contribute

Fork the repository.

Create a new branch.

Implement your changes.

Test thoroughly.

Submit a pull request.

📞 Contact

Feel free to reach out if you have any questions or suggestions!

GitHub: jitendradoriya66

Email: jitendradoriya92@gmail.com

⭐ Don’t forget to star this repository if you find it helpful!

