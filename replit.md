# Bellari Concept - Website CMS

## Project Overview
A modern, professional website for Bellari Concept with a complete Content Management System. This project features a redesigned luxury interior design website with full mobile responsiveness and an integrated backend CMS for easy content management.

## Recent Changes
- **October 24, 2025**: Initial project setup
  - Created Flask backend with PostgreSQL database
  - Implemented CMS system for content and image management
  - Built modern frontend with Tailwind CSS
  - Added admin authentication system
  - Created 5 main pages: Home, About, Services, Portfolio, Contact

## Tech Stack
- **Frontend**: HTML, Tailwind CSS (CDN), Vanilla JavaScript
- **Backend**: Python 3.11, Flask, Flask-SQLAlchemy, Flask-Login
- **Database**: PostgreSQL (Neon)
- **Image Processing**: Pillow

## Project Architecture

### Backend Structure
- `app.py` - Main Flask application with routes, models, and CMS functionality
- `templates/` - Jinja2 templates for frontend and admin
  - `base.html` - Main site layout
  - `index.html`, `about.html`, `services.html`, `portfolio.html`, `contact.html` - Public pages
  - `admin/` - Admin panel templates (dashboard, pages, images, login)
- `static/` - Static assets
  - `uploads/` - User-uploaded images

### Database Models
1. **User** - Admin authentication
2. **Page** - Website pages (slug, title, meta description)
3. **Section** - Page content sections (heading, content, images, buttons)
4. **Image** - Uploaded image metadata
5. **SiteSettings** - Global site settings (future use)

### Color Scheme
- Primary: #1A1A1A (charcoal black)
- Secondary: #F8F8F8 (warm white)
- Accent: #D4AF37 (elegant gold)
- Text: #333333 (dark grey)
- Background: #FFFFFF (pure white)
- Subtle: #E5E5E5 (light grey)

### Typography
- Display Font: Playfair Display (headings, logo)
- Body Font: Inter (content, UI)

## Features
- ✅ Full CMS for editing all page content
- ✅ Image upload and management system
- ✅ Admin authentication (Flask-Login)
- ✅ Mobile-responsive design
- ✅ Modern, professional UI with smooth transitions
- ✅ SEO-friendly meta tags
- ✅ Section-based content management

## Admin Access
- URL: `/admin/login`
- Default credentials: username=`admin`, password=`admin123`
- **IMPORTANT**: Change default password in production

## Database Initialization
Visit `/init-db` to initialize the database with default data and admin user.

## Environment Variables
- `DATABASE_URL` - PostgreSQL connection string (auto-configured)
- `SECRET_KEY` - Flask secret key (auto-generated)

## User Preferences
None specified yet.
