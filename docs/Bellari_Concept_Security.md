# Bellari Concept - Architecture de Sécurité

Ce document décrit les mesures de sécurité techniques et organisationnelles mises en place pour protéger l'application, ses données et ses utilisateurs.

---

## 1. Authentification & Gestion des Sessions

### Hachage des Mots de Passe
*   **Algorithme :** Argon2 (via `werkzeug.security`).
*   **Implémentation :** `generate_password_hash` avec salt automatique.
*   **Justification :** Argon2 est l'état de l'art actuel, résistant aux attaques par force brute GPU et ASIC grâce à sa configuration mémoire-dure (memory-hard).

### Sécurité des Sessions (Cookies)
Les cookies de session utilisateur sont configurés pour prévenir le vol et la manipulation :
*   `HttpOnly` : Empêche l'accès au cookie via JavaScript (atténue XSS).
*   `Secure` : Le cookie n'est transmis que sur des connexions HTTPS chiffrées.
*   `SameSite='Lax'` : Restreint l'envoi du cookie aux requêtes provenant du même site, bloquant la majorité des attaques CSRF cross-origin.

---

## 2. Sécurité Applicative

### Protection CSRF (Cross-Site Request Forgery)
*   **Outil :** `Flask-WTF`.
*   **Mécanisme :** Chaque formulaire POST doit inclure un token CSRF unique et signé.
*   **Validation :** Le serveur rejette toute requête modifiant l'état (POST, PUT, DELETE) sans token valide.

### Content Security Policy (CSP)
*   **Outil :** `Flask-Talisman`.
*   **Politique Stricte :**
    *   `default-src 'self'` : Par défaut, tout contenu externe est bloqué.
    *   `script-src` : Autorise uniquement les scripts locaux et le CDN TailwindCSS (si utilisé).
    *   `style-src` : Autorise les styles locaux et Google Fonts.
    *   `img-src` : Autorise les images locales et les Data URI.
*   **Objectif :** Réduire drastiquement la surface d'attaque XSS en empêchant l'exécution de scripts non autorisés.

### Upload de Fichiers Sécurisé
*   **Liste Blanche :** Seules les extensions d'images (`png`, `jpg`, `jpeg`, `gif`, `webp`) sont acceptées.
*   **Assainissement des Noms :** `secure_filename` nettoie les noms de fichiers (supprime les `../` et caractères spéciaux).
*   **Préfixe Aléatoire :** Chaque fichier reçoit un préfixe hexadécimal unique pour éviter les collisions et les devinettes d'URL.
*   **Validation Binaire :** `PIL` (Pillow) ouvre le fichier pour confirmer qu'il s'agit bien d'une image valide et non d'un script PHP/Shell déguisé.

---

## 3. Sécurité Infrastructure

### HTTPS & HSTS
*   **Force HTTPS :** L'application redirige automatiquement tout trafic HTTP vers HTTPS via `Flask-Talisman`.
*   **HSTS (HTTP Strict Transport Security) :** En-tête indiquant aux navigateurs de ne plus jamais tenter de connexion non sécurisée pour ce domaine pendant une longue période (ex: 1 an).

### Gestion des Secrets
*   **Zéro Secret Hardcodé :** `SECRET_KEY`, `DATABASE_URL`, et mots de passe Admin sont injectés via des variables d'environnement (`.env`).
*   **Isolation :** Le fichier `.env` est exclu de Git (`.gitignore`).

### Initialisation Admin Verrouillée
*   La création du premier compte administrateur est conditionnée par la variable `ADMIN_INIT_ALLOWED=True`.
*   Une fois le compte créé, il est impératif de passer cette variable à `False` en production pour empêcher toute réinitialisation malveillante.

---

## 4. Recommandations pour l'Opérateur

1.  **Mises à Jour Régulières :** Appliquez les correctifs de sécurité OS et Python (`pip install --upgrade -r requirements.txt`).
2.  **Surveillance des Logs :** Vérifiez régulièrement les logs d'accès et d'erreur pour détecter des tentatives d'intrusion (scans, brute-force).
3.  **Backups Chiffrés :** Sauvegardez la base de données PostgreSQL hors site et de manière chiffrée.
