"""
Setup script for ConsultEase Django project.
Run this script to initialize the project.
"""
import os
import sys
import subprocess

def run_command(command):
    """Run a shell command."""
    print(f"Running: {command}")
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error: {result.stderr}")
        return False
    print(result.stdout)
    return True

def main():
    print("ConsultEase Setup Script")
    print("=" * 50)
    
    # Create media directories
    print("\n1. Creating media directories...")
    os.makedirs('media/logos', exist_ok=True)
    print("   ✓ Media directories created")
    
    # Run migrations
    print("\n2. Running migrations...")
    if not run_command('python manage.py makemigrations'):
        print("   ✗ Failed to create migrations")
        return
    print("   ✓ Migrations created")
    
    if not run_command('python manage.py migrate'):
        print("   ✗ Failed to run migrations")
        return
    print("   ✓ Migrations applied")
    
    # Create superuser
    print("\n3. Creating superuser...")
    print("   Please enter details for the admin account:")
    if not run_command('python manage.py createsuperuser'):
        print("   ✗ Failed to create superuser (you can create it manually later)")
    
    print("\n" + "=" * 50)
    print("Setup complete!")
    print("\nTo start the server, run:")
    print("  python manage.py runserver")
    print("\nThen visit: http://127.0.0.1:8000/")

if __name__ == '__main__':
    main()

