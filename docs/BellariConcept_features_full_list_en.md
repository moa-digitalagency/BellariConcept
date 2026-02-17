> **© MOA Digital Agency (myoneart.com) - Author: Aisance KALONJI**
> *This code is the exclusive property of MOA Digital Agency. Internal use only. Any unauthorized reproduction or distribution is strictly prohibited.*

[Passer à la version Française](./BellariConcept_features_full_list.md)

# Full Feature List - Bellari Concept

## 1. Administration & Security
*   **Strong Authentication:** Secure login with Argon2 hashing (`werkzeug.security`).
*   **CSRF Protection:** Global anti-CSRF tokens via `Flask-WTF` for all forms and AJAX requests.
*   **Content Security Policy (CSP):** Strict configuration via `Flask-Talisman` to prevent XSS attacks.
*   **Secure Cookies:** `HttpOnly`, `Secure`, and `SameSite=Lax` attributes.
*   **Admin Dashboard:** Overview of pages, recent images, and quick access to settings.

## 2. CMS & Content Management
*   **Bilingual Editing (FR/EN):** Natively bilingual content architecture.
*   **Page Management:** Create, edit meta-data (title, description), and toggle page visibility.
*   **Modular Sections:**
    *   Add, edit, delete, and reorder (logical drag & drop via `order_index`).
    *   Various section types: Hero, Text, Services, Portfolio, Contact, etc.
    *   Synchronization of FR/EN section pairs via `normalize_sections.py`.
    *   **Content Editor:** Fields for headings, subheadings, rich content, call-to-action buttons, and links.

## 3. Media Management
*   **Secure Upload:** Extension verification (`png`, `jpg`, `webp`, etc.) and filename sanitization.
*   **Optimization:** Resizing and processing via `Pillow` (PIL).
*   **Image Gallery:** Centralized library to reuse images across sections.
*   **ALT Attributes:** Management of alternative text for accessibility and SEO.

## 4. Dynamic Configuration (Site Settings)
*   **Visual Identity:** Change logo, favicon, and PWA icon from the admin panel.
*   **Social Networks:** Configuration of Facebook, Instagram, LinkedIn, WhatsApp links.
*   **Global SEO:** Default keywords, OG (Open Graph) Image, Google Analytics ID.

## 5. Progressive Web App (PWA)
*   **Installation:** Configurable dynamic `/manifest.json`.
*   **Customization:** App name, theme colors, icons, display mode (standalone).
*   **Offline Support:** Prepared for service worker (configurable).

## 6. SEO & Performance
*   **XML Sitemap:** Automatic generation at `/sitemap.xml` with update dates.
*   **Robots.txt:** Dynamic management of indexing rules.
*   **Meta Tags:** Fine-grained management of meta tags for each page.
*   **Optimized Assets:** Use of TailwindCSS via CDN for fast loading.

## 7. Deployment & Maintenance
*   **Automated Scripts:** `deploy.sh` and `verify_deployment.py` for reliable production releases.
*   **DB Migration:** Robust manual migration system (`init_db.py`) adapted for VPS.
*   **Logs & Errors:** Custom error pages (404, 500) with Lottie animations.
