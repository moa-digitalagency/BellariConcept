![Python 3.11](https://img.shields.io/badge/Python-3.11-blue?style=flat-square&logo=python) ![Flask 3.0](https://img.shields.io/badge/Framework-Flask%203.0-green?style=flat-square&logo=flask) ![PostgreSQL 15](https://img.shields.io/badge/Database-PostgreSQL%2015-336791?style=flat-square&logo=postgresql) ![Status: Stable](https://img.shields.io/badge/Status-Stable-success?style=flat-square) ![License: Proprietary](https://img.shields.io/badge/License-Proprietary-red?style=flat-square) ![Owner: MOA Digital Agency](https://img.shields.io/badge/Owner-MOA%20Digital%20Agency-orange?style=flat-square)

# Bellari Concept - Liste Complète des Fonctionnalités

> **AVERTISSEMENT LÉGAL**
>
> Ce document et le code source associé sont la propriété exclusive de **MOA Digital Agency** et **Aisance KALONJI**.
> Toute reproduction, distribution ou utilisation non autorisée est strictement interdite.
> Usage interne uniquement.

---

Ce document recense de manière exhaustive toutes les fonctionnalités techniques et métier implémentées dans le CMS Bellari Concept.

## 1. Gestion de Contenu (CMS)
Le cœur du système repose sur une architecture flexible permettant une gestion bilingue (Français/Anglais) fluide.

### 1.1 Architecture des Pages et Sections
*   **Modèle `Page` :** Gestion des pages statiques (Accueil, À Propos, Services, Portfolio, Contact) avec slugs personnalisés.
*   **Modèle `Section` :** Chaque page est composée de blocs modulaires (`hero`, `text`, `service`, `contact`, `features`).
*   **Synchronisation Bilingue :**
    *   Le système de "Normalisation des Sections" (`normalize_sections.py` / Admin Route) assure que chaque section FR possède son équivalent EN avec le même `order_index`.
    *   L'interface d'édition permet la création simultanée des contenus FR et EN.
*   **SEO par Page :** Titres (`title`) et méta-descriptions éditables individuellement pour chaque page.

### 1.2 Gestion des Médias
*   **Upload Sécurisé :** Vérification des extensions (`png`, `jpg`, `jpeg`, `gif`, `webp`) et nettoyage des noms de fichiers (`werkzeug.secure_filename`).
*   **Optimisation :** Stockage des métadonnées (taille, dimensions) dans la base de données (`Image` model).
*   **Visualisation :** Galerie d'images dans l'interface d'administration avec prévisualisation.

### 1.3 Interface d'Administration
*   **Dashboard :** Vue d'ensemble des pages et des dernières images uploadées.
*   **Éditeur WYSIWYG (Textarea) :** Champs de texte riches pour le contenu des sections.
*   **Gestion des Paramètres du Site :** Configuration dynamique (Nom du site, Logos, Liens sociaux) sans redéploiement via la table `SiteSettings`.

## 2. Sécurité & Robustesse
La sécurité est intégrée à chaque niveau de l'application.

### 2.1 Authentification & Autorisation
*   **Hachage Argon2 :** Utilisation de `werkzeug.security` pour le hachage robuste des mots de passe administrateur.
*   **Session Management :** Cookies sécurisés (`HttpOnly`, `Secure`, `SameSite='Lax'`).
*   **Protection Admin :** Décorateur `@login_required` sur toutes les routes `/admin`.

### 2.2 Protections Web
*   **CSRF (Cross-Site Request Forgery) :** Protection globale via `Flask-WTF` sur tous les formulaires POST.
*   **CSP (Content Security Policy) :** Configuration stricte via `flask-talisman` pour prévenir les attaques XSS.
    *   Autorise uniquement les sources de confiance (Self, Google Fonts, Tailwind CDN).
    *   Force HTTPS en production.
*   **Gestion des Erreurs :** Pages d'erreur personnalisées (400, 403, 404, 451) avec animations Lottie pour une meilleure UX même en cas de problème.

## 3. Progressive Web App (PWA)
Le site est entièrement compatible PWA, transformant le site web en application installable.

*   **Manifeste Dynamique :** Route `/manifest.json` générée à la volée depuis la base de données (`SiteSettings`).
*   **Configuration Admin :**
    *   Activation/Désactivation de la PWA.
    *   Personnalisation du nom, des couleurs (thème/background) et des icônes.
    *   Choix du mode d'affichage (`standalone`, `fullscreen`, etc.).
*   **Support Mobile :** `viewport` et balises `meta` optimisées pour l'expérience mobile.

## 4. Optimisation SEO & Technique
*   **Sitemap XML Automatique :** Route `/sitemap.xml` générant dynamiquement la liste des pages actives avec leur date de modification (`lastmod`) et priorité.
*   **Robots.txt Dynamique :** Route `/robots.txt` configurée pour autoriser les moteurs de recherche légitimes (Google, Bing) et bloquer les bots malveillants ou inutiles (MJ12bot, Ahrefs, etc.).
*   **Gestion des Langues :** Route `/set_language/<lang>` avec stockage en session pour une persistance du choix utilisateur.

## 5. Déploiement & Maintenance
Des scripts automatisés assurent un déploiement fiable et reproductible.

*   **`deploy.sh` :**
    *   Vérification des dépendances système (Python 3.11+, pip).
    *   Génération automatique du fichier `.env` sécurisé (clés secrètes aléatoires).
    *   Création et activation de l'environnement virtuel (`.venv`).
    *   Installation des dépendances Python.
*   **`init_db.py` (Migration Robuste) :**
    *   Système de migration "maison" pour VPS : vérifie l'existence des tables ET des colonnes.
    *   Ajoute automatiquement les colonnes manquantes (ALTER TABLE) sans perte de données.
    *   Initialisation intelligente du contenu par défaut (Pages, Sections, Admin) si la base est vide.
*   **`verify_deployment.py` :** Script de pré-vol vérifiant la connexion DB et la présence des fichiers statiques critiques.

---
*© 2024 MOA Digital Agency. Tous droits réservés.*
