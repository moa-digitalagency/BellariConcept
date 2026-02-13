# Bellari Concept CMS

![Python Version](https://img.shields.io/badge/python-3.11%2B-blue.svg)
![Flask](https://img.shields.io/badge/flask-3.0-green.svg)
![Status](https://img.shields.io/badge/status-production-success.svg)
![License](https://img.shields.io/badge/license-Private-red.svg)

> **Une plateforme CMS moderne, sécurisée et performante conçue sur mesure pour l'agence d'architecture et de design Bellari Concept.**

---

## 📖 Table des Matières

- [Aperçu du Projet](#-aperçu-du-projet)
- [Fonctionnalités Clés](#-fonctionnalités-clés)
- [Stack Technique](#-stack-technique)
- [Documentation Complète](#-documentation-complète)
- [Installation Rapide](#-installation-rapide)
- [Structure du Projet](#-structure-du-projet)
- [Crédits](#-crédits)

---

## 🔭 Aperçu du Projet

Bellari Concept CMS est une application web monolithique développée en Python/Flask. Elle offre une expérience utilisateur fluide (SPA-like) grâce à une gestion intelligente du cache et des transitions, tout en conservant la robustesse d'un backend traditionnel.

Le cœur du système est un **CMS bilingue (FR/EN)** permettant une gestion fine du contenu (texte, images, SEO) sans aucune compétence technique, le tout sécurisé par des standards industriels (CSP, CSRF, Argon2).

---

## ✨ Fonctionnalités Clés

*   **🌍 Bilinguisme Natif :** Gestion symétrique des contenus FR/EN avec bascule instantanée.
*   **📱 Progressive Web App (PWA) :** Installable sur mobile, fonctionne hors-ligne (partiellement), manifest dynamique.
*   **🎨 Éditeur de Contenu Visuel :** Interface d'administration intuitive pour gérer les pages et les sections.
*   **🖼️ Médiathèque Optimisée :** Upload, redimensionnement et compression automatique des images (Pillow).
*   **🔒 Sécurité Renforcée :** Protection CSRF globale, Content Security Policy (Talisman), Hachage Argon2.
*   **🚀 Performance :** Assets statiques optimisés, base de données relationnelle structurée.

---

## 🛠 Stack Technique

| Composant | Technologie |
| :--- | :--- |
| **Backend** | Python 3.11, Flask 3.0 |
| **Base de Données** | PostgreSQL (Prod) / SQLite (Dev), SQLAlchemy |
| **Frontend** | Jinja2, Tailwind CSS (CDN), Vanilla JS |
| **Serveur** | Gunicorn (WSGI) |
| **Sécurité** | Flask-Talisman (CSP), Flask-WTF (CSRF), Werkzeug (Argon2) |

---

## 📚 Documentation Complète

La documentation détaillée se trouve dans le dossier [`docs/`](./docs/).

*   👉 **[Bible des Fonctionnalités](./docs/features_full_list.md)** : Liste exhaustive de toutes les features.
*   👉 **[Architecture Technique](./docs/technical_architecture.md)** : Structure du code, schéma BDD, sécurité.
*   👉 **[Guide de Déploiement](./docs/deployment_guide.md)** : Installation, variables d'env, mise en prod.
*   👉 **[Manuel Utilisateur](./docs/user_manual.md)** : Guide pour les éditeurs de contenu.

---

## 🚀 Installation Rapide

### Prérequis
*   Python 3.11+
*   `pip` ou `uv`
*   Git

### 1. Cloner le projet
```bash
git clone https://github.com/votre-org/bellari-concept.git
cd bellari-concept
```

### 2. Installer les dépendances
```bash
pip install -r requirements.txt
```

### 3. Configurer l'environnement
Créez un fichier `.env` à la racine :
```ini
DATABASE_URL=sqlite:///site.db
SESSION_SECRET=votre_cle_secrete_super_longue
ADMIN_USERNAME=admin
ADMIN_PASSWORD=password123
ADMIN_INIT_ALLOWED=true
```

### 4. Initialiser la Base de Données
```bash
python init_db.py
```

### 5. Lancer le serveur
```bash
python app.py
```
Accédez à l'application sur `http://localhost:5000`.

---

## 📂 Structure du Projet

```
bellari-concept/
├── app.py                 # Point d'entrée principal
├── init_db.py             # Script de migration et seeding
├── docs/                  # Documentation technique et utilisateur
├── static/                # Assets (CSS, JS, Uploads)
├── templates/             # Vues HTML (Jinja2)
├── requirements.txt       # Dépendances Python
└── README.md              # Ce fichier
```

---

## © Crédits

*   **Produit par :** MOA Digital Agency
*   **Développé par :** Aisance KALONJI
*   **Audité par :** La CyberConfiance

*Copyright © 2025 Bellari Concept. Tous droits réservés.*
