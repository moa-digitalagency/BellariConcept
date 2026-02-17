![Python Version](https://img.shields.io/badge/Python-3.11%2B-blue) ![Framework](https://img.shields.io/badge/Framework-Flask%203.0-green) ![Database](https://img.shields.io/badge/Database-PostgreSQL-orange) ![Status](https://img.shields.io/badge/Status-Proprietary-red) ![License](https://img.shields.io/badge/License-MOA%20Private-red) ![Owner](https://img.shields.io/badge/Owner-MOA%20Digital%20Agency-purple)

# Bellari Concept - User Guide (Admin)

> **STRICTLY CONFIDENTIAL DOCUMENT**
>
> This guide is intended for the administrators of the Bellari Concept website.

This guide describes how to use the administration interface to manage site content, images, and settings.

## 1. Access to Administration

### Login
1.  Access the URL: `https://your-site.com/admin/login`
2.  Enter your credentials (Username and Password).
3.  Click on **"Sign In"**.

### Dashboard
Once connected, the Dashboard displays:
*   An overview of existing **Pages**.
*   The latest **Images** uploaded.
*   Quick links to management tools (`Settings`, `Logout`).

---

## 2. Page and Content Management

The site is structured into **Pages** (Home, About...), composed of **Sections** (content blocks).

### Edit a Page
1.  Go to the **Pages** menu.
2.  Click the **"Edit"** button (pencil icon) next to the desired page.
3.  **Metadata (SEO):**
    *   Modify the **Title** and **Meta Description** (crucial for Google).
    *   **"Active"** Checkbox: Uncheck to hide the page (404 error).

### Manage Sections (The Core of the Site)
The editor displays sections in bilingual pairs.
*   **Left:** **FR** Version.
*   **Right:** **EN** Version.
*   **Note:** These two blocks work together and share the same position.

#### Add a New Section
1.  At the bottom of the page, find the **"Add a new section (FR & EN)"** form.
2.  Select the **Section Type** (Hero, Text, Service, Features, Contact).
3.  Fill in the content for **French** and **English**.
4.  Click **"Create Sections"**.

#### Edit an Existing Section
1.  Locate the block to modify.
2.  Change texts, links, or images.
3.  Click **"Update"** to save *this specific block*.

#### Delete a Section
1.  Click **"Delete"** (red) at the bottom of the block.
    *   *Warning:* Always delete the EN version if you delete the FR to keep symmetry.

---

## 3. Image Management (Media Library)

### Add an Image
1.  Go to the **Images** menu.
2.  Use the **Drag & Drop** area or click to select a file (JPG, PNG, WEBP).
3.  The image appears in the list with its URL.

### Use an Image
1.  Copy the **URL** displayed under the image (e.g., `/static/uploads/image.jpg`).
2.  In the section editor, paste the URL into the **"Image URL"** or **"Background Image"** field.

---

## 4. Site Settings & PWA

The **Settings** menu (`/admin/settings`) allows you to configure the site's identity.

### Visual Identity
*   **Logo / Favicon:** Change the branding image.
*   **Site Name (FR/EN):** Appears in the browser tab.

### Progressive Web App (PWA)
Transform the site into a mobile application:
*   **Enable PWA:** Check to activate.
*   **App Name / Icon / Colors:** Customize the appearance on the customer's phone.

---

## 5. Troubleshooting

### Synchronization Issue
If the French text no longer corresponds to the English (offset):
1.  Go to the **Dashboard**.
2.  Click the **"Normalize Sections"** button.
3.  This script automatically realigns all content.
