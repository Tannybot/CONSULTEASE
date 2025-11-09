# ConsultEase

A Django-based web application with login/logout functionality and an editable UI featuring custom logo upload.

## Features

- User authentication (login/logout)
- User registration with extended profile information
- Custom logo upload
- Editable site name
- Modern, responsive UI
- SQLite database
- Error handling
- User profile management

## Setup Instructions

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

### Installation

1. **Create a virtual environment (recommended):**
   ```bash
   python -m venv venv
   ```

2. **Activate the virtual environment:**
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create a superuser (admin account):**
   ```bash
   python manage.py createsuperuser
   ```
   Follow the prompts to create an admin user. You'll use this account to log in.

6. **Create media directories:**
   ```bash
   mkdir media
   mkdir media/logos
   ```

7. **Run the development server:**
   ```bash
   python manage.py runserver
   ```

8. **Access the application:**
   - Open your browser and go to: `http://127.0.0.1:8000/`
   - Log in with the superuser credentials you created

## Usage

### Registering a New Account

1. Navigate to the registration page (click "Register here" on the login page)
2. Fill in the required fields:
   - Username (required, minimum 3 characters)
   - Email (required, must be unique)
   - Password (required, minimum 8 characters)
   - Confirm Password (must match password)
3. Optionally fill in additional information:
   - First Name, Last Name
   - Phone Number
   - Date of Birth
   - Address, City, Country
4. Click "Register"
5. You will be automatically logged in and redirected to the dashboard

### Logging In

1. Navigate to the login page
2. Enter your username and password
3. Click "Login"
4. If you don't have an account, click "Register here" to create one

### Customizing the Site

1. After logging in, you'll see the dashboard
2. In the settings panel:
   - **Upload Logo**: Click "Choose Logo", select an image file, then click "Upload Logo"
   - **Update Site Name**: Enter a new name and click "Update Name"

### Logging Out

Click the "Logout" button in the header to log out of your account.

## Project Structure

```
SYSTEM WEB/
├── consultease/          # Django project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── main/                 # Main application
│   ├── models.py         # Database models (SiteSettings, UserProfile)
│   ├── views.py          # View functions (login, register, dashboard)
│   ├── urls.py           # URL routing
│   └── admin.py          # Admin configuration
├── templates/            # HTML templates
│   ├── base.html
│   └── main/
│       ├── login.html
│       ├── register.html
│       └── dashboard.html
├── static/               # Static files
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── dashboard.js
├── media/                # Uploaded files (created after setup)
├── db.sqlite3            # SQLite database (created after migrations)
├── manage.py             # Django management script
└── requirements.txt      # Python dependencies
```

## Database Models

### UserProfile
Stores extended user information:
- User (OneToOne relationship with Django User)
- Phone Number
- Date of Birth
- Address
- City
- Country
- Registration Date (automatic)
- Updated At (automatic)

### SiteSettings
Stores site configuration:
- Site Name
- Logo
- Created/Updated timestamps

## Error Handling

The application includes error handling for:
- Invalid login credentials
- Registration validation (username, email uniqueness, password strength)
- File upload errors
- Missing required fields
- Network errors
- File size validation (max 5MB for logos)
- File type validation (images only)
- Duplicate username/email detection

## Development

### Running Migrations

If you modify models, run:
```bash
python manage.py makemigrations
python manage.py migrate
```

### Creating Additional Users

You can create additional users through:
1. Registration page: `http://127.0.0.1:8000/register/` (recommended)
2. Django admin panel: `http://127.0.0.1:8000/admin/`
3. Django shell:
   ```bash
   python manage.py shell
   ```
   Then:
   ```python
   from django.contrib.auth.models import User
   from main.models import UserProfile
   user = User.objects.create_user('username', 'email@example.com', 'password')
   UserProfile.objects.get_or_create(user=user)
   ```

### Viewing Registered Users

You can view all registered users and their profiles in the Django admin panel:
- Navigate to: `http://127.0.0.1:8000/admin/`
- Log in with your superuser credentials
- Go to "User Profiles" to see all registered users with their information

## Troubleshooting

### Issue: "No module named 'django'"
- Make sure you've activated your virtual environment
- Run `pip install -r requirements.txt`

### Issue: "Migration errors"
- Delete `db.sqlite3` and the `migrations` folder in the `main` app
- Run `python manage.py makemigrations` again
- Run `python manage.py migrate` again

### Issue: "Media files not loading"
- Ensure the `media` directory exists
- Check that `MEDIA_ROOT` and `MEDIA_URL` are correctly set in `settings.py`
- Make sure you're running the server in DEBUG mode

### Issue: "CSRF token errors"
- Clear your browser cookies
- Make sure you're accessing the site through the correct URL

## Security Notes

- This is a development setup. For production:
  - Change `SECRET_KEY` in `settings.py`
  - Set `DEBUG = False`
  - Configure proper `ALLOWED_HOSTS`
  - Use a production database (PostgreSQL, MySQL)
  - Set up proper static file serving
  - Use HTTPS
  - Implement additional security measures

## License

This project is open source and available for educational purposes.

