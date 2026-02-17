[ 🇫🇷 Français ] | [ 🇬🇧 English ](BellariConcept_Technical_Architecture_en.md)

# ⚙️ Bellari Concept - Architecture Technique
**Date :** 2025
**Auteur :** Aisance KALONJI (MOA Digital Agency)
**Statut :** Confidentiel / Propriétaire

Ce document détaille l'architecture logicielle, le modèle de données et les mécanismes de sécurité de la plateforme.

---

## 1. Stack Technologique

### Backend
*   **Langage :** Python 3.11+
*   **Framework Web :** Flask 3.x
*   **ORM :** SQLAlchemy (Abstention SQL pour compatibilité SQLite/Postgres)
*   **Authentification :** Flask-Login + Argon2 (via Werkzeug)
*   **Formulaires :** Flask-WTF

### Frontend
*   **Templating :** Jinja2 (Rendu côté serveur)
*   **CSS :** TailwindCSS (v3 via CDN)
*   **Animations :** LottieFiles (via CDN)
*   **Icons :** FontAwesome (via CDN)

### Infrastructure (Production)
*   **OS :** Ubuntu LTS (Recommandé)
*   **Serveur Web :** Nginx (Proxy Inverse, Terminaison SSL)
*   **Serveur WSGI :** Gunicorn (Workers synchrones)
*   **Base de Données :** PostgreSQL (Production) / SQLite (Développement)

---

## 2. Modèle de Données (Schéma BDD)

L'application repose sur un modèle relationnel optimisé pour la flexibilité du CMS.

### `User` (Administrateurs)
*   `id`: Integer (PK)
*   `username`: String(80) (Unique)
*   `password_hash`: String(255) (Argon2)

### `Page` (Structure du Site)
*   `id`: Integer (PK)
*   `slug`: String(100) (Unique, ex: 'home', 'about')
*   `title`: String(200) (SEO)
*   `meta_description`: String(300) (SEO)
*   `is_active`: Boolean
*   `sections`: Relationship (One-to-Many vers Section)

### `Section` (Blocs de Contenu Polymorphes)
*   `id`: Integer (PK)
*   `page_id`: FK vers Page
*   `section_type`: String(50) ('hero', 'intro', 'features', etc.)
*   `language_code`: String(5) ('fr' ou 'en')
*   `order_index`: Integer (Position dans la page)
*   `heading`, `subheading`, `content`: Champs de texte
*   `image_url`, `background_image`: Liens vers médias
*   `background_color`: String(20) (Hex)

### `Image` (Médiathèque)
*   `id`: Integer (PK)
*   `filename`: String(300) (Nom sécurisé sur disque)
*   `original_filename`: String(300)
*   `file_size`: Integer (Bytes)
*   `width`, `height`: Integer (Dimensions)

### `SiteSettings` (Configuration Dynamique)
*   `key`: String(100) (Unique, ex: 'site_logo', 'pwa_enabled')
*   `value`: Text
*   Stocke la configuration PWA, les liens sociaux, et les clés API.

---

## 3. Sécurité & Conformité

### 3.1 Content Security Policy (CSP)
Mise en œuvre via `Flask-Talisman`.
```python
csp = {
    'default-src': '\'self\'',
    'style-src': ['\'self\'', '\'unsafe-inline\'', 'https://fonts.googleapis.com'],
    'script-src': ['\'self\'', '\'unsafe-inline\'', 'https://cdn.tailwindcss.com'],
    'img-src': ['\'self\'', 'data:', 'https:'],
    ...
}
```
*   Protection contre les attaques XSS.
*   Force HTTPS en production.

### 3.2 Protection CSRF
`CSRFProtect(app)` est activé globalement.
*   Chaque formulaire POST doit inclure un `<input type="hidden" name="csrf_token">`.
*   Les requêtes AJAX doivent inclure le header `X-CSRFToken`.

### 3.3 Gestion des Uploads
*   Nettoyage des noms de fichiers via `werkzeug.utils.secure_filename`.
*   Préfixe aléatoire (UUID) pour éviter les collisions.
*   Vérification stricte des extensions (`.png`, `.jpg`, `.webp`).

---

## 4. Stratégie de Déploiement

### Migration de Base de Données (`init_db.py`)
Contrairement à Alembic qui peut être fragile sur de petits VPS sans CI/CD complexe, ce projet utilise un système de migration manuel robuste ("Smart Init") :
1.  Vérifie l'existence des tables.
2.  Inspecte les colonnes existantes.
3.  Ajoute les colonnes manquantes à la volée (`ALTER TABLE`).
4.  Initialise les données par défaut (Pages, Admin) si la table est vide.

### Scripts Utilitaires
*   `deploy.sh`: Wizard interactif pour configurer l'environnement (`.env`), installer les dépendances et initialiser la BDD.
*   `verify_deployment.py`: Vérifie que les fichiers statiques (CSS, JS, Images) sont accessibles et que la BDD est connectée avant le lancement.

---
© MOA Digital Agency (myoneart.com) - Auteur : Aisance KALONJI
