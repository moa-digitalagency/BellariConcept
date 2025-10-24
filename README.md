# Bellari Concept - Website CMS

A modern, professional website for luxury interior design with a complete Content Management System.

## Features

- ✅ Modern, responsive design with Tailwind CSS
- ✅ Complete CMS for editing all page content
- ✅ Image upload and management system
- ✅ Admin authentication system
- ✅ Mobile-first responsive design
- ✅ SEO-friendly meta tags
- ✅ Section-based content management

## Tech Stack

- **Frontend**: HTML, Tailwind CSS, Vanilla JavaScript
- **Backend**: Python 3.11, Flask, Flask-SQLAlchemy, Flask-Login
- **Database**: PostgreSQL
- **Image Processing**: Pillow

## Installation

1. **Install dependencies**:
   ```bash
   pip install flask flask-sqlalchemy flask-login werkzeug pillow psycopg2-binary python-dotenv
   ```

2. **Set environment variables**:
   ```bash
   export DATABASE_URL="your_postgresql_connection_string"
   export SECRET_KEY="your_secret_key_here"
   ```

3. **Initialize the database** (FIRST TIME ONLY):
   ```bash
   python init_database.py
   ```

4. **Start the server**:
   ```bash
   python app.py
   ```

5. **Access the website**:
   - Public site: `http://localhost:5000`
   - Admin panel: `http://localhost:5000/admin/login`

## Default Admin Credentials

⚠️ **SECURITY WARNING**: Change these immediately after first login!

- **Username**: `admin`
- **Password**: `admin123`

## Admin Panel Features

### Pages Management
- Edit page titles and meta descriptions
- Manage page visibility (active/inactive)
- Access via `/admin/pages`

### Content Sections
- Create, edit, and delete content sections
- Support for multiple section types:
  - Hero sections (with CTAs)
  - Text sections
  - Service sections
  - Feature grids
  - Contact information
- Reorder sections by index
- Toggle section visibility

### Image Management
- Upload images (PNG, JPG, GIF, WEBP)
- View image dimensions and file size
- Copy image URLs for use in content
- Delete unused images
- Access via `/admin/images`

## Color Scheme

- **Primary**: `#1A1A1A` (charcoal black)
- **Secondary**: `#F8F8F8` (warm white)
- **Accent**: `#D4AF37` (elegant gold)
- **Text**: `#333333` (dark grey)
- **Background**: `#FFFFFF` (pure white)
- **Subtle**: `#E5E5E5` (light grey)

## Typography

- **Display Font**: Playfair Display (headings, logo)
- **Body Font**: Inter (content, UI)

## Security Notes

1. **Never use default credentials in production**
2. **Change admin password immediately after setup**
3. **Set a strong SECRET_KEY environment variable**
4. **Database initialization is disabled by default for security**
5. **Only enable ADMIN_INIT_ALLOWED in development**

## File Structure

```
.
├── app.py                      # Main Flask application
├── init_database.py            # Database initialization script
├── templates/
│   ├── base.html              # Main site layout
│   ├── index.html             # Homepage
│   ├── about.html             # About page
│   ├── services.html          # Services page
│   ├── portfolio.html         # Portfolio page
│   ├── contact.html           # Contact page
│   └── admin/
│       ├── base.html          # Admin panel layout
│       ├── login.html         # Admin login
│       ├── dashboard.html     # Admin dashboard
│       ├── pages.html         # Pages list
│       ├── edit_page.html     # Page editor
│       └── images.html        # Image gallery
├── static/
│   └── uploads/               # Uploaded images
└── README.md
```

## Database Models

### User
Admin users for CMS access

### Page
Website pages with slug, title, and meta information

### Section
Content sections within pages (headings, text, images, buttons)

### Image
Uploaded image metadata

### SiteSettings
Global site configuration (future use)

## Development

Run in debug mode (default):
```bash
python app.py
```

The server will run on `http://0.0.0.0:5000` and reload automatically on code changes.

## Production Deployment

1. Set secure environment variables:
   ```bash
   export SECRET_KEY="generate-a-strong-secret-key"
   export DATABASE_URL="production-postgresql-url"
   export FLASK_ENV="production"
   ```

2. Use a production WSGI server (e.g., Gunicorn):
   ```bash
   gunicorn --bind 0.0.0.0:5000 app:app
   ```

3. **Important**: Do NOT set `ADMIN_INIT_ALLOWED=true` in production

## Support

For issues or questions, please contact the development team.

## License

Copyright © 2024 Bellari Concept. All rights reserved.
