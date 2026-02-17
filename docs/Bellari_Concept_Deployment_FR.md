![Python Version](https://img.shields.io/badge/Python-3.11%2B-blue) ![Framework](https://img.shields.io/badge/Framework-Flask%203.0-green) ![Database](https://img.shields.io/badge/Database-PostgreSQL-orange) ![Status](https://img.shields.io/badge/Status-Proprietary-red) ![License](https://img.shields.io/badge/License-MOA%20Private-red) ![Owner](https://img.shields.io/badge/Owner-MOA%20Digital%20Agency-purple)

# Bellari Concept - Guide de Déploiement

> **DOCUMENT STRICTEMENT CONFIDENTIEL**
>
> Ce document est destiné uniquement aux administrateurs système autorisés par **MOA Digital Agency**.

Ce guide décrit la procédure de déploiement sécurisée sur un environnement de production Linux (Ubuntu/Debian).

## 1. Prérequis Système

*   **OS :** Ubuntu 22.04 LTS (recommandé) ou Debian 11+.
*   **Runtime :** Python 3.11+.
*   **Base de Données :** PostgreSQL 14+ (ou SQLite pour environnements restreints).
*   **Serveur Web :** Nginx.
*   **Accès :** SSH avec privilèges sudo.

---

## 2. Déploiement Automatisé (`deploy.sh`)

Le projet inclut un script d'orchestration qui automatise la configuration initiale.

```bash
# 1. Cloner le dépôt (Accès restreint)
git clone https://github.com/votre-repo/bellari-concept.git
cd bellari-concept

# 2. Lancer le script de déploiement
chmod +x deploy.sh
./deploy.sh
```

**Actions du script :**
1.  Vérifie la version de Python.
2.  Génère le fichier `.env` de production (demande les credentials DB).
3.  Crée l'environnement virtuel (`.venv`) et installe les dépendances.
4.  Initialise la base de données et crée le compte Admin initial.

---

## 3. Configuration Manuelle des Variables d'Environnement

Si vous ne pouvez pas utiliser le script, créez manuellement le fichier `.env` :

```ini
# Base de Données (PostgreSQL)
DATABASE_URL=postgresql://user:password@localhost:5432/bellari_db

# Sécurité Flask
SESSION_SECRET=votre_chaine_aleatoire_tres_longue_et_securisee
FLASK_ENV=production
FLASK_DEBUG=False
FORCE_HTTPS=True

# Admin Initial (Sécurité)
# Définir à 'true' uniquement pour le premier déploiement
ADMIN_INIT_ALLOWED=true
ADMIN_USERNAME=admin
ADMIN_PASSWORD=votre_mot_de_passe_fort
```

---

## 4. Vérification de Santé (`verify_deployment.py`)

Avant de mettre le site en ligne, exécutez le script de diagnostic. Il vérifie l'intégrité des fichiers statiques, la connexion DB et la structure des répertoires.

```bash
source .venv/bin/activate
python verify_deployment.py
```

**Sortie attendue :**
```text
✅ TOUTES LES VÉRIFICATIONS ONT RÉUSSI!
🎉 Le site est prêt pour le déploiement sur VPS
```

---

## 5. Configuration Serveur (Production)

### A. Gunicorn (Serveur d'Application)

Créer le service systemd `/etc/systemd/system/bellari.service` :

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

Configuration recommandée `/etc/nginx/sites-available/bellari` :

```nginx
server {
    listen 80;
    server_name exemple.com;

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

Activez le site et sécurisez avec Certbot :
```bash
sudo ln -s /etc/nginx/sites-available/bellari /etc/nginx/sites-enabled
sudo certbot --nginx -d exemple.com
```

---

## 6. Post-Déploiement

1.  Accédez à `/admin/login`.
2.  Connectez-vous avec les identifiants définis dans `.env`.
3.  **IMPORTANT :** Modifiez immédiatement le mot de passe Admin.
4.  Dans `.env`, passez `ADMIN_INIT_ALLOWED=false` et redémarrez le service (`sudo systemctl restart bellari`).
