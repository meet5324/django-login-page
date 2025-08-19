# Django Login Page

A modern, professional Django login/register system with a blue-themed UI, user profile (with designation), and account deletion feature.

## Features

- User registration with first name, last name, email, user ID, password, and designation
- User login with email and password
- Home page displays user info and designation
- Delete account button (with confirmation)
- Consistent, beautiful blue UI (HTML, CSS, JS)
- Django best practices: `.gitignore`, no tracked venv or cache files

## Quick Start

1. **Clone the repository:**
   ```bash
   git clone https://github.com/meet5324/django-login-page.git
   cd django-login-page/login
   ```
2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   venv\Scripts\activate  # On Windows
   # or
   source venv/bin/activate  # On Mac/Linux
   ```
3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
   *(Create `requirements.txt` if needed: `pip freeze > requirements.txt`)*

4. **Run migrations:**
   ```bash
   python manage.py migrate
   ```

5. **Start the server:**
   ```bash
   python manage.py runserver
   ```

6. **Visit:**
   [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## Screenshots

- **Login, Register, Home**: All pages use a modern blue gradient and are fully responsive.

## Notes

- The `.env` file is ignored for security.
- The `venv` folder and all `__pycache__` files are ignored.
- If you want to customize the UI, edit the HTML/CSS in `accounts/templates/accounts/`.

---

Made with ❤️ using Django.
