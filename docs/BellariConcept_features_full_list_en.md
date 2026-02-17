[ 🇫🇷 Français ](BellariConcept_features_full_list.md) | [ 🇬🇧 English ]

# 📜 Bellari Concept - Feature Bible
**Last Updated:** 2025
**Author:** Aisance KALONJI (MOA Digital Agency)
**Usage:** Internal & Confidential

This document exhaustively lists all technical and business functionalities of the Bellari Concept platform.

---

## 1. Core System (Core)

*   **Framework:** Python Flask 3.x.
*   **Database:** SQLAlchemy ORM (Compatible with SQLite Dev / PostgreSQL Prod).
*   **MVC Architecture:** Clear separation of Models (DB), Views (Jinja2), Controllers (Routes).
*   **Error Handling:** Custom error pages with Lottie animations (400, 403, 404, 451).

## 2. Content Management System (CMS)

### 2.1 Page Management
*   **CRUD Pages:** Create, Read, Update pages (Home, About, Services, etc.).
*   **Metadata:** Edit Title Tag, Slug (URL), and Meta Description for SEO.
*   **Activation:** Ability to enable/disable a page without deleting it.

### 2.2 Section Management (The "Page Builder")
*   **Bilingual Architecture:** Each FR section is linked to a corresponding EN section.
*   **Supported Section Types:**
    *   `Hero`: Main banner with background image, heading, subheading, and CTA.
    *   `Intro`: Simple introductory text.
    *   `Features`: List of features or services (bullet points).
    *   `Expertise`: Image + text block to showcase skills.
    *   `Why Us`: Unique Selling Points (USP).
    *   `Service`: Dedicated block for a specific service.
    *   `Contact`: Formatted contact information.
    *   `CTA`: Isolated Call-to-Action.
    *   `Text`: Standard rich text block.
*   **Ordering:** Display order management (`order_index`).
*   **Normalization Tool:** Script (`/admin/normalize-sections`) to resynchronize FR/EN indexes in case of mismatch.
*   **Visual Customization:**
    *   Background image upload.
    *   Hex background color.
    *   Customizable button text and link.

### 2.3 Media Library (Images)
*   **Secure Upload:** Extension verification (.jpg, .png, .webp, .gif).
*   **Sanitization:** Automatic file renaming to prevent conflicts and vulnerabilities (UUID + secure name).
*   **Analysis:** Automatic detection of dimensions (Width/Height) and file size.
*   **Deletion:** Removal of the file from disk and the DB entry.

## 3. Progressive Web App (PWA)

*   **Dynamic Manifest:** The `/manifest.json` file is generated on the fly from DB settings.
*   **Admin Configuration:**
    *   App Name (Long/Short).
    *   Colors (Theme, Background).
    *   Display Mode (Standalone, Minimal-UI, etc.).
    *   Icons (192x192, 512x512).
*   **Installation:** Native support for mobile and desktop installation ("Add to Home Screen").

## 4. Security & Compliance

*   **Admin Authentication:**
    *   Secure session protection.
    *   Password hashing via **Argon2** (via Werkzeug).
    *   Secure initial creation via Environment Variables (`ADMIN_USERNAME`, `ADMIN_PASSWORD`).
*   **CSRF Protection:** Mandatory `Flask-WTF` tokens on all forms (POST).
*   **Content Security Policy (CSP):** Strict configuration via `Flask-Talisman`.
    *   Restriction of script sources (Self + CDN Tailwind).
    *   XSS Protection.
*   **Secure Cookies:** `HttpOnly`, `Secure` (if HTTPS), `SameSite=Lax` flags.
*   **Uploads:** File size limit (16MB).

## 5. SEO & Marketing

*   **XML Sitemap:** Automatic generation at `/sitemap.xml` including all active pages with `lastmod`.
*   **Robots.txt:**
    *   Blocks harmful scrapers (Ahrefs, Semrush, MJ12bot).
    *   Explicitly allows ethical AI bots (GPTBot, ClaudeBot) for AI referencing.
    *   Hides admin (`/admin/*`).
*   **Social Graph:**
    *   Default `og:image` management.
    *   Configurable social links (Facebook, Instagram, LinkedIn, WhatsApp).
*   **Tracking:** Google Analytics ID injection.

## 6. Deployment & Maintenance

*   **Robust Initialization (`init_db.py`):**
    *   Manual schema migration system (Checks for missing columns at startup).
    *   Automatic population of default content if DB is empty.
*   **Reverse Proxy:** Designed to run behind Nginx (`X-Forwarded-Proto` handling).
*   **Containerization:** Docker-ready (via `deploy.sh` and standard structure).

---
© MOA Digital Agency (myoneart.com) - Author: Aisance KALONJI
