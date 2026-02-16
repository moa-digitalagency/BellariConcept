# Bellari Concept - Bible des Fonctionnalités

Ce document constitue la référence exhaustive des fonctionnalités techniques, métier et utilisateur de l'application Bellari Concept. Il couvre l'intégralité du cycle de vie de la donnée, de la base de données à l'interface client.

---

## 1. Core CMS & Architecture de Contenu

### Gestion des Pages (`Page`)
*   **Structure BDD :** Modèle `Page` avec `slug` (URL unique), `title`, `meta_description`, `is_active`.
*   **Comportement :**
    *   Routing dynamique : `/` charge le slug `home`. Toutes les autres pages sont accessibles via `/<slug>`.
    *   **Soft Delete :** Le champ `is_active` permet de désactiver une page sans la supprimer, renvoyant une 404 aux visiteurs mais restant éditable par l'admin.
    *   **Métadonnées SEO :** Chaque page dispose de ses propres balises `<title>` et `<meta name="description">`, éditables via le CMS.

### Gestion des Sections (`Section`)
L'architecture repose sur un système de blocs flexibles ("Sections") qui composent chaque page.
*   **Types de Sections :** `hero`, `text`, `service`, `features`, `expertise`, `why_us`, `contact`, `cta`.
*   **Pairing Multilingue (Logiciel) :**
    *   Chaque section possède un `language_code` ('fr' ou 'en') et un `order_index`.
    *   **Règle d'Or :** Pour garantir un affichage cohérent lors du changement de langue, une section FR à l'index N doit impérativement avoir une section équivalente EN à l'index N.
    *   **Création Atomique :** L'interface admin `/admin/section/create_both` force la création simultanée des deux variantes pour maintenir la synchronicité.
*   **Normalisation Automatique (`normalize_sections.py`) :**
    *   Script de maintenance critique.
    *   Parcourt toutes les pages et regroupe les sections par type et langue.
    *   Réécrit les `order_index` de manière séquentielle (0, 1, 2...) pour s'assurer que la paire FR/EN partage strictement le même index.
    *   Corrige les désynchronisations dues à des suppressions manuelles ou erreurs d'insertion.

### Gestion des Médias (`Image`)
*   **Upload Sécurisé :**
    *   Validation stricte des extensions (`png`, `jpg`, `jpeg`, `gif`, `webp`).
    *   Renommage automatique via `secure_filename` + hash hexadécimal (8 chars) pour éviter les collisions et l'exécution de code malveillant.
*   **Validation PIL :**
    *   Vérification binaire du fichier via `PIL.Image` pour s'assurer qu'il s'agit bien d'une image valide, prévenant les attaques par upload de scripts déguisés.
    *   Extraction automatique des dimensions (width/height) pour le layout.
*   **Stockage :** Local (`static/uploads/`).

---

## 2. Authentification & Sécurité

### Protocole de Connexion
*   **Hachage Argon2 :** Utilisation de `werkzeug.security` avec l'algorithme Argon2 pour le stockage des mots de passe (résistant aux attaques GPU/ASIC).
*   **Session Admin :**
    *   Protection via `Flask-Login`.
    *   Cookie de session sécurisé : `HttpOnly` (anti-XSS), `Secure` (HTTPS only), `SameSite='Lax'` (anti-CSRF).
*   **Initialisation Sécurisée (`init_db.py`) :**
    *   Création du premier administrateur uniquement via variables d'environnement (`ADMIN_USERNAME`, `ADMIN_PASSWORD`).
    *   Refus de création si le mot de passe est inférieur à 8 caractères.

### Défense en Profondeur
*   **CSRF Protection (`Flask-WTF`) :**
    *   Token CSRF obligatoire pour tous les formulaires (POST).
    *   Validation stricte côté serveur avant traitement.
*   **Content Security Policy (CSP) :**
    *   Implémentation stricte via `Flask-Talisman`.
    *   Autorise : `self`, Google Fonts, Tailwind CDN.
    *   Bloque : Scripts inline non autorisés, iframes externes, objets flash/java.
    *   Force HTTPS en production.
*   **En-têtes de Sécurité :**
    *   `X-Content-Type-Options: nosniff`
    *   `X-Frame-Options: SAMEORIGIN`

