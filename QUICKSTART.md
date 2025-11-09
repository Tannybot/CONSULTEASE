# ConsultEase - Quick Start Guide

## Quick Setup (5 minutes)

### Step 1: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 2: Set Up Database
```bash
python manage.py makemigrations
python manage.py migrate
```

### Step 3: Create Admin User
```bash
python manage.py createsuperuser
```
Enter a username, email (optional), and password when prompted.

### Step 4: Create Media Directory
```bash
mkdir media
mkdir media\logos
```
(On Windows, use `mkdir media\logos`)

### Step 5: Run Server
```bash
python manage.py runserver
```

### Step 6: Access the Application
1. Open your browser and go to: `http://127.0.0.1:8000/`
2. Log in with the superuser credentials you created
3. Start customizing your site!

## Features

### Login/Logout
- Secure user authentication
- Session management
- Automatic redirect after login

### Custom Logo
- Upload your own logo (PNG, JPG, etc.)
- Logo appears in the header
- Automatic image optimization
- Max file size: 5MB

### Site Name
- Change the website name dynamically
- Updates appear immediately
- Saved to database

### Error Handling
- User-friendly error messages
- Validation for file uploads
- Secure error handling
- Success notifications

## File Structure

```
SYSTEM WEB/
├── consultease/       # Django project settings
├── main/              # Main application
├── templates/         # HTML templates
├── static/            # CSS and JavaScript
│   ├── css/
│   └── js/
├── media/             # Uploaded files
│   └── logos/
└── db.sqlite3         # Database (created after migrations)
```

## Troubleshooting

### "No module named 'django'"
- Make sure you've installed dependencies: `pip install -r requirements.txt`
- Check that you're in the correct virtual environment

### "Table doesn't exist" errors
- Run migrations: `python manage.py migrate`

### Logo not displaying
- Check that the `media` directory exists
- Verify file permissions
- Check browser console for errors

### CSRF errors
- Clear your browser cookies
- Make sure you're accessing the site through `http://127.0.0.1:8000/`

## Next Steps

1. Customize the logo and site name
2. Add more features as needed
3. Customize the CSS in `static/css/style.css`
4. Modify the dashboard in `templates/main/dashboard.html`

## Support

For issues or questions, check the main README.md file for detailed documentation.

