> **© MOA Digital Agency (myoneart.com) - Auteur : Aisance KALONJI**
> *Ce code est la propriété exclusive de MOA Digital Agency. Usage interne uniquement. Toute reproduction ou distribution non autorisée est strictement interdite.*

[Switch to English Version](./BellariConcept_features_full_list_en.md)

# Liste Complète des Fonctionnalités - Bellari Concept

## 1. Administration & Sécurité
*   **Authentification Forte :** Login sécurisé avec hachage Argon2 (`werkzeug.security`).
*   **Protection CSRF :** Tokens anti-CSRF globaux via `Flask-WTF` pour tous les formulaires et requêtes AJAX.
*   **Content Security Policy (CSP) :** Configuration stricte via `Flask-Talisman` pour prévenir les attaques XSS.
*   **Cookies Sécurisés :** Attributs `HttpOnly`, `Secure`, et `SameSite=Lax`.
*   **Dashboard Admin :** Vue d'ensemble des pages, images récentes et accès rapide aux réglages.

## 2. CMS & Gestion de Contenu
*   **Édition Bilingue (FR/EN) :** Architecture de contenu nativement bilingue.
*   **Gestion des Pages :** Création, modification des méta-données (titre, description) et activation/désactivation des pages.
*   **Sections Modulaires :**
    *   Ajout, modification, suppression et réorganisation (drag & drop logique via `order_index`).
    *   Types de sections variés : Hero, Texte, Services, Portfolio, Contact, etc.
    *   Synchronisation des paires de sections FR/EN via `normalize_sections.py`.
    *   **Éditeur de Contenu :** Champs pour titres, sous-titres, contenu riche, boutons d'action et liens.

## 3. Gestion des Médias
*   **Upload Sécurisé :** Vérification des extensions (`png`, `jpg`, `webp`, etc.) et nettoyage des noms de fichiers.
*   **Optimisation :** Redimensionnement et traitement via `Pillow` (PIL).
*   **Galerie d'Images :** Bibliothèque centralisée pour réutiliser les images dans les sections.
*   **Attributs ALT :** Gestion des textes alternatifs pour l'accessibilité et le SEO.

## 4. Configuration Dynamique (Site Settings)
*   **Identité Visuelle :** Changement du logo, favicon et icône PWA depuis l'admin.
*   **Réseaux Sociaux :** Configuration des liens Facebook, Instagram, LinkedIn, WhatsApp.
*   **SEO Global :** Mots-clés par défaut, Image OG (Open Graph), ID Google Analytics.

## 5. Progressive Web App (PWA)
*   **Installation :** Manifeste dynamique `/manifest.json` configurable.
*   **Personnalisation :** Nom de l'app, couleurs de thème, icônes, mode d'affichage (standalone).
*   **Support Offline :** Préparé pour le service worker (configurable).

## 6. SEO & Performance
*   **Sitemap XML :** Génération automatique à `/sitemap.xml` avec dates de mise à jour.
*   **Robots.txt :** Gestion dynamique des règles d'indexation.
*   **Meta Tags :** Gestion fine des balises méta pour chaque page.
*   **Assets Optimisés :** Utilisation de TailwindCSS via CDN pour un chargement rapide.

## 7. Déploiement & Maintenance
*   **Scripts Automatisés :** `deploy.sh` et `verify_deployment.py` pour des mises en production fiables.
*   **Migration BDD :** Système de migration manuel robuste (`init_db.py`) adapté aux VPS.
*   **Logs & Erreurs :** Pages d'erreur personnalisées (404, 500) avec animations Lottie.
