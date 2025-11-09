# How to Add Your Logo Image

## Quick Setup

1. **Save your logo image file** with the name `logo.png` in the `static/images/` folder
   - Location: `static/images/logo.png`
   - Supported formats: PNG (recommended), JPG, SVG
   - Recommended dimensions: 200-300px width, 60-100px height

2. **For Favicon (Browser Tab Icon)**:
   - Option 1: The system will automatically use `logo.png` as the favicon
   - Option 2: Create a `favicon.ico` file (16x16 or 32x32 pixels) and place it in `static/images/`

3. **Refresh your browser** - The logo should appear automatically!

## File Structure

```
static/
└── images/
    ├── logo.png        (Your main logo - REQUIRED)
    └── favicon.ico     (Optional - for custom tab icon)
```

## Current Configuration

The logo is configured to display:
- ✅ In the dashboard header
- ✅ On the login page
- ✅ On the registration page
- ✅ As the browser tab icon (favicon)

## Troubleshooting

If the logo doesn't appear:
1. Check that the file is named exactly `logo.png` (case-sensitive)
2. Verify the file is in `static/images/` directory
3. Clear your browser cache
4. Restart the Django development server
5. Check browser console for any errors

## Image Requirements

- **Format**: PNG (recommended for transparency) or JPG
- **Size**: 200-300px width, 60-100px height works best
- **Background**: Transparent PNG works best for logos
- **File size**: Keep under 1MB for best performance

The system will automatically resize the logo to fit the header while maintaining aspect ratio.

