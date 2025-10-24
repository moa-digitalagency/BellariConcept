# Bellari Concept - Website CMS

## Project Overview
A modern, professional website for Bellari Concept - a construction and renovation company based in Marrakech, Morocco. This project features full multilingual support (French/English) with real company content, professional images, and a complete Content Management System.

## Recent Changes
- **October 24, 2025**: Major update with real content and multilingual support
  - ✅ **Multilingual Support**: Added French (default) and English language switching
  - ✅ **Real Content**: Integrated actual Bellari Concept content from bellariconcept.com
  - ✅ **Company Logo**: Added official Bellari Concept logo throughout the site
  - ✅ **Professional Images**: Added stock images for all 6 services
  - ✅ **Floating Language Toggle**: Added FR/EN switcher in bottom left corner
  - ✅ **Updated Contact Info**: Real contact details (bellari.groupe@gmail.com, +212 6 35 50 24 61, Marrakech)
  - ✅ **Services**: Construction, Électricité, Plomberie, Peinture, Climatisation, Entretien de Piscine

- **October 24, 2025**: Initial project setup
  - Created Flask backend with PostgreSQL database
  - Implemented CMS system for content and image management
  - Built modern frontend with Tailwind CSS
  - Added admin authentication system
  - Created 5 main pages: Home, About, Services, Portfolio, Contact
  - Security improvements: Protected database initialization, persistent SESSION_SECRET, admin-only access controls

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
3. **Section** - Page content sections (heading, content, images, buttons, **language_code**)
4. **Image** - Uploaded image metadata
5. **SiteSettings** - Global site settings (future use)

### Multilingual Features
- **Languages**: French (default), English
- **Language Storage**: Session-based (persisted across page navigation)
- **Language Toggle**: Floating FR/EN switcher in bottom-left corner
- **Content**: All page sections available in both languages
- **Navigation**: Language-aware menu items (ACCUEIL/HOME, À PROPOS/ABOUT, etc.)
- **Switching**: `/set_language/fr` or `/set_language/en` routes

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
- **IMPORTANT**: Change default password immediately after first login

## Database Initialization
Run `python init_database.py` for initial setup (one-time only).
The `/admin/init-db` route is protected and disabled by default for security.

## Environment Variables
- `DATABASE_URL` - PostgreSQL connection string (auto-configured)
- `SECRET_KEY` - Flask secret key (set for persistent sessions)
- `ADMIN_INIT_ALLOWED` - Enable/disable database initialization endpoint (default: false)

## User Preferences
None specified yet.
