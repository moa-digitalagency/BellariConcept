[ 🇫🇷 Français ] | [ 🇬🇧 English ](BellariConcept_features_full_list_en.md)

# 📜 Bellari Concept - Bible des Fonctionnalités
**Date de mise à jour :** 2025
**Auteur :** Aisance KALONJI (MOA Digital Agency)
**Usage :** Interne & Confidentiel

Ce document recense de manière exhaustive l'ensemble des fonctionnalités techniques et métier de la plateforme Bellari Concept.

---

## 1. Cœur du Système (Core)

*   **Framework :** Python Flask 3.x.
*   **Base de Données :** SQLAlchemy ORM (Compatible SQLite Dev / PostgreSQL Prod).
*   **Architecture MVC :** Séparation claire Modèles (BDD), Vues (Jinja2), Contrôleurs (Routes).
*   **Gestion des Erreurs :** Pages d'erreur personnalisées avec animations Lottie (400, 403, 404, 451).

## 2. Système de Gestion de Contenu (CMS)

### 2.1 Gestion des Pages
*   **CRUD Pages :** Création, Lecture, Mise à jour de pages (Home, About, Services, etc.).
*   **Métadonnées :** Édition du Titre (Title tag), Slug (URL), et Meta Description pour le SEO.
*   **Activation :** Possibilité d'activer/désactiver une page sans la supprimer.

### 2.2 Gestion des Sections (Le "Page Builder")
*   **Architecture Bilingue :** Chaque section FR est liée à une section EN correspondante.
*   **Types de Sections Supportés :**
    *   `Hero` : Bannière principale avec image de fond, titre, sous-titre et CTA.
    *   `Intro` : Texte d'introduction simple.
    *   `Features` : Liste de fonctionnalités ou services (avec puces).
    *   `Expertise` : Bloc image + texte pour présenter les compétences.
    *   `Why Us` : Arguments de vente (USP).
    *   `Service` : Bloc dédié à un service spécifique.
    *   `Contact` : Informations de contact formatées.
    *   `CTA` : Appel à l'action isolé.
    *   `Text` : Bloc de texte riche standard.
*   **Ordonnancement :** Gestion de l'ordre d'affichage (`order_index`).
*   **Outil de Normalisation :** Script (`/admin/normalize-sections`) pour resynchroniser les index FR/EN en cas de décalage.
*   **Personnalisation Visuelle :**
    *   Upload d'image de fond.
    *   Couleur de fond hexadécimale.
    *   Texte et lien de bouton personnalisables.

### 2.3 Médiathèque (Images)
*   **Upload Sécurisé :** Vérification des extensions (.jpg, .png, .webp, .gif).
*   **Sanitization :** Renommage automatique des fichiers pour éviter les conflits et failles (UUID + nom sécurisé).
*   **Analyse :** Détection automatique des dimensions (Largeur/Hauteur) et poids du fichier.
*   **Suppression :** Retrait du fichier disque et de l'entrée BDD.

## 3. Progressive Web App (PWA)

*   **Manifest Dynamique :** Le fichier `/manifest.json` est généré à la volée depuis la BDD.
*   **Configuration Admin :**
    *   Nom de l'App (Long/Court).
    *   Couleurs (Thème, Background).
    *   Mode d'affichage (Standalone, Minimal-UI, etc.).
    *   Icônes (192x192, 512x512).
*   **Installation :** Support natif de l'installation sur mobile et desktop ("Add to Home Screen").

## 4. Sécurité & Conformité

*   **Authentification Admin :**
    *   Protection par session sécurisée.
    *   Hachage des mots de passe via **Argon2** (via Werkzeug).
    *   Création initiale sécurisée via Variables d'Environnement (`ADMIN_USERNAME`, `ADMIN_PASSWORD`).
*   **CSRF Protection :** Tokens `Flask-WTF` obligatoires sur tous les formulaires (POST).
*   **Content Security Policy (CSP) :** Configuration stricte via `Flask-Talisman`.
    *   Restriction des sources de scripts (Self + CDN Tailwind).
    *   Protection XSS.
*   **Cookies Sécurisés :** Flags `HttpOnly`, `Secure` (si HTTPS), `SameSite=Lax`.
*   **Uploads :** Limite de taille de fichier (16MB).

## 5. SEO & Marketing

*   **Sitemap XML :** Génération automatique à `/sitemap.xml` incluant toutes les pages actives avec `lastmod`.
*   **Robots.txt :**
    *   Bloque les scrapers nuisibles (Ahrefs, Semrush, MJ12bot).
    *   Autorise explicitement les bots IA éthiques (GPTBot, ClaudeBot) pour le référencement IA.
    *   Dissimule l'admin (`/admin/*`).
*   **Social Graph :**
    *   Gestion de l'image `og:image` par défaut.
    *   Liens sociaux configurables (Facebook, Instagram, LinkedIn, WhatsApp).
*   **Tracking :** Injection du ID Google Analytics.

## 6. Déploiement & Maintenance

*   **Initialisation Robuste (`init_db.py`) :**
    *   Système de migration de schéma manuel (Vérification des colonnes manquantes au démarrage).
    *   Peuplement automatique du contenu par défaut si la BDD est vide.
*   **Proxy Inverse :** Conçu pour tourner derrière Nginx (gestion `X-Forwarded-Proto`).
*   **Conteneurisation :** Prêt pour Docker (via `deploy.sh` et structure standard).

---
© MOA Digital Agency (myoneart.com) - Auteur : Aisance KALONJI
