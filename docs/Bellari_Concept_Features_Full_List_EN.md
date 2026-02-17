![Python 3.11](https://img.shields.io/badge/Python-3.11-blue?style=flat-square&logo=python) ![Flask 3.0](https://img.shields.io/badge/Framework-Flask%203.0-green?style=flat-square&logo=flask) ![PostgreSQL 15](https://img.shields.io/badge/Database-PostgreSQL%2015-336791?style=flat-square&logo=postgresql) ![Status: Stable](https://img.shields.io/badge/Status-Stable-success?style=flat-square) ![License: Proprietary](https://img.shields.io/badge/License-Proprietary-red?style=flat-square) ![Owner: MOA Digital Agency](https://img.shields.io/badge/Owner-MOA%20Digital%20Agency-orange?style=flat-square)

# Bellari Concept - Full Features List

> **LEGAL NOTICE**
>
> This document and the associated source code are the exclusive property of **MOA Digital Agency** and **Aisance KALONJI**.
> Any unauthorized reproduction, distribution, or use is strictly prohibited.
> Internal Use Only.

---

This document exhaustively details all technical and business functionalities implemented in the Bellari Concept CMS.

## 1. Content Management (CMS)
The core of the system relies on a flexible architecture enabling fluid bilingual (French/English) management.

### 1.1 Page and Section Architecture
*   **`Page` Model:** Management of static pages (Home, About, Services, Portfolio, Contact) with custom slugs.
*   **`Section` Model:** Each page is composed of modular blocks (`hero`, `text`, `service`, `contact`, `features`).
*   **Bilingual Synchronization:**
    *   The "Section Normalization" system (`normalize_sections.py` / Admin Route) ensures each FR section has an EN equivalent with the same `order_index`.
    *   The editing interface allows simultaneous creation of FR and EN content.
*   **Page-Level SEO:** Individually editable titles (`title`) and meta-descriptions.

### 1.2 Media Management
*   **Secure Upload:** Verification of extensions (`png`, `jpg`, `jpeg`, `gif`, `webp`) and file name sanitization (`werkzeug.secure_filename`).
*   **Optimization:** Storage of metadata (size, dimensions) in the database (`Image` model).
*   **Visualization:** Image gallery in the administration interface with preview.

### 1.3 Administration Interface
*   **Dashboard:** Overview of pages and latest uploaded images.
*   **WYSIWYG Editor (Textarea):** Rich text fields for section content.
*   **Site Settings Management:** Dynamic configuration (Site Name, Logos, Social Links) without redeployment via the `SiteSettings` table.

## 2. Security & Robustness
Security is integrated at every level of the application.

### 2.1 Authentication & Authorization
*   **Argon2 Hashing:** Use of `werkzeug.security` for robust administrator password hashing.
*   **Session Management:** Secure cookies (`HttpOnly`, `Secure`, `SameSite='Lax'`).
*   **Admin Protection:** `@login_required` decorator on all `/admin` routes.

### 2.2 Web Protections
*   **CSRF (Cross-Site Request Forgery):** Global protection via `Flask-WTF` on all POST forms.
*   **CSP (Content Security Policy):** Strict configuration via `flask-talisman` to prevent XSS attacks.
    *   Only allows trusted sources (Self, Google Fonts, Tailwind CDN).
    *   Forces HTTPS in production.
*   **Error Management:** Custom error pages (400, 403, 404, 451) with Lottie animations for better UX even during issues.

## 3. Progressive Web App (PWA)
The site is fully PWA compatible, transforming the website into an installable application.

*   **Dynamic Manifest:** Route `/manifest.json` generated on the fly from the database (`SiteSettings`).
*   **Admin Configuration:**
    *   Enable/Disable PWA.
    *   Customization of name, colors (theme/background), and icons.
    *   Choice of display mode (`standalone`, `fullscreen`, etc.).
*   **Mobile Support:** `viewport` and `meta` tags optimized for mobile experience.

## 4. Technical & SEO Optimization
*   **Automatic XML Sitemap:** Route `/sitemap.xml` dynamically generating the list of active pages with their modification date (`lastmod`) and priority.
*   **Dynamic Robots.txt:** Route `/robots.txt` configured to allow legitimate search engines (Google, Bing) and block malicious or useless bots (MJ12bot, Ahrefs, etc.).
*   **Language Management:** Route `/set_language/<lang>` with session storage for user choice persistence.

## 5. Deployment & Maintenance
Automated scripts ensure reliable and reproducible deployment.

*   **`deploy.sh`:**
    *   System dependency check (Python 3.11+, pip).
    *   Automatic secure `.env` generation (random secret keys).
    *   Virtual environment creation and activation (`.venv`).
    *   Python dependency installation.
*   **`init_db.py` (Robust Migration):**
    *   "Home-made" VPS migration system: checks table existence AND columns.
    *   Automatically adds missing columns (ALTER TABLE) without data loss.
    *   Intelligent default content initialization (Pages, Sections, Admin) if the database is empty.
*   **`verify_deployment.py`:** Pre-flight script verifying DB connection and critical static files presence.

---
*© 2024 MOA Digital Agency. All rights reserved.*
