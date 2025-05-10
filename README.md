# MultiTools Web Application

A fully responsive Multi-Tools Website with 80+ utility tools organized by categories, built with HTML, JavaScript, Bootstrap, and Flask.

## Overview

This project is a comprehensive collection of web-based tools that users can access without installing any software. The tools are organized into categories such as:

- Image Tools
- SEO Tools
- Text Tools
- Calculators
- Converters
- Social Media Tools
- Miscellaneous Tools

## Technical Stack

- **Backend**: Flask (Python)
- **Frontend**: HTML, CSS, JavaScript
- **CSS Framework**: Bootstrap 5
- **Icons**: Font Awesome
- **Server**: Gunicorn (for production)

## File Structure

```
├── app.py                  # Main Flask application
├── main.py                 # Entry point
├── wsgi.py                 # WSGI entry point for production
├── requirements-production.txt  # Python dependencies
├── .htaccess               # Apache server configuration
├── static/                 # Static assets
│   ├── css/                # CSS files
│   ├── js/                 # JavaScript files
│   └── partials/           # HTML partials for header and footer
└── templates/              # HTML templates
    └── tools/              # Tool-specific templates
```

## Deployment Guide for Hostinger

### Prerequisites

- A Hostinger web hosting account with Python support
- Domain name (optional but recommended)
- Basic knowledge of FTP or file management in Hostinger

### Deployment Steps

1. **Prepare the Files**: 
   - Download all files from this project
   - Make sure you have all the necessary files including the hidden ones (.htaccess)

2. **Set Up Python Environment on Hostinger**:
   - Log in to your Hostinger control panel
   - Go to "Advanced" > "Python" section
   - Create a new Python application
   - Set the application path to the directory where your files will be uploaded
   - Choose Python 3.9+ as your Python version
   - Set entry point to `wsgi.py`

3. **Upload Files to Hostinger**:
   - Use FTP client (like FileZilla) or Hostinger's File Manager
   - Upload all files to your hosting account
   - Make sure to upload to the directory you specified in the Python application setup

4. **Install Dependencies**:
   - Use Hostinger's SSH access or control panel
   - Navigate to your application directory
   - Run: `pip install -r requirements-production.txt`

5. **Configure Environment Variables** (if necessary):
   - Set `SESSION_SECRET` for production security
   - Configure any database connections if needed

6. **Update .htaccess**:
   - Edit the .htaccess file
   - Replace `/path/to/your/wsgi.py` with the actual path to your wsgi.py file
   - Replace `/path/to/your/application` with the actual path to your application

7. **Configure Domain**:
   - In Hostinger control panel, navigate to "Domains" section
   - Point your domain to the directory containing your application

8. **Restart the Application**:
   - In Hostinger control panel, navigate to the Python application
   - Restart the application to apply changes

### Troubleshooting

- **500 Internal Server Error**: Check the error logs in Hostinger control panel
- **Application not loading**: Ensure wsgi.py and app.py are correctly configured
- **Static files not loading**: Check paths and permissions for the static directory

## Additional Notes

- This application uses a simple file-based structure with no database by default
- If you need database functionality, configure your database connection in app.py
- Consider setting up HTTPS for your domain through Hostinger for security

## Customization

To customize the website:
- Edit the templates in the `templates` directory
- Modify CSS in `static/css/styles.css`
- Update tool data in `static/js/dynamic-content.js`