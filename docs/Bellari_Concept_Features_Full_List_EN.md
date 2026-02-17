![Python Version](https://img.shields.io/badge/Python-3.11%2B-blue) ![Framework](https://img.shields.io/badge/Framework-Flask%203.0-green) ![Database](https://img.shields.io/badge/Database-PostgreSQL-orange) ![Status](https://img.shields.io/badge/Status-Proprietary-red) ![License](https://img.shields.io/badge/License-MOA%20Private-red) ![Owner](https://img.shields.io/badge/Owner-MOA%20Digital%20Agency-purple)

# Bellari Concept - Full Feature List

> **STRICTLY CONFIDENTIAL DOCUMENT**
>
> This document is the exclusive property of **MOA Digital Agency**.

This document lists all the technical and business features of the Bellari Concept platform.

## 1. Content Management (Bilingual CMS)

The core of the system is a bespoke CMS allowing fine-grained content management in French and English.

*   **Dynamic Pages:** Management of main pages (`Home`, `About`, `Services`, `Portfolio`, `Contact`).
*   **Section System:** Each page is composed of modular blocks.
    *   **Hero:** Main banner with background image, title, subtitle, and call-to-action (CTA) button.
    *   **Intro:** Rich introductory text.
    *   **Features:** List of key points or quick services.
    *   **Service:** Detailed description of an offering.
    *   **Contact:** Structured contact information.
*   **FR/EN Synchronization:**
    *   Simultaneous creation of FR and EN versions of a section.
    *   Automatic alignment via `normalize_sections.py`.
    *   Visual parity indicator in the admin panel.

## 2. Administration & Security

Protected admin interface (`/admin`) for autonomous site management.

*   **Strong Authentication:**
    *   Password hashing via **Argon2** (industry standard).
    *   Protection against brute-force attacks (via response delays).
    *   Secure session (Cookies `HttpOnly`, `Secure`, `SameSite=Lax`).
*   **Media Library:**
    *   Secure image upload (extension verification).
    *   Unique file renaming (UUID) to prevent collisions.
    *   Asset visualization and deletion.
*   **Site Settings (SiteSettings):**
    *   Logo and Favicon modification on the fly.
    *   Social link configuration (Facebook, Instagram, LinkedIn).
    *   Google Analytics ID injection.

## 3. Progressive Web App (PWA)

The site is an installable PWA, offering an experience close to a native application.

*   **Dynamic Manifest (`/manifest.json`):** Generated from the database (configurable name, colors, icons in admin).
*   **Installation:** Installation prompt on mobile and desktop.
*   **Standalone Mode:** The application launches without the browser URL bar.
*   **Service Worker:** Caches static assets for instant loading.

## 4. SEO & Technical Performance

The architecture is optimized for natural referencing and speed.

*   **Technical SEO:**
    *   Dynamically generated `sitemap.xml` for all active pages.
    *   Configurable `robots.txt` (blocks unwanted bots, allows Google/GPTBot).
    *   Editable Meta tags (Title, Description) for each page.
    *   OpenGraph support for social media sharing.
*   **Performance:**
    *   Images served via Nginx with cache (`Expires` headers).
    *   Minified CSS (Tailwind via CDN).
    *   Database indexed on slugs and IDs.

## 5. Compliance & Advanced Security

*   **CSRF Protection:** All forms include a unique anti-forgery token (`Flask-WTF`).
*   **Content Security Policy (CSP):** Strict headers blocking unauthorized scripts (`Flask-Talisman`).
*   **Strict Transport Security (HSTS):** Forces the browser to use only HTTPS.
*   **Sanitization:** User inputs are cleaned to prevent SQL and XSS injections.