---

## 3. Progressive Web App (PWA)

### Manifest Dynamique
*   **Route :** `/manifest.json`
*   **Logique :** Généré dynamiquement à partir des `SiteSettings` en base de données.
    *   Permet à l'administrateur de changer le nom de l'app, l'icône, et les couleurs (thème/background) sans redéployer le code.
    *   Supporte les modes d'affichage `standalone`, `browser`, `minimal-ui`.

### Service Worker & Installation (`pwa.js`)
*   **Enregistrement :** `static/sw.js` est enregistré au chargement de la page si supporté par le navigateur.
*   **Prompts d'Installation Intelligents :**
    *   **Android/Desktop :** Intercepte l'événement `beforeinstallprompt`, empêche la bannière native Chrome, et affiche un modal personnalisé `#pwa-install-prompt`.
    *   **iOS :** Détecte le User-Agent (iPhone/iPad/iPod) et l'absence de mode `standalone`. Affiche un modal spécifique `#pwa-ios-prompt` avec instructions manuelles ("Share" -> "Add to Home Screen").
    *   **Persistance :** Utilise `localStorage` pour ne pas harceler l'utilisateur iOS s'il a déjà fermé le prompt.

---

## 4. SEO Technique & Structuré

### Données Structurées (JSON-LD)
*   **Type :** `LocalBusiness`.
*   **Injection :** Dynamique dans `<head>` de `base.html`.
*   **Données :**
    *   Nom, Logo, Description (adaptée à la langue FR/EN).
    *   Coordonnées géographiques (Latitude/Longitude), Adresse, Téléphone, Email.
    *   Heures d'ouverture (`OpeningHoursSpecification`).
    *   Catalogue de services (`OfferCatalog`) listant Construction, Électricité, Plomberie, etc.

### Méta-données Dynamiques
*   **OpenGraph & Twitter Cards :**
    *   Générés automatiquement pour chaque page.
    *   Image par défaut configurable dans les `SiteSettings`.
*   **Sitemap XML (`/sitemap.xml`) :**
    *   Liste toutes les pages actives.
    *   Priorité : 1.0 (Accueil) vs 0.8 (Pages internes).
    *   Fréquence de changement : `weekly`.
*   **Robots.txt (`/robots.txt`) :**
    *   Allow : Bots majeurs (Google, Bing) et IA éthiques (GPTBot, ClaudeBot).
    *   Disallow : Admin (`/admin`), uploads bruts, et scrapers agressifs (Ahrefs, Semrush, MJ12bot).

---

## 5. Déploiement & Maintenance

### Vérification Pré-Déploiement (`verify_deployment.py`)
Script critique à exécuter avant tout déploiement ou redémarrage.
1.  **Vérification Fichiers :** Confirme la présence des assets statiques critiques (images du thème).
2.  **Vérification Structure :** Valide l'existence des dossiers `static/uploads`, `templates`, etc.
3.  **Vérification BDD :**
    *   S'assure que la page `home` existe.
    *   Compte les sections critiques (`hero`, `expertise`) pour garantir qu'il y en a bien 2 de chaque (FR + EN).
4.  **Vérification Env :** Valide `DATABASE_URL` et `SESSION_SECRET`.

### Migration "Resiliente" (`init_db.py`)
Contrairement à Alembic qui nécessite un historique strict, ce système est conçu pour l'auto-réparation sur VPS.
*   **Vérification de Schéma :** Inspecte les tables existantes.
*   **Migration Colonne par Colonne :**
    *   Définit un schéma cible (dictionnaire `schema_checks`).
    *   Si une colonne manque (ex: `pwa_enabled` ajouté dans une mise à jour), exécute un `ALTER TABLE ADD COLUMN` brut.
    *   Compatible SQLite et PostgreSQL.

### Configuration Globale (`SiteSettings`)
Table clé-valeur permettant la configuration à chaud sans redémarrage :
*   **Champs :** `pwa_enabled`, `google_analytics_id`, `facebook_url`, etc.
*   **Injection Contextuelle :** `inject_site_settings` rend ces valeurs disponibles dans tous les templates Jinja2 sans requête explicite dans chaque route.
