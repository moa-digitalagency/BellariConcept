# Bellari Concept - Guide de Déploiement Production

Ce document détaille la procédure standard pour déployer Bellari Concept sur un serveur de production (VPS Linux type Ubuntu/Debian).

---

## 1. Prérequis Infrastructure

*   **Serveur :** VPS avec 2GB RAM minimum recommandé.
*   **OS :** Ubuntu 20.04 ou 22.04 LTS.
*   **Domaine :** Un nom de domaine pointant vers l'IP du serveur (A Record).
*   **Accès :** SSH avec privilèges root/sudo.

---

## 2. Déploiement Automatisé (Recommandé)

Le projet inclut un script `deploy.sh` qui automatise 90% des tâches.

```bash
# 1. Cloner le dépôt
git clone https://github.com/votre-repo/bellari-concept.git
cd bellari-concept

# 2. Rendre le script exécutable
chmod +x deploy.sh

# 3. Lancer le déploiement
./deploy.sh
```

Le script va :
*   Vérifier Python 3.11+ et pip.
*   Générer un fichier `.env` interactif.
*   Créer l'environnement virtuel et installer les dépendances.
*   Initialiser la base de données SQLite ou tester la connexion PostgreSQL.

---

## 3. Configuration Manuelle Avancée

Si vous préférez une installation manuelle ou devez configurer un environnement spécifique.

### A. Base de Données (PostgreSQL)

```bash
# Installation
sudo apt update
sudo apt install postgresql postgresql-contrib

# Création BDD et User
sudo -u postgres psql
```

```sql
CREATE DATABASE bellari_concept;
CREATE USER bellari_user WITH PASSWORD 'votre_mot_de_passe_fort';
GRANT ALL PRIVILEGES ON DATABASE bellari_concept TO bellari_user;
\q
```

### B. Variables d'Environnement (`.env`)

Créez le fichier `.env` à la racine :

```ini
# DATABASE
DATABASE_URL=postgresql://bellari_user:votre_mot_de_passe_fort@localhost:5432/bellari_concept

# FLASK
FLASK_ENV=production
FLASK_DEBUG=False
SESSION_SECRET=générez_une_chaine_aléatoire_longue_ici
FORCE_HTTPS=True

# ADMIN INIT (True pour le premier run, False ensuite)
ADMIN_INIT_ALLOWED=True
ADMIN_USERNAME=admin
ADMIN_PASSWORD=votre_password_admin_initial
```

### C. Initialisation Application

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python init_db.py  # Crée les tables et l'admin
python verify_deployment.py  # Vérifie que tout est OK
```

---

## 4. Configuration Serveur Web (Production)

Pour la production, n'utilisez **jamais** `flask run`. Utilisez Gunicorn derrière Nginx.

### A. Service Systemd (Gunicorn)

Créez `/etc/systemd/system/bellari.service` :

```ini
[Unit]
Description=Gunicorn instance to serve Bellari Concept
After=network.target

[Service]
User=www-data
Group=www-data
WorkingDirectory=/var/www/bellari-concept
Environment="PATH=/var/www/bellari-concept/.venv/bin"
ExecStart=/var/www/bellari-concept/.venv/bin/gunicorn --workers 3 --bind unix:bellari.sock -m 007 main:app

[Install]
WantedBy=multi-user.target
```

Activez le service :
```bash
sudo systemctl start bellari
sudo systemctl enable bellari
```

### B. Nginx (Reverse Proxy)

Créez `/etc/nginx/sites-available/bellari` :

```nginx
server {
    listen 80;
    server_name votredomaine.com www.votredomaine.com;

    location / {
        include proxy_params;
        proxy_pass http://unix:/var/www/bellari-concept/bellari.sock;
    }

    location /static {
        alias /var/www/bellari-concept/static;
        expires 30d;
    }

    # Sécurité supplémentaire
    client_max_body_size 16M;  # Pour l'upload d'images
}
```

Activez le site :
```bash
sudo ln -s /etc/nginx/sites-available/bellari /etc/nginx/sites-enabled
sudo nginx -t
sudo systemctl restart nginx
```

### C. SSL (HTTPS)

Sécurisez le site avec Let's Encrypt :

```bash
sudo apt install certbot python3-certbot-nginx
sudo certbot --nginx -d votredomaine.com -d www.votredomaine.com
```

---

## 5. Checklist de Sécurité Post-Déploiement

Une fois le site en ligne, effectuez impérativement ces actions :

1.  **Désactiver l'Init Admin :** Dans `.env`, passez `ADMIN_INIT_ALLOWED=False`.
2.  **Changer le Mot de Passe Admin :** Connectez-vous sur `/admin` et changez le mot de passe initial.
3.  **Vérifier les Backups :** Mettez en place un cron job pour dumper la base PostgreSQL quotidiennement.
    *   `pg_dump bellari_concept > backup_$(date +%F).sql`

---

## 6. Dépannage

*   **Logs Gunicorn :** `journalctl -u bellari`
*   **Logs Nginx :** `/var/log/nginx/error.log`
*   **Erreur 500 :** Vérifiez `FLASK_DEBUG=False` dans `.env` mais regardez les logs pour la stacktrace.
*   **Images ne s'affichent pas :** Vérifiez les permissions du dossier `static/uploads` (doit être accessible par `www-data`).
