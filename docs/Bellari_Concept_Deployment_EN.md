![Python Version](https://img.shields.io/badge/Python-3.11%2B-blue) ![Framework](https://img.shields.io/badge/Framework-Flask%203.0-green) ![Database](https://img.shields.io/badge/Database-PostgreSQL-orange) ![Status](https://img.shields.io/badge/Status-Proprietary-red) ![License](https://img.shields.io/badge/License-MOA%20Private-red) ![Owner](https://img.shields.io/badge/Owner-MOA%20Digital%20Agency-purple)

# Bellari Concept - Deployment Guide

> **STRICTLY CONFIDENTIAL DOCUMENT**
>
> This document is intended only for system administrators authorized by **MOA Digital Agency**.

This guide describes the secure deployment procedure for a Linux production environment (Ubuntu/Debian).

## 1. System Prerequisites

*   **OS:** Ubuntu 22.04 LTS (recommended) or Debian 11+.
*   **Runtime:** Python 3.11+.
*   **Database:** PostgreSQL 14+ (or SQLite for restricted environments).
*   **Web Server:** Nginx.
*   **Access:** SSH with sudo privileges.

---

## 2. Automated Deployment (`deploy.sh`)

The project includes an orchestration script that automates the initial configuration.

```bash
# 1. Clone the repository (Restricted Access)
git clone https://github.com/votre-repo/bellari-concept.git
cd bellari-concept

# 2. Run the deployment script
chmod +x deploy.sh
./deploy.sh
```

**Script Actions:**
1.  Verifies the Python version.
2.  Generates the production `.env` file (prompts for DB credentials).
3.  Creates the virtual environment (`.venv`) and installs dependencies.
4.  Initializes the database and creates the initial Admin account.

---

## 3. Manual Environment Variable Configuration

If you cannot use the script, create the `.env` file manually:

```ini
# Database (PostgreSQL)
DATABASE_URL=postgresql://user:password@localhost:5432/bellari_db

# Flask Security
SESSION_SECRET=your_very_long_secure_random_string
FLASK_ENV=production
FLASK_DEBUG=False
FORCE_HTTPS=True

# Initial Admin (Security)
# Set to 'true' only for the first deployment
ADMIN_INIT_ALLOWED=true
ADMIN_USERNAME=admin
ADMIN_PASSWORD=your_strong_password
```

---

## 4. Health Check (`verify_deployment.py`)

Before going live, execute the diagnostic script. It checks the integrity of static files, DB connection, and directory structure.

```bash
source .venv/bin/activate
python verify_deployment.py
```

**Expected Output:**
```text
✅ TOUTES LES VÉRIFICATIONS ONT RÉUSSI!
🎉 Le site est prêt pour le déploiement sur VPS
```

---

## 5. Server Configuration (Production)

### A. Gunicorn (Application Server)

Create the systemd service `/etc/systemd/system/bellari.service`:

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

### B. Nginx (Reverse Proxy & SSL)

Recommended configuration `/etc/nginx/sites-available/bellari`:

```nginx
server {
    listen 80;
    server_name example.com;

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

Enable the site and secure with Certbot:
```bash
sudo ln -s /etc/nginx/sites-available/bellari /etc/nginx/sites-enabled
sudo certbot --nginx -d example.com
```

---

## 6. Post-Deployment

1.  Access `/admin/login`.
2.  Log in with the credentials defined in `.env`.
3.  **IMPORTANT:** Change the Admin password immediately.
4.  In `.env`, set `ADMIN_INIT_ALLOWED=false` and restart the service (`sudo systemctl restart bellari`).
