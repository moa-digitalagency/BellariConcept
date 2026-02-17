![Python Version](https://img.shields.io/badge/Python-3.11%2B-blue) ![Framework](https://img.shields.io/badge/Framework-Flask%203.0-green) ![Database](https://img.shields.io/badge/Database-PostgreSQL-orange) ![Status](https://img.shields.io/badge/Status-Proprietary-red) ![License](https://img.shields.io/badge/License-MOA%20Private-red) ![Owner](https://img.shields.io/badge/Owner-MOA%20Digital%20Agency-purple)

# Bellari Concept - Architecture Technique

> **DOCUMENT STRICTEMENT CONFIDENTIEL**
>
> Ce logiciel est la propriété exclusive de **MOA Digital Agency**. Toute reproduction ou distribution non autorisée est strictement interdite.

Ce document détaille l'architecture logicielle, la structure de la base de données et les flux de sécurité de l'application Bellari Concept.

## 1. Vue d'Ensemble

L'application suit une architecture monolithique robuste, optimisée pour le déploiement sur VPS avec une séparation claire entre le serveur web, le serveur d'application et la base de données.

```mermaid
graph TD
    Client["Client (Browser/PWA)"]
    Nginx["Nginx (Reverse Proxy / SSL)"]
    Gunicorn["Gunicorn (WSGI Server)"]
    Flask["Flask App (Bellari Concept)"]
    DB[("PostgreSQL (Données)")]
    FS["File System (Images/Uploads)"]

    Client -->|HTTPS| Nginx
    Nginx -->|Proxy Pass| Gunicorn
    Nginx -->|Serve Static| FS
    Gunicorn -->|WSGI| Flask
    Flask -->|SQLAlchemy| DB
    Flask -->|Read/Write| FS
```

---

## 2. Stack Technologique

### Backend
*   **Langage :** Python 3.11+
*   **Framework Web :** Flask 3.0.0
*   **ORM :** SQLAlchemy (via `flask-sqlalchemy`)
*   **Sécurité :**
    *   `Werkzeug` (Hachage Argon2 pour les mots de passe)
    *   `Flask-Login` (Gestion de session utilisateur sécurisée)
    *   `Flask-WTF` (Protection CSRF globale)
    *   `Flask-Talisman` (Content Security Policy & Force HTTPS)

### Frontend
*   **Templating :** Jinja2 (Rendu côté serveur avec injection de contexte)
*   **CSS Framework :** TailwindCSS (via CDN pour performance et itération rapide)
*   **JavaScript :** Vanilla JS (ES6+) pour l'interactivité PWA et UI.

### Infrastructure & Déploiement
*   **Base de Données :** PostgreSQL (Production) / SQLite (Développement/Fallback)
*   **Serveur d'Application :** Gunicorn (WSGI Production)
*   **Serveur Web :** Nginx (Reverse Proxy, SSL Termination)
*   **Containerisation :** Compatible Docker (optionnel), déploiement standard via `deploy.sh`.

---

## 3. Modèle de Données (Entités)

Le schéma de base de données est conçu pour offrir une flexibilité totale au CMS tout en maintenant l'intégrité des données bilingues.

```mermaid
classDiagram
    class User {
        +Integer id
        +String username
        +String password_hash
        +DateTime created_at
    }

    class Page {
        +Integer id
        +String slug
        +String title
        +String meta_description
        +Boolean is_active
        +DateTime created_at
        +DateTime updated_at
    }

    class Section {
        +Integer id
        +Integer page_id
        +String section_type
        +String language_code
        +Integer order_index
        +String heading
        +String subheading
        +Text content
        +String button_text
        +String button_link
        +String image_url
        +String background_image
        +Boolean is_active
    }

    class Image {
        +Integer id
        +String filename
        +String original_filename
        +String alt_text
        +Integer file_size
        +Integer width
        +Integer height
        +DateTime uploaded_at
    }

    class SiteSettings {
        +Integer id
        +String key
        +Text value
        +String description
        +DateTime updated_at
    }

    Page "1" -- "*" Section : contient
```

### Relations Clés
*   **Page -> Section :** Une `Page` (ex: "Accueil") contient plusieurs `Section`s ordonnées.
*   **Pairing FR/EN :** La synchronisation entre les contenus Français et Anglais est gérée logiquement par l'application via `order_index` et `section_type`. Le script `normalize_sections.py` assure l'intégrité de cet alignement.

---

## 4. Flux de Sécurité & Application

### Cycle de Vie d'une Requête (Request Lifecycle)

1.  **Entrée Sécurisée :** Nginx termine la connexion SSL et transmet la requête à Gunicorn.
2.  **Middleware de Sécurité (`Talisman`) :**
    *   Force HTTPS.
    *   Applique les en-têtes de sécurité stricts (HSTS, X-Frame-Options).
    *   Applique une Content Security Policy (CSP) pour prévenir les XSS.
3.  **Validation CSRF :** `Flask-WTF` valide le token CSRF pour toutes les méthodes POST/PUT/DELETE.
4.  **Authentification :** `Flask-Login` vérifie le cookie de session (Secure, HttpOnly, SameSite=Lax).
5.  **Logique Métier & Rendu :**
    *   Les vues interrogent la DB.
    *   Le processeur de contexte (`context_processor`) injecte les configurations globales (`SiteSettings`).
    *   Jinja2 génère le HTML final.

### Initialisation Robuste (`init_db.py`)
Le système dispose d'un mécanisme d'auto-réparation au démarrage :
*   Vérification et création du schéma de base de données.
*   Création sécurisée du compte Admin via variables d'environnement (`ADMIN_USERNAME`, `ADMIN_PASSWORD`).
*   Population du contenu par défaut si la base est vide.
