# Bellari Concept - Guide d'Installation & Déploiement

Ce guide technique détaille les étapes nécessaires pour installer, configurer et déployer l'application Bellari Concept sur un environnement de production (VPS, Heroku, Railway) ou local.

---

## 1. Prérequis Système

*   **OS :** Linux (Ubuntu 20.04+ recommandé), macOS, ou Windows (WSL2).
*   **Langage :** Python 3.10 ou supérieur.
*   **Gestionnaire de Paquets :** `pip` (ou `uv` pour plus de rapidité).
*   **Base de Données :**
    *   **PostgreSQL** (Production).
    *   **SQLite** (Développement local uniquement).

---

## 2. Configuration de l'Environnement

L'application suit la méthodologie "Twelve-Factor App" et se configure exclusivement via des variables d'environnement. Créez un fichier `.env` à la racine ou configurez votre hébergeur.

### Variables Critiques (Obligatoires)

| Variable | Description | Exemple / Valeur |
| :--- | :--- | :--- |
| `DATABASE_URL` | Chaîne de connexion à la BDD | `postgresql://user:pass@host:5432/dbname` (ou `sqlite:///site.db`) |
| `SESSION_SECRET` | Clé secrète pour signer les cookies | `long-random-string-generated-by-openssl` |
| `ADMIN_USERNAME` | Nom d'utilisateur du compte Admin | `admin` |
| `ADMIN_PASSWORD` | Mot de passe initial Admin | `SuperSecretPassword123!` (Min 8 chars) |

### Variables Optionnelles

| Variable | Description | Défaut |
| :--- | :--- | :--- |
| `FLASK_ENV` | Mode d'exécution Flask | `production` |
| `FORCE_HTTPS` | Redirection HTTP vers HTTPS | `True` (Mettre `False` en local) |
| `ADMIN_INIT_ALLOWED` | Autorise la création de l'admin | `true` |

---

## 3. Installation & Démarrage

### A. Installation des Dépendances
```bash
# Créer un environnement virtuel (optionnel mais recommandé)
python3 -m venv venv
source venv/bin/activate

# Installer les paquets
pip install -r requirements.txt
```

### B. Initialisation de la Base de Données
Cette étape crée les tables et l'utilisateur admin par défaut.
```bash
python init_db.py
```
*   *Sortie attendue :* `✅ Admin user created: admin`

### C. Vérification Pré-Déploiement
Avant de lancer le serveur, exécutez le script de santé pour valider l'environnement.
```bash
python verify_deployment.py
```
*   *Sortie attendue :* `✅ TOUTES LES VÉRIFICATIONS ONT RÉUSSI!`

### D. Lancement du Serveur

**En Développement :**
```bash
python main.py
# ou
flask run --debug
```

**En Production (Gunicorn) :**
```bash
gunicorn --bind 0.0.0.0:8000 --workers 4 main:app
```
*   Pour un VPS, utilisez un gestionnaire de processus comme `systemd` ou `supervisor` pour maintenir Gunicorn en vie.

---

## 4. Maintenance & Mises à Jour

### Mise à jour du Schéma BDD
Si le code change (nouvelles colonnes), relancez simplement :
```bash
python init_db.py
```
Le script détectera les colonnes manquantes et appliquera les `ALTER TABLE` nécessaires sans perte de données.

### Normalisation des Sections
Si l'ordre des sections devient incohérent (désynchronisation FR/EN), connectez-vous à l'admin ou lancez le script (si disponible en CLI, sinon via l'interface web `/admin/normalize-sections`).
