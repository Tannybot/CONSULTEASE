"""
Helper script to set up the logo for ConsultEase.
This script helps you prepare the logo directory and provides instructions.
"""
import os
from pathlib import Path

def setup_logo_directory():
    """Create logo directory and provide setup instructions."""
    base_dir = Path(__file__).resolve().parent
    logo_dir = base_dir / 'static' / 'images'
    
    # Create directory if it doesn't exist
    logo_dir.mkdir(parents=True, exist_ok=True)
    
    print("=" * 60)
    print("Logo Setup for ConsultEase")
    print("=" * 60)
    print()
    print("To add your logo:")
    print("1. Save your logo image file as 'logo.png'")
    print("2. Place it in the following directory:")
    print(f"   {logo_dir}")
    print()
    print("File requirements:")
    print("  - Name: logo.png (or logo.jpg, logo.svg)")
    print("  - Recommended size: 200-300px width, 60-100px height")
    print("  - Format: PNG (recommended) or JPG")
    print()
    print("For favicon (browser tab icon):")
    print("  - Option 1: Use the same logo.png (automatic)")
    print("  - Option 2: Create favicon.ico (16x16 or 32x32px)")
    print(f"  - Place in: {logo_dir}")
    print()
    print("Current directory status:")
    if (logo_dir / 'logo.png').exists():
        print("  [OK] logo.png found!")
    else:
        print("  [X] logo.png not found - please add your logo image")
    if (logo_dir / 'favicon.ico').exists():
        print("  [OK] favicon.ico found!")
    else:
        print("  [INFO] favicon.ico not found (optional - will use logo.png)")
    print()
    print("=" * 60)
    print("Once you've added the logo, restart your Django server.")
    print("The logo will appear automatically in:")
    print("  - Dashboard header")
    print("  - Login page")
    print("  - Registration page")
    print("  - Browser tab (favicon)")
    print("=" * 60)

if __name__ == '__main__':
    setup_logo_directory()

