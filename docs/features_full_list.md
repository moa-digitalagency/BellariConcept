# Bellari Concept - Bible des Fonctionnalités

Ce document recense de manière exhaustive toutes les fonctionnalités techniques et métier de l'application Bellari Concept.

---

## 1. Authentification & Sécurité

### Système de Connexion
*   **Route :** `/admin/login` (GET/POST)
*   **Mécanisme :**
    *   Authentification par session via `Flask-Login`.
    *   Vérification du mot de passe avec hachage **Argon2** (implémentation par défaut de `werkzeug.security`).
    *   Protection contre les attaques CSRF (Cross-Site Request Forgery) sur tous les formulaires via `Flask-WTF`.
*   **Sécurité des Cookies :**
    *   `HttpOnly` : Empêche l'accès aux cookies via JavaScript (protection XSS).
    *   `Secure` : Force l'envoi des cookies uniquement via HTTPS.
    *   `SameSite=Lax` : Protection contre les requêtes inter-sites non sollicitées.

### Sécurité Globale
*   **Content Security Policy (CSP) :**
    *   Implémenté via `flask-talisman`.
    *   Politique stricte : Autorise uniquement les scripts/styles locaux, Google Fonts, et le CDN Tailwind.
    *   Blocage par défaut des scripts inline non sécurisés et des sources externes non whitelistées.
*   **En-têtes HTTP :**
    *   Forçage HTTPS strict en production (`Strict-Transport-Security`).
    *   Protection contre le Clickjacking (`X-Frame-Options: SAMEORIGIN`).

---

## 2. Système de Gestion de Contenu (CMS)

### Gestion des Pages
*   **Routes :** `/admin/pages`, `/admin/page/<id>`
*   **Fonctionnalités :**
    *   Liste de toutes les pages statiques et dynamiques.
    *   Modification des métadonnées SEO par page : Titre (`<title>`) et Meta Description.
    *   Activation/Désactivation d'une page (Soft delete : la page reste en BDD mais renvoie une 404 ou n'est plus listée).

### Gestion des Sections (Le cœur du contenu)
*   **Concept :** Une page est une agrégation de "Sections" ordonnées.
*   **Support Multilingue (FR/EN) :**
    *   Chaque section possède un code langue (`fr` ou `en`).
    *   L'interface d'édition `/admin/page/<id>` regroupe visuellement les sections par paire (FR + EN) pour une édition parallèle.
*   **Création :**
    *   Endpoint `/admin/section/create_both` : Crée simultanément la version FR et EN d'une section avec le même index d'ordre.
*   **Types de Sections supportés :**
    *   `hero` : Grande bannière avec titre, sous-titre et bouton d'action.
    *   `text` : Bloc de texte standard riche.
    *   `service` : Carte de service avec icône/image.
    *   `features` : Liste de points clés ou caractéristiques.
    *   `expertise` : Bloc mettant en avant les compétences spécifiques.
    *   `why_us` : Arguments de vente ("Pourquoi nous choisir").
    *   `contact` : Informations de contact formatées.
    *   `cta` : Appel à l'action (Call to Action).
*   **Ordonnancement :**
    *   Champ `order_index` (Entier) pour définir l'ordre d'affichage.
    *   Outil de normalisation `/admin/normalize-sections` pour réaligner les index en cas de désynchronisation entre les langues.

### Gestion des Images (Médiathèque)
*   **Route :** `/admin/images`, `/admin/upload`
*   **Upload :**
    *   Support Drag & Drop.
    *   Validation stricte des extensions (`png`, `jpg`, `jpeg`, `gif`, `webp`).
    *   **Sécurisation du nom de fichier :** `secure_filename` + préfixe hexadécimal aléatoire (8 caractères) pour éviter les collisions et les injections.
*   **Traitement :**
    *   Utilisation de la librairie **Pillow** pour analyser les dimensions (largeur/hauteur) et la taille du fichier à la volée.
*   **Suppression :**
    *   Suppression atomique du fichier sur le disque (`os.remove`) et de l'entrée en base de données.

---

