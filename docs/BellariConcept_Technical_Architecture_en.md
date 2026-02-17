[ 🇫🇷 Français ](BellariConcept_Technical_Architecture.md) | [ 🇬🇧 English ]

# ⚙️ Bellari Concept - Technical Architecture
**Date:** 2025
**Author:** Aisance KALONJI (MOA Digital Agency)
**Status:** Confidential / Proprietary

This document details the software architecture, data model, and security mechanisms of the platform.

---

## 1. Technology Stack

### Backend
*   **Language:** Python 3.11+
*   **Web Framework:** Flask 3.x
*   **ORM:** SQLAlchemy (SQL abstraction for SQLite/Postgres compatibility)
*   **Authentication:** Flask-Login + Argon2 (via Werkzeug)
*   **Forms:** Flask-WTF

### Frontend
*   **Templating:** Jinja2 (Server-side rendering)
*   **CSS:** TailwindCSS (v3 via CDN)
*   **Animations:** LottieFiles (via CDN)
*   **Icons:** FontAwesome (via CDN)

### Infrastructure (Production)
*   **OS:** Ubuntu LTS (Recommended)
*   **Web Server:** Nginx (Reverse Proxy, SSL Termination)
*   **WSGI Server:** Gunicorn (Synchronous Workers)
*   **Database:** PostgreSQL (Production) / SQLite (Development)

---

## 2. Data Model (DB Schema)

The application relies on a relational model optimized for CMS flexibility.

### `User` (Administrators)
*   `id`: Integer (PK)
*   `username`: String(80) (Unique)
*   `password_hash`: String(255) (Argon2)

### `Page` (Site Structure)
*   `id`: Integer (PK)
*   `slug`: String(100) (Unique, e.g., 'home', 'about')
*   `title`: String(200) (SEO)
*   `meta_description`: String(300) (SEO)
*   `is_active`: Boolean
*   `sections`: Relationship (One-to-Many to Section)

### `Section` (Polymorphic Content Blocks)
*   `id`: Integer (PK)
*   `page_id`: FK to Page
*   `section_type`: String(50) ('hero', 'intro', 'features', etc.)
*   `language_code`: String(5) ('fr' or 'en')
*   `order_index`: Integer (Position in page)
*   `heading`, `subheading`, `content`: Text fields
*   `image_url`, `background_image`: Media links
*   `background_color`: String(20) (Hex)

### `Image` (Media Library)
*   `id`: Integer (PK)
*   `filename`: String(300) (Secure filename on disk)
*   `original_filename`: String(300)
*   `file_size`: Integer (Bytes)
*   `width`, `height`: Integer (Dimensions)

### `SiteSettings` (Dynamic Configuration)
*   `key`: String(100) (Unique, e.g., 'site_logo', 'pwa_enabled')
*   `value`: Text
*   Stores PWA configuration, social links, and API keys.

---

## 3. Security & Compliance

### 3.1 Content Security Policy (CSP)
Implemented via `Flask-Talisman`.
```python
csp = {
    'default-src': '\'self\'',
    'style-src': ['\'self\'', '\'unsafe-inline\'', 'https://fonts.googleapis.com'],
    'script-src': ['\'self\'', '\'unsafe-inline\'', 'https://cdn.tailwindcss.com'],
    'img-src': ['\'self\'', 'data:', 'https:'],
    ...
}
```
*   Protection against XSS attacks.
*   Forces HTTPS in production.

### 3.2 CSRF Protection
`CSRFProtect(app)` is globally enabled.
*   Every POST form must include an `<input type="hidden" name="csrf_token">`.
*   AJAX requests must include the `X-CSRFToken` header.

### 3.3 Upload Handling
*   Filename cleaning via `werkzeug.utils.secure_filename`.
*   Random prefix (UUID) to avoid collisions.
*   Strict extension checking (`.png`, `.jpg`, `.webp`).

---

## 4. Deployment Strategy

### Database Migration (`init_db.py`)
Unlike Alembic which can be fragile on small VPS without complex CI/CD, this project uses a robust manual migration system ("Smart Init"):
1.  Checks table existence.
2.  Inspects existing columns.
3.  Adds missing columns on the fly (`ALTER TABLE`).
4.  Initializes default data (Pages, Admin) if the table is empty.

### Utility Scripts
*   `deploy.sh`: Interactive wizard to configure environment (`.env`), install dependencies, and initialize the DB.
*   `verify_deployment.py`: Verifies static files (CSS, JS, Images) are accessible and DB is connected before launch.

---
© MOA Digital Agency (myoneart.com) - Author: Aisance KALONJI
