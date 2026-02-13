# Bellari Concept - Guide de Déploiement

Ce guide détaille les étapes nécessaires pour déployer l'application Bellari Concept en local (développement) et en production (VPS, Docker, Replit).

---

## 1. Prérequis Système

*   **Python :** Version 3.11 ou supérieure.
*   **Base de Données :** PostgreSQL 14+ recommandé pour la production (SQLite supporté pour le dev).
*   **Gestionnaire de Paquets :** `pip` ou `uv` (plus rapide).
*   **Serveur Web :** Nginx (recommandé comme reverse proxy devant Gunicorn).
*   **Système d'exploitation :** Linux (Ubuntu/Debian) préféré pour la production.

---

## 2. Variables d'Environnement

L'application utilise `python-dotenv` pour charger la configuration. En production, définissez ces variables dans votre environnement système ou un fichier `.env`.

| Variable | Description | Obligatoire ? | Exemple |
| :--- | :--- | :--- | :--- |
| `DATABASE_URL` | Chaîne de connexion à la base de données (PostgreSQL/SQLite). | **OUI** | `postgresql://user:pass@localhost/db` |
| `SESSION_SECRET` | Clé secrète pour signer les cookies de session. | **OUI** | `chaine_aleatoire_tres_longue_et_complexe` |
| `ADMIN_USERNAME` | Nom d'utilisateur pour le premier compte admin. | **OUI** (init) | `admin` |
| `ADMIN_PASSWORD` | Mot de passe pour le premier compte admin. | **OUI** (init) | `MonSuperMotDePasse8!` |
| `ADMIN_INIT_ALLOWED` | Autorise l'exécution de l'initialisation DB via URL. | Non | `true` ou `false` (défaut: `false`) |
| `FORCE_HTTPS` | Force la redirection HTTPS via Flask-Talisman. | Non | `true` (défaut: `true`) |
| `FLASK_ENV` | Environnement d'exécution. | Non | `production` ou `development` |

---

## 3. Installation Locale (Développement)

1.  **Cloner le dépôt :**
    ```bash
    git clone https://github.com/votre-repo/bellari-concept.git
    cd bellari-concept
    ```

2.  **Créer un environnement virtuel :**
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # Linux/Mac
    # venv\Scripts\activate   # Windows
    ```

3.  **Installer les dépendances :**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configurer l'environnement (.env) :**
    Créez un fichier `.env` à la racine :
    ```ini
    DATABASE_URL=sqlite:///site.db
    SESSION_SECRET=dev_secret_key
    ADMIN_USERNAME=admin
    ADMIN_PASSWORD=admin
    ADMIN_INIT_ALLOWED=true
    FORCE_HTTPS=false
    ```

5.  **Initialiser la base de données :**
    Lancer le script d'initialisation :
    ```bash
    python init_db.py
    ```

6.  **Lancer le serveur de développement :**
    ```bash
    python app.py
    ```
    Accédez à `http://localhost:5000`.

---

## 4. Déploiement en Production (VPS / Linux)

### A. Préparation
Suivez les étapes 1 à 3 de l'installation locale sur votre serveur.

### B. Configuration Base de Données (PostgreSQL)
1.  Installez PostgreSQL : `sudo apt install postgresql postgresql-contrib`
2.  Créez la base et l'utilisateur :
    ```sql
    sudo -u postgres psql
    CREATE DATABASE bellari_prod;
    CREATE USER bellari_user WITH PASSWORD 'votre_mot_de_passe_fort';
    GRANT ALL PRIVILEGES ON DATABASE bellari_prod TO bellari_user;
    \q
    ```
3.  Mettez à jour votre `.env` avec l'URL PostgreSQL :
    `DATABASE_URL=postgresql://bellari_user:votre_mot_de_passe_fort@localhost/bellari_prod`

### C. Service Systemd (Gunicorn)
Créez un fichier de service pour que l'application tourne en arrière-plan et redémarre automatiquement.

Fichier `/etc/systemd/system/bellari.service` :
```ini
[Unit]
Description=Gunicorn instance to serve Bellari Concept
After=network.target

[Service]
User=www-data
Group=www-data
WorkingDirectory=/var/www/bellari-concept
Environment="PATH=/var/www/bellari-concept/venv/bin"
EnvironmentFile=/var/www/bellari-concept/.env
ExecStart=/var/www/bellari-concept/venv/bin/gunicorn --workers 3 --bind unix:bellari.sock -m 007 main:app

[Install]
WantedBy=multi-user.target
```

Activez le service :
```bash
sudo systemctl start bellari
sudo systemctl enable bellari
```

### D. Configuration Nginx
Configurez Nginx comme reverse proxy pour gérer le SSL et servir les fichiers statiques.

Fichier `/etc/nginx/sites-available/bellari` :
```nginx
server {
    listen 80;
    server_name voutre-domaine.com www.votre-domaine.com;

    location / {
        include proxy_params;
        proxy_pass http://unix:/var/www/bellari-concept/bellari.sock;
    }

    location /static {
        alias /var/www/bellari-concept/static;
        expires 30d;
    }
}
```

Activez le site :
```bash
sudo ln -s /etc/nginx/sites-available/bellari /etc/nginx/sites-enabled
sudo nginx -t
sudo systemctl restart nginx
```

---

## 5. Maintenance & Dépannage

### Mises à Jour (Git Pull)
Lorsque vous mettez à jour le code via `git pull` :
1.  Activez l'environnement virtuel.
2.  Installez les nouvelles dépendances : `pip install -r requirements.txt`.
3.  Lancez le script de migration manuelle : `python init_db.py`.
    *   *Note :* Ce script détecte automatiquement les nouvelles colonnes et met à jour le schéma sans perte de données.
4.  Redémarrez le service : `sudo systemctl restart bellari`.

### Problèmes Courants

*   **Erreur 500 au démarrage :**
    *   Vérifiez les logs Gunicorn : `sudo journalctl -u bellari`.
    *   Assurez-vous que `DATABASE_URL` est correct.

*   **Erreur CSRF "The CSRF token is missing" :**
    *   Vérifiez que `SESSION_SECRET` est défini.
    *   Si vous êtes derrière un proxy (Cloudflare, Nginx), assurez-vous que les en-têtes `X-Forwarded-Proto` sont bien transmis (HTTPS).
    *   Vérifiez que votre navigateur accepte les cookies (la configuration `SameSite=Lax` peut bloquer dans certains contextes d'iframe).

*   **Images non affichées :**
    *   Vérifiez les permissions du dossier `static/uploads`. L'utilisateur `www-data` doit avoir les droits d'écriture :
        ```bash
        sudo chown -R www-data:www-data static/uploads
        sudo chmod -R 755 static/uploads
        ```