## 3. Configuration du Site & PWA

### Paramètres Généraux (`SiteSettings`)
*   **Route :** `/admin/settings`
*   **Stockage :** Table clé-valeur flexible en base de données.
*   **Champs configurables :**
    *   Identité : Nom du site (FR/EN), Logo, Favicon.
    *   Réseaux Sociaux : URLs Facebook, Instagram, LinkedIn.
    *   SEO Global : Mots-clés par défaut, Image OpenGraph par défaut, ID Google Analytics.

### Progressive Web App (PWA)
*   **Manifest Dynamique :**
    *   Route `/manifest.json` générée à la volée depuis les `SiteSettings`.
    *   Permet de changer l'icône, le nom de l'app et les couleurs du thème sans redéployer le code.
*   **Configuration PWA :**
    *   Activation/Désactivation globale.
    *   Mode d'affichage (Standalone, Browser, Minimal-UI).
    *   Thème et couleur de fond personnalisables.

---

## 4. Interface Publique (Frontend)

### Rendu et Routing
*   **Moteur de Template :** Jinja2 avec héritage (`base.html`).
*   **Routing Dynamique :**
    *   La page d'accueil `/` charge le contenu de la page au slug `home`.
    *   Les autres pages sont servies via `/<slug>` (ex: `/about`, `/services`).
*   **Injection de Contexte :**
    *   Un `context_processor` injecte automatiquement les `SiteSettings` (logo, nom du site, liens sociaux) dans tous les templates, évitant la répétition de code.

### Gestion des Langues
*   **Sélecteur :** Bouton bascule FR/EN.
*   **Persistance :**
    *   Choix stocké dans la session utilisateur (`session['language']`).
    *   Route `/set_language/<lang>` pour changer la locale et rediriger vers la page précédente (`request.referrer`).
*   **Fallback :** Langue par défaut définie sur `fr` si aucune session n'est active.

### Optimisation SEO Technique
*   **Sitemap XML :**
    *   Route `/sitemap.xml`.
    *   Généré dynamiquement en listant toutes les pages actives.
    *   Inclut la date de dernière modification (`updated_at`) et la priorité (1.0 pour Home, 0.8 pour les autres).
*   **Robots.txt :**
    *   Route `/robots.txt`.
    *   Autorise les bots majeurs (Google, Bing) et les bots IA (GPTBot, ClaudeBot).
    *   Bloque explicitement les scrapers nuisibles (Ahrefs, Semrush, MJ12bot) pour préserver la bande passante.
    *   Indique l'emplacement du Sitemap.

---

## 5. Architecture Technique & Déploiement

### Base de Données
*   **ORM :** SQLAlchemy.
*   **Modèles :**
    *   `User` : Administrateurs.
    *   `Page` : Structure des pages.
    *   `Section` : Contenu riche associé aux pages.
    *   `Image` : Métadonnées des fichiers uploadés.
    *   `SiteSettings` : Configuration globale.
*   **Migration Robuste (`init_db.py`) :**
    *   Système de "Migration Manuelle" intégré au démarrage.
    *   Vérifie l'existence des tables et, surtout, **l'existence de chaque colonne critique**.
    *   Exécute des `ALTER TABLE ADD COLUMN` automatiquement si une colonne manque (compatible SQLite et PostgreSQL), assurant la stabilité lors des mises à jour sur VPS sans outils externes (Alembic).

### Initialisation
*   **Admin par défaut :**
    *   Création automatique d'un utilisateur admin au démarrage si la table est vide.
    *   Utilise les variables d'environnement `ADMIN_USERNAME` et `ADMIN_PASSWORD`.
    *   Refuse la création si le mot de passe est < 8 caractères.
*   **Contenu par défaut :**
    *   Peuple la base avec des pages et sections exemples (Lorem Ipsum structuré) si aucune page n'existe.

### Stack
*   **Serveur WSGI :** Gunicorn (Production) ou Werkzeug (Dev).
*   **Frontend :** HTML5, Tailwind CSS (via CDN), JavaScript Vanilla (pas de framework lourd).
