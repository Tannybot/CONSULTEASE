# Logo Setup Instructions

## How to Add Your Logo to ConsultEase

The logo can be configured directly in the template code. Follow these steps:

### Option 1: Use a Static File (Recommended)

1. Create a folder for your logo images:
   ```bash
   mkdir static/images
   ```

2. Place your logo file in the `static/images/` folder (e.g., `logo.png`, `logo.jpg`)

3. Open `templates/main/dashboard.html`

4. Find the logo section (around line 17-34)

5. Uncomment Option 1 and update the path:
   ```html
   <img src="{% static 'images/logo.png' %}" alt="ConsultEase Logo" id="site-logo" class="site-logo">
   ```

6. Comment out or remove the other options

### Option 2: Use an External URL

1. Open `templates/main/dashboard.html`

2. Find the logo section

3. Uncomment Option 2 and update the URL:
   ```html
   <img src="https://yourdomain.com/logo.png" alt="ConsultEase Logo" id="site-logo" class="site-logo">
   ```

4. Comment out or remove the other options

### Option 3: Use Database Logo (Admin Upload)

1. Log in to the admin panel: `http://127.0.0.1:8000/admin/`

2. Navigate to "Site Settings"

3. Upload your logo through the admin interface

4. The logo will automatically display if Option 3 is active in the template

### Option 4: Use Text Logo (Current Default)

The current default shows a text-based logo with an icon. This requires no setup.

## Logo Styling

The logo is styled with the class `site-logo`. You can customize it in `static/css/style.css`:

```css
.site-logo {
    max-height: 60px;
    max-width: 200px;
    object-fit: contain;
    border-radius: 4px;
}
```

## Quick Setup Example

1. Add your logo file to `static/images/logo.png`

2. In `templates/main/dashboard.html`, replace the logo section with:
   ```html
   <div class="logo-section">
       <img src="{% static 'images/logo.png' %}" alt="ConsultEase Logo" id="site-logo" class="site-logo">
   </div>
   ```

3. Save and refresh your browser

That's it! Your logo will now display in the header.

