# Django Login Page

A modern, professional Django login/register system, user profile (with designation), JWT authentication, email notifications, and account deletion feature.

## Features

- User registration with first name, last name, email, user ID, password, and designation
- Welcome email sent on registration
- User login with username and password
- Login notification email sent to user
- JWT authentication endpoints (API)
- Home page displays user info and designation
- Delete account button (with confirmation)
- Consistent, beautiful blue UI (HTML, CSS, JS)
- Secure credentials using `.env` (never pushed to GitHub)

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

4. **Configure environment variables:**
   - Copy `.env.example` to `.env` and add your email credentials and secret key.

5. **Run migrations:**
   ```bash
   python manage.py migrate
   ```

6. **Start the server:**
   ```bash
   python manage.py runserver
   ```

7. **Visit:**
   [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## JWT API Endpoints

- `/api/token/` - Obtain JWT token
- `/api/token/refresh/` - Refresh JWT token
- `/api/register/` - Register via API

## Screenshots

- **Login, Register, Home**: All pages use a modern blue gradient and are fully responsive.

## Notes

- The `.env` file is ignored for security.
- The `venv` folder and all `__pycache__` files are ignored.
- If you want to customize the UI, edit the HTML/CSS in `accounts/templates/accounts/`.
- Email notifications require valid Gmail app password in `.env`.
