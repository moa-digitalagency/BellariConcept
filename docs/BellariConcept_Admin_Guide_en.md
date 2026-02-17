[ 🇫🇷 Français ](BellariConcept_Admin_Guide.md) | [ 🇬🇧 English ]

# 📖 Bellari Concept - Admin Guide
**Date:** 2025
**Author:** Aisance KALONJI (MOA Digital Agency)
**Usage:** Internal & Final Client

This guide explains how to use the administration panel to manage content, media, and site configuration.

---

## 1. Access and Login

The administration interface is secured and only accessible via authentication.

*   **URL:** `/admin` (or `/admin/login`)
*   **Credentials:** Defined during installation (or via `ADMIN_USERNAME` / `ADMIN_PASSWORD` environment variables).

> **Security Note:** After 3 failed attempts, access may be temporarily limited depending on the server configuration (Fail2Ban recommended in production).

---

## 2. Dashboard

The admin home page (`/admin`) offers an overview:
*   **Active Pages:** Quick list of site pages.
*   **Recent Images:** Preview of recently uploaded files.
*   **Quick Actions:** Links to settings and the media library.
*   **Tools:** "Normalize Sections" link to fix FR/EN sync issues.

---

## 3. Content Management (Pages & Sections)

### 3.1 Edit a Page
Click on a page (e.g., "Home") to enter the editor.
*   **SEO Parameters:** Modify the `Title` (Title Tag) and `Meta Description` (Appears in Google).
*   **Status:** Check/Uncheck "Active" to publish or hide the page.

### 3.2 Manage Sections (The "Builder")
Content is divided into blocks called "Sections". Each section exists in a pair (French / English).

*   **Add a Section:**
    1.  Go to the bottom of the page "Add a new section".
    2.  Choose the **Type** (Hero, Features, Text, Contact...).
    3.  Fill in the content for both FR and EN simultaneously (recommended via "Create Both").
*   **Edit a Section:**
    *   Modify the text, button links, or background image.
    *   **Background Image:** Copy an image URL from the Media Library and paste it into the `Background Image` field.
*   **Reorder:** Modify the `Order` number and save. (Tip: Use the "Normalize" tool after major changes).

---

## 4. Media Library (Images)

Accessible via the "Images" menu.

*   **Upload:** Drag-and-drop or select files (.jpg, .png, .webp).
*   **Optimization:** The system automatically renames files for security.
*   **Usage:**
    1.  Copy the image URL ("Copy Link" button).
    2.  Paste this URL into the `Image URL` or `Background Image` fields of your sections.

---

## 5. Site Settings & PWA

Accessible via the "Settings" menu.

### 5.1 Visual Identity
*   **Site Logo:** Change the main logo (PNG/SVG recommended).
*   **Favicon:** The browser tab icon.

### 5.2 Progressive Web App (PWA)
Configure the app's appearance when installed on mobile.
*   **Enable PWA:** Enable/Disable the manifest.
*   **App Name:** The name under the icon on the phone home screen.
*   **Theme:** Status bar color (Hexadecimal).
*   **PWA Icon:** Must be a square image (512x512 recommended).

### 5.3 Social Media
Fill in the links to your profiles (Facebook, Instagram, LinkedIn). They will automatically appear in the footer.

---
© MOA Digital Agency (myoneart.com) - Author: Aisance KALONJI
