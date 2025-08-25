# 🎓 Django Staff Manager [EMS]

This is a Django-based Staff Management that allows users to **Create, Read, Update, and Delete (CRUD)** staff records. It also includes **user authentication** using Django's built-in auth system.

---

## 🚀 Features

- ⭐ User registration, login, and logout
- ⭐ Add , Show , Update or Delete new staff records
- ⭐ Authentication-protected views
- ⭐ Clean Django templates

---

## 🛠️ Tech Stack

- **Framework:** Django (Python)
- **Frontend:** HTML5
- **Database:** MySQL
- **Auth:** Django built-in authentication

---

## 📁 Project Structure
```
Employee_Management_System/                 # Root GitHub repo
│
├── .gitignore                 # Files and folders Git should ignore
├── requirements.txt           # All required Python packages
├── README.md                  # Project documentation
├── .env                       # Environment variables (excluded from Git)
│
├── Employee_Management_System/             # The main Django project folder
│   ├── manage.py              # Django command-line utility
│   │
│   ├── Employee_Management_System/         # Django settings folder
│   │   ├── __init__.py
│   │   ├── settings.py        # Global settings like apps, middleware, DB, etc.
│   │   ├── urls.py            # Root URL configurations
│   │   ├── wsgi.py            # For WSGI deployment
│   │
│   ├── Emp_app/               # App for Staff [ Employee ] CRUD
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   ├── forms.py
│   │   ├── admin.py
│   │   └── templates/
│   │       └── Emp_app/
│   │           ├── Add_emp.html
│   │           ├── Show_emp.html
│   │           ├── Delete_emp.html
│   │           └── Update_emp.html
│   │
│   ├── Auth_app/              # App for Authentication
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   ├── forms.py
│   │   ├── admin.py
│   │   └── templates/
│   │       └── Auth_app/
│   │           ├── log_in.html
│   │           └── sign_up.html
│   │
│   └── templates/             # Shared project-level templates
│       └── base.html
```

---

## 🔐 Authentication

- Uses Django's built-in `User` model
- Session-based login and logout
- Protected views using `@login_required`

---

## ⚙️ MySQL Database Configuration

In your `settings.py`, the `DATABASES` section should look like this:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'database_name',
        'USER': 'your_mysql_user',
        'PASSWORD': 'your_mysql_password',
    }
}
```

Make sure to install mysqlclient
```bash
 pip install mysqlclient
```

Clone the Repository
```bash
git clone https://github.com/omkarpawar2002/Staff_Manager.git
cd Staff_Manager
```

Create and Activate Virtual Environment
```bash
python -m venv .venv or py -m virtualenv .venv
.\.venv\Scripts\activate   # On Windows
```

Install Dependencies
```bash
pip install -r requirements.txt
```

Generate requirements.txt with:
```bash
pip freeze > requirements.txt
```

Configure settings.py for MySQL and 
Edit the DATABASES setting in your student/settings.py

Run Migrations
```bash
python manage.py migrate
```
Then open:http://127.0.0.1:8000

Start the Server
```bash
python manage.py runserver
or
py manage.py runserver
```

## 👨‍💻 Author

- **Omkar Pawar**  
- GitHub: [@omkarpawar2002](https://github.com/omkarpawar2002)  
- Email: omkarsp20@gmail.com

