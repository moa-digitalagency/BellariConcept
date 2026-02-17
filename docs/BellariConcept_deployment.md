> **© MOA Digital Agency (myoneart.com) - Auteur : Aisance KALONJI**
> *Ce code est la propriété exclusive de MOA Digital Agency. Usage interne uniquement. Toute reproduction ou distribution non autorisée est strictement interdite.*

[Switch to English Version](./BellariConcept_deployment_en.md)

# Guide de Déploiement - Bellari Concept

## 1. Prérequis Système
*   **OS :** Ubuntu 22.04 LTS (Recommandé) ou Debian 11+.
*   **Langage :** Python 3.11 ou supérieur.
*   **Serveur Web :** Nginx (Reverse Proxy).
*   **Base de Données :** SQLite (Défaut) ou PostgreSQL (Production).
*   **Accès :** Privilèges root ou sudo.

## 2. Déploiement Automatisé
Le script `deploy.sh` automatise l'installation des dépendances et la configuration initiale.

```bash
# Rendre le script exécutable
chmod +x deploy.sh

# Lancer le déploiement
./deploy.sh
```

Le script va :
1.  Vérifier la version de Python.
2.  Créer un environnement virtuel `.venv`.
3.  Installer les dépendances via `uv` (si disponible) ou `pip`.
4.  Demander les crédentiels pour la base de données.
5.  Générer le fichier `.env` si inexistant.

## 3. Déploiement Manuel
Si vous ne pouvez pas utiliser le script automatique, suivez ces étapes :

### 3.1 Installation
```bash
# 1. Cloner le dépôt (si applicable)
git clone <url_du_repo_prive>
cd bellari-concept

# 2. Créer l'environnement virtuel
python3 -m venv .venv
source .venv/bin/activate

# 3. Installer les dépendances
pip install -r requirements.txt
```

### 3.2 Configuration
Créez un fichier `.env` à la racine :
```ini
SESSION_SECRET=votre_cle_secrete_tres_longue
DATABASE_URL=sqlite:///bellari.db
ADMIN_USERNAME=admin
ADMIN_PASSWORD=votre_mot_de_passe_fort
FLASK_ENV=production
```

### 3.3 Initialisation
Exécutez le script d'initialisation pour créer les tables et l'utilisateur admin :
```bash
python init_db.py
```
*Note : Ce script gère aussi les migrations de schéma manuelles.*

## 4. Vérification
Avant de lancer le serveur, utilisez le script de vérification :
```bash
python verify_deployment.py
```
Il scannera :
*   La structure des dossiers (`static`, `templates`).
*   La connexion à la base de données.
*   La présence des fichiers critiques.

## 5. Serveur de Production (Gunicorn)
Lancez l'application avec Gunicorn :
```bash
gunicorn -w 4 -b 0.0.0.0:8000 app:app
```

Configurez ensuite Nginx pour rediriger le trafic port 80/443 vers le port 8000.
