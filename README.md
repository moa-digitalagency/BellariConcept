# Bellari Concept CMS

![Version](https://img.shields.io/badge/version-2.1.0-blue.svg)
![Python](https://img.shields.io/badge/python-3.10%2B-blue.svg)
![Status](https://img.shields.io/badge/status-production_ready-success.svg)
![License](https://img.shields.io/badge/license-Proprietary-red.svg)

> **Un CMS d'Architecture & Design d'Intérieur de nouvelle génération.**
> Conçu pour la performance, la sécurité et une expérience utilisateur fluide (PWA).

Bellari Concept est une plateforme web sur-mesure permettant aux agences d'architecture de gérer leur vitrine digitale avec une flexibilité totale. Il combine la puissance d'un CMS headless (gestion par blocs/sections) avec la simplicité d'un site vitrine statique optimisé pour le SEO.

---

## 🚀 Fonctionnalités Clés

*   **CMS Bilingue (FR/EN) :** Gestion de contenu par paires synchronisées. Une modification en français garde la structure en anglais intacte.
*   **Architecture Modulaire :** Construction de pages via des blocs réutilisables ("Sections") : Hero, Services, Portfolio, Témoignages...
*   **Progressive Web App (PWA) :** Transformable en application mobile native (iOS/Android) avec manifeste dynamique et invite d'installation intelligente.
*   **Sécurité Enterprise-Grade :** Hachage Argon2, CSP strict, Protection CSRF, Cookies Sécurisés.
*   **SEO Automatisé :** Génération automatique de Sitemap XML, Robots.txt, et injection de données structurées JSON-LD (LocalBusiness).
*   **Déploiement Résilient :** Scripts d'auto-réparation de la base de données (`init_db.py`) et de vérification de santé (`verify_deployment.py`).

---

## 🛠 Stack Technique

*   **Backend :** Python, Flask, SQLAlchemy.
*   **Frontend :** Jinja2, TailwindCSS (CDN), Vanilla JS.
*   **Base de Données :** PostgreSQL (Prod) / SQLite (Dev).
*   **Sécurité :** Flask-Talisman, Flask-WTF, Werkzeug Security.

---

## 📚 Documentation Complète

La documentation détaillée se trouve dans le dossier `docs/`.

| Document | Description |
| :--- | :--- |
| [**Bible des Fonctionnalités**](docs/Bellari_Concept_features_full_list.md) | Référence exhaustive de toutes les features métier et techniques. |
| [**Architecture Technique**](docs/Bellari_Concept_Architecture.md) | Diagrammes de classes, flux de données et stack. |
| [**Guide Utilisateur (Admin)**](docs/Bellari_Concept_User_Guide.md) | Manuel pour les administrateurs du site. |
| [**Guide d'Installation**](docs/Bellari_Concept_Installation.md) | Procédure de déploiement et configuration des variables d'environnement. |

> **Note :** Les liens ci-dessus pointent vers les fichiers générés dans `docs/`. Assurez-vous de consulter la version la plus récente.

---

## ⚡ Démarrage Rapide (Local)

1.  **Cloner le dépôt :**
    ```bash
    git clone https://github.com/votre-repo/bellari-concept.git
    cd bellari-concept
    ```

2.  **Configurer l'environnement :**
    Créez un fichier `.env` ou exportez les variables :
    ```bash
    export FLASK_APP=app.py
    export FLASK_ENV=development
    export DATABASE_URL="sqlite:///site.db"
    export SESSION_SECRET="dev-secret-key"
    export ADMIN_USERNAME="admin"
    export ADMIN_PASSWORD="password12345678"
    ```

3.  **Installer les dépendances :**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Initialiser la Base de Données :**
    ```bash
    python init_db.py
    # Vérifiez que l'admin est créé
    ```

5.  **Lancer le Serveur :**
    ```bash
    python main.py
    ```
    Accédez à `http://localhost:5000`.

---

## 🏗 Architecture Simplifiée

```mermaid
graph TD
    Client[Client (Browser/PWA)] -->|HTTPS| Nginx[Nginx / Gunicorn]
    Nginx -->|WSGI| Flask[Flask App]
    Flask -->|SQLAlchemy| DB[(PostgreSQL)]
    Flask -->|Jinja2| Templates[HTML Templates]
    Templates -->|CDN| Tailwind[TailwindCSS]
    Flask -->|Logic| Admin[Admin Panel]
    Admin -->|Upload| Uploads[Static Files]
```

---

## 🛡 Credits

*   **Produit par :** MOA Digital Agency
*   **Développé par :** Aisance KALONJI
*   **Audité par :** La CyberConfiance
