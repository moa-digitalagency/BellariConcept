# Bellari Concept - Website CMS

[English Version](#english-version) | [Version Française](#version-française)

---

## English Version

### 🎨 Project Overview

A modern, professional website with full Content Management System (CMS) for Bellari Concept - a construction and renovation company based in Marrakech, Morocco. This project features complete multilingual support (French/English), professional images, and an intuitive admin panel for content management.

### ✨ Key Features

- **🌍 Multilingual Support**: Full French and English translation support with easy language switching
- **📱 Mobile Responsive**: Optimized design for all devices (desktop, tablet, mobile)
- **🎛️ Complete CMS**: Manage all website content without touching code
- **🖼️ Image Management**: Upload, organize, and manage images with automatic optimization
- **🔐 Secure Admin**: Password-protected admin panel with user authentication
- **🎨 Modern Design**: Clean, professional interface with smooth animations
- **🔍 SEO Optimized**: Built-in SEO tools with customizable meta tags and Open Graph support
- **🚀 Fast Performance**: Lightweight and optimized for speed
- **⚙️ Customizable Settings**: Logo, social media links, and SEO settings all configurable via admin panel

### 🛠️ Technology Stack

- **Backend**: Python 3.11, Flask, Flask-SQLAlchemy, Flask-Login
- **Frontend**: HTML5, Tailwind CSS, Vanilla JavaScript
- **Database**: PostgreSQL (Neon)
- **Image Processing**: Pillow
- **Deployment**: Gunicorn

### 📋 Prerequisites

- Python 3.11+
- PostgreSQL database
- pip or uv package manager

### 🚀 Quick Start

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd bellari-concept
   ```

2. **Install dependencies**
   ```bash
   uv sync
   # or
   pip install -r requirements.txt
   ```

3. **Set environment variables**
   ```bash
   export DATABASE_URL="postgresql://user:password@localhost/bellari_concept"
   export SESSION_SECRET="your-secret-key-here"
   ```

4. **Initialize the database**
   ```bash
   python init_database.py
   ```

5. **Run the server**
   ```bash
   gunicorn --bind 0.0.0.0:5000 --reuse-port --reload main:app
   # or for development
   python app.py
   ```

6. **Access the website**
   - Website: http://localhost:5000
   - Admin Panel: http://localhost:5000/admin/login
   - Default credentials: username=`admin`, password=`admin123`
   - **⚠️ IMPORTANT**: Change the default password immediately after first login!

### 📚 Project Structure

```
bellari-concept/
├── app.py                 # Main Flask application
├── main.py               # Application entry point
├── init_database.py      # Database initialization script
├── templates/            # HTML templates
│   ├── base.html        # Main layout template
│   ├── index.html       # Homepage
│   ├── about.html       # About page
│   ├── services.html    # Services page
│   ├── portfolio.html   # Portfolio page
│   ├── contact.html     # Contact page
│   └── admin/           # Admin panel templates
│       ├── base.html
│       ├── dashboard.html
│       ├── pages.html
│       ├── edit_page.html
│       ├── images.html
│       ├── settings.html
│       └── login.html
├── static/              # Static assets
│   ├── uploads/        # User-uploaded images
│   ├── images/         # Stock images
│   └── logo.png        # Site logo
├── README.md           # This file
└── CHANGELOG.md        # Version history
```

### 🎯 Database Models

1. **User** - Admin user accounts
2. **Page** - Website pages (slug, title, meta_description)
3. **Section** - Page content sections (multilingual, with images and buttons)
4. **Image** - Uploaded images with metadata
5. **SiteSettings** - Global site configuration (logo, SEO, social media)

### 📖 User Guide

#### Managing Content

1. **Login to Admin Panel**
   - Navigate to `/admin/login`
   - Enter your credentials

2. **Edit Page Content**
   - Go to "Pages & Content"
   - Select a page to edit
   - Modify sections in both French and English
   - Click "Save" to apply changes

3. **Manage Images**
   - Go to "Image Gallery"
   - Upload new images (drag & drop supported)
   - View image details (resolution, file size)
   - Delete unused images

4. **Configure Settings**
   - Go to "Settings & SEO"
   - Upload custom logo
   - Set SEO meta tags
   - Configure social media links
   - Set up Google Analytics

#### Multilingual Content

- Each page section has both French and English versions
- Visitors can switch language using the FR/EN toggle button
- Language preference is saved in session
- Admin panel also supports both languages

### 🔒 Security Notes

- Default admin password should be changed immediately
- Database initialization route is disabled by default
- All admin routes require authentication
- Session secret should be kept confidential
- Use HTTPS in production

### 🌐 Deployment

The project is configured for deployment on Replit or any cloud platform:

1. Set environment variables:
   - `DATABASE_URL` - PostgreSQL connection string
   - `SESSION_SECRET` - Flask secret key

2. Run database initialization once:
   ```bash
   python init_database.py
   ```

3. Start the server:
   ```bash
   gunicorn --bind 0.0.0.0:5000 main:app
   ```

### 📝 Environment Variables

- `DATABASE_URL` - PostgreSQL database connection URL
- `SESSION_SECRET` - Flask session secret key (automatically generated in Replit)
- `ADMIN_INIT_ALLOWED` - Enable/disable database initialization endpoint (default: false)

### 🤝 Contributing

This is a private project for Bellari Concept. For questions or support, contact the development team.

### 📄 License

© 2025 Bellari Concept. All rights reserved.

---

## Version Française

### 🎨 Aperçu du Projet

Un site web moderne et professionnel avec système de gestion de contenu (CMS) complet pour Bellari Concept - une entreprise de construction et rénovation basée à Marrakech, Maroc. Ce projet offre un support multilingue complet (français/anglais), des images professionnelles et un panneau d'administration intuitif.

### ✨ Fonctionnalités Principales

- **🌍 Support Multilingue**: Support complet français et anglais avec changement de langue facile
- **📱 Responsive Mobile**: Design optimisé pour tous les appareils (ordinateur, tablette, mobile)
- **🎛️ CMS Complet**: Gérez tout le contenu du site sans toucher au code
- **🖼️ Gestion d'Images**: Téléchargez, organisez et gérez les images avec optimisation automatique
- **🔐 Admin Sécurisé**: Panneau d'administration protégé par mot de passe
- **🎨 Design Moderne**: Interface propre et professionnelle avec animations fluides
- **🔍 Optimisé SEO**: Outils SEO intégrés avec balises meta et support Open Graph personnalisables
- **🚀 Performance Rapide**: Léger et optimisé pour la vitesse
- **⚙️ Paramètres Personnalisables**: Logo, liens réseaux sociaux et paramètres SEO configurables via l'admin

### 🛠️ Stack Technologique

- **Backend**: Python 3.11, Flask, Flask-SQLAlchemy, Flask-Login
- **Frontend**: HTML5, Tailwind CSS, JavaScript Vanilla
- **Base de données**: PostgreSQL (Neon)
- **Traitement d'images**: Pillow
- **Déploiement**: Gunicorn

### 📋 Prérequis

- Python 3.11+
- Base de données PostgreSQL
- Gestionnaire de paquets pip ou uv

### 🚀 Démarrage Rapide

1. **Cloner le dépôt**
   ```bash
   git clone <url-de-votre-dépôt>
   cd bellari-concept
   ```

2. **Installer les dépendances**
   ```bash
   uv sync
   # ou
   pip install -r requirements.txt
   ```

3. **Définir les variables d'environnement**
   ```bash
   export DATABASE_URL="postgresql://user:password@localhost/bellari_concept"
   export SESSION_SECRET="votre-clé-secrète-ici"
   ```

4. **Initialiser la base de données**
   ```bash
   python init_database.py
   ```

5. **Lancer le serveur**
   ```bash
   gunicorn --bind 0.0.0.0:5000 --reuse-port --reload main:app
   # ou pour le développement
   python app.py
   ```

6. **Accéder au site**
   - Site web: http://localhost:5000
   - Panneau Admin: http://localhost:5000/admin/login
   - Identifiants par défaut: username=`admin`, password=`admin123`
   - **⚠️ IMPORTANT**: Changez le mot de passe par défaut immédiatement après la première connexion!

### 📖 Guide d'Utilisation

#### Gestion du Contenu

1. **Connexion au Panneau Admin**
   - Naviguer vers `/admin/login`
   - Entrer vos identifiants

2. **Éditer le Contenu des Pages**
   - Aller dans "Pages & Content"
   - Sélectionner une page à éditer
   - Modifier les sections en français et en anglais
   - Cliquer sur "Enregistrer" pour appliquer les changements

3. **Gérer les Images**
   - Aller dans "Image Gallery"
   - Télécharger de nouvelles images (glisser-déposer supporté)
   - Voir les détails des images (résolution, taille du fichier)
   - Supprimer les images inutilisées

4. **Configurer les Paramètres**
   - Aller dans "Settings & SEO"
   - Télécharger un logo personnalisé
   - Définir les balises meta SEO
   - Configurer les liens réseaux sociaux
   - Configurer Google Analytics

#### Contenu Multilingue

- Chaque section de page a des versions française et anglaise
- Les visiteurs peuvent changer de langue avec le bouton FR/EN
- La préférence de langue est sauvegardée en session
- Le panneau admin supporte également les deux langues

### 🔒 Notes de Sécurité

- Le mot de passe admin par défaut doit être changé immédiatement
- La route d'initialisation de la base de données est désactivée par défaut
- Toutes les routes admin nécessitent une authentification
- Le secret de session doit rester confidentiel
- Utiliser HTTPS en production

### 🌐 Déploiement

Le projet est configuré pour le déploiement sur Replit ou toute plateforme cloud:

1. Définir les variables d'environnement:
   - `DATABASE_URL` - Chaîne de connexion PostgreSQL
   - `SESSION_SECRET` - Clé secrète Flask

2. Exécuter l'initialisation de la base de données une fois:
   ```bash
   python init_database.py
   ```

3. Démarrer le serveur:
   ```bash
   gunicorn --bind 0.0.0.0:5000 main:app
   ```

### 📝 Variables d'Environnement

- `DATABASE_URL` - URL de connexion à la base de données PostgreSQL
- `SESSION_SECRET` - Clé secrète de session Flask (générée automatiquement dans Replit)
- `ADMIN_INIT_ALLOWED` - Activer/désactiver l'endpoint d'initialisation de la base de données (défaut: false)

### 🤝 Contribution

Ceci est un projet privé pour Bellari Concept. Pour questions ou support, contactez l'équipe de développement.

### 📄 Licence

© 2025 Bellari Concept. Tous droits réservés.
