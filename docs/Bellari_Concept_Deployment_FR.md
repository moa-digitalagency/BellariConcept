![Python 3.11](https://img.shields.io/badge/Python-3.11-blue?style=flat-square&logo=python) ![PostgreSQL 15](https://img.shields.io/badge/Database-PostgreSQL%2015-336791?style=flat-square&logo=postgresql) ![Status: Production](https://img.shields.io/badge/Status-Production-success?style=flat-square) ![License: Proprietary](https://img.shields.io/badge/License-Proprietary-red?style=flat-square) ![Owner: MOA Digital Agency](https://img.shields.io/badge/Owner-MOA%20Digital%20Agency-orange?style=flat-square)

# Bellari Concept - Guide de Déploiement

> **AVERTISSEMENT LÉGAL**
>
> Ce guide et les scripts associés sont la propriété exclusive de **MOA Digital Agency**.
> Toute distribution externe est interdite.

---

## 1. Prérequis Système
Le CMS est optimisé pour un déploiement sur VPS Linux (Ubuntu 20.04/22.04 recommandé).

*   **Système :** Ubuntu 22.04 LTS (ou équivalent)
*   **Langage :** Python 3.11 ou supérieur
*   **Base de Données :** PostgreSQL 15+ (local ou distant)
*   **Serveur Web :** Nginx (Reverse Proxy)

## 2. Installation Automatisée

Le script `deploy.sh` automatise 90% du processus.

### 2.1 Clonage et Lancement
```bash
# 1. Cloner le dépôt (Accès privé requis)
git clone <URL_DU_DEPOT>
cd bellari-concept

# 2. Rendre le script exécutable
chmod +x deploy.sh

# 3. Lancer l'installation
./deploy.sh
```

### 2.2 Ce que fait le script :
1.  **Vérification :** Contrôle la version de Python et la présence de `pip`.
2.  **Environnement :** Demande les identifiants PostgreSQL et génère un fichier `.env` sécurisé.
3.  **Virtualenv :** Crée un environnement virtuel dans `.venv` et l'active.
4.  **Dépendances :** Installe les paquets listés dans `requirements.txt`.
5.  **Base de Données :**
    *   Vérifie la connexion PostgreSQL.
    *   Exécute `init_db.py` pour créer les tables et migrer le schéma si nécessaire.
    *   Crée un compte administrateur par défaut si aucun n'existe.

## 3. Configuration Manuelle (.env)
Si vous ne souhaitez pas utiliser le script, créez un fichier `.env` à la racine :

```ini
# Base de Données
DATABASE_URL=postgresql://user:password@localhost:5432/bellari_concept

# Sécurité Flask
SESSION_SECRET=votre_cle_secrete_tres_longue_et_aleatoire
FLASK_ENV=production
FLASK_DEBUG=False

# Configuration Admin (Optionnel pour l'init)
ADMIN_USERNAME=admin
ADMIN_PASSWORD=votre_mot_de_passe_fort
ADMIN_INIT_ALLOWED=true

# Serveur
PORT=5000
HOST=0.0.0.0
```

## 4. Démarrage en Production

Pour la production, utilisez Gunicorn (installé via requirements.txt).

```bash
# Activer l'environnement
source .venv/bin/activate

# Lancer avec 4 workers (ajuster selon CPU)
gunicorn --bind 0.0.0.0:5000 --workers 4 app:app
```

### Configuration Nginx (Recommandée)
Créez un bloc serveur pour rediriger le trafic vers le port 5000.

```nginx
server {
    listen 80;
    server_name vobeddomaine.com;

    location / {
        proxy_pass http://127.0.0.1:5000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

## 5. Maintenance et Mises à Jour

### Initialisation / Migration de la BDD
Le script `init_db.py` est idempotent. Il peut être relancé en toute sécurité pour :
*   Créer de nouvelles tables.
*   Ajouter de nouvelles colonnes (via le système de migration manuelle).
*   Réinitialiser les paramètres PWA par défaut.

```bash
python3 init_db.py
```

### Logs
*   **Gunicorn :** Définis lors du lancement (ex: `--access-logfile logs/access.log`).
*   **Flask :** Affiche les erreurs critiques dans `logs/error.log` (si configuré).

---
*© 2024 MOA Digital Agency. Tous droits réservés.*
