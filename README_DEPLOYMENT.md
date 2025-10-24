# Bellari Concept - Guide de Déploiement

## 📋 Prérequis

- Python 3.11 ou supérieur
- PostgreSQL 12 ou supérieur
- pip3
- Git (optionnel mais recommandé)

## 🚀 Déploiement Rapide

### Option 1: Script Automatique (Recommandé)

```bash
./deploy.sh
```

Le script effectuera automatiquement :
1. ✅ Vérification des prérequis système
2. ✅ Configuration des variables d'environnement
3. ✅ Création de l'environnement virtuel Python
4. ✅ Installation des dépendances
5. ✅ Initialisation de la base de données
6. ✅ Création des tables
7. ✅ Chargement des données par défaut
8. ✅ Configuration des logs

### Option 2: Déploiement Manuel

#### 1. Configuration de la Base de Données

Créez une base de données PostgreSQL :

```bash
createdb bellari_concept
```

Ou via psql :

```sql
CREATE DATABASE bellari_concept;
CREATE USER bellari_user WITH PASSWORD 'your_secure_password';
GRANT ALL PRIVILEGES ON DATABASE bellari_concept TO bellari_user;
```

#### 2. Variables d'Environnement

Créez un fichier `.env` à la racine du projet :

```bash
cp .env.example .env
```

Modifiez `.env` avec vos paramètres :

```env
# Database
DATABASE_URL=postgresql://bellari_user:your_password@localhost:5432/bellari_concept
PGHOST=localhost
PGPORT=5432
PGUSER=bellari_user
PGPASSWORD=your_password
PGDATABASE=bellari_concept

# Flask
SESSION_SECRET=your_very_long_random_secret_key_here
FLASK_ENV=production
FLASK_DEBUG=False

# Admin
ADMIN_INIT_ALLOWED=false

# Server
PORT=5000
HOST=0.0.0.0
```

#### 3. Environnement Virtuel

```bash
python3 -m venv .venv
source .venv/bin/activate
```

#### 4. Installation des Dépendances

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

#### 5. Initialisation de la Base de Données

```bash
# Créer les tables
python3 -c "from app import app, db; app.app_context().push(); db.create_all()"

# Charger les données par défaut
python3 init_data.py
```

#### 6. Lancement du Serveur

**Mode Développement:**
```bash
gunicorn --bind 0.0.0.0:5000 --reload main:app
```

**Mode Production:**
```bash
gunicorn --bind 0.0.0.0:5000 --workers 4 main:app
```

**Avec Logs:**
```bash
mkdir -p logs
gunicorn --bind 0.0.0.0:5000 --workers 4 \
  --access-logfile logs/access.log \
  --error-logfile logs/error.log \
  main:app
```

## 🔐 Sécurité Post-Déploiement

### ⚠️ IMPORTANT - À faire immédiatement :

1. **Changer le mot de passe admin**
   - Connexion: `/admin/login`
   - Username: `admin`
   - Password: `admin123` (À CHANGER IMMÉDIATEMENT)

2. **Générer une nouvelle SESSION_SECRET**
   ```bash
   openssl rand -hex 32
   ```
   Mettez à jour dans `.env`

3. **Désactiver l'initialisation admin**
   Dans `.env`:
   ```
   ADMIN_INIT_ALLOWED=false
   ```

## 🌐 Configuration Nginx (Production)

Créez `/etc/nginx/sites-available/bellari`:

```nginx
server {
    listen 80;
    server_name votre-domaine.com;

    location / {
        proxy_pass http://127.0.0.1:5000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }

    location /static {
        alias /chemin/vers/projet/static;
        expires 30d;
    }
}
```

Activez le site:
```bash
sudo ln -s /etc/nginx/sites-available/bellari /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl reload nginx
```

## 🔒 SSL/TLS avec Let's Encrypt

```bash
sudo apt install certbot python3-certbot-nginx
sudo certbot --nginx -d votre-domaine.com
```

## 📊 Systemd Service (Auto-start)

Créez `/etc/systemd/system/bellari.service`:

```ini
[Unit]
Description=Bellari Concept Web Application
After=network.target

[Service]
User=www-data
Group=www-data
WorkingDirectory=/chemin/vers/projet
Environment="PATH=/chemin/vers/projet/.venv/bin"
ExecStart=/chemin/vers/projet/.venv/bin/gunicorn \
    --bind 0.0.0.0:5000 \
    --workers 4 \
    --access-logfile /chemin/vers/projet/logs/access.log \
    --error-logfile /chemin/vers/projet/logs/error.log \
    main:app
Restart=always

[Install]
WantedBy=multi-user.target
```

Activez le service:
```bash
sudo systemctl daemon-reload
sudo systemctl enable bellari
sudo systemctl start bellari
sudo systemctl status bellari
```

## 💾 Sauvegardes Automatiques

### Script de Sauvegarde PostgreSQL

Créez `backup.sh`:

```bash
#!/bin/bash
BACKUP_DIR="/backups/bellari"
DATE=$(date +%Y%m%d_%H%M%S)
mkdir -p $BACKUP_DIR

pg_dump -U bellari_user bellari_concept | gzip > \
  $BACKUP_DIR/bellari_${DATE}.sql.gz

# Garder seulement les 30 dernières sauvegardes
find $BACKUP_DIR -name "bellari_*.sql.gz" -mtime +30 -delete
```

Ajoutez au crontab (sauvegarde quotidienne à 2h du matin):
```bash
0 2 * * * /chemin/vers/backup.sh
```

## 🔍 Monitoring

### Logs

```bash
# Logs en temps réel
tail -f logs/access.log
tail -f logs/error.log

# Logs systemd
sudo journalctl -u bellari -f
```

### Santé de l'Application

```bash
# Vérifier que le serveur répond
curl http://localhost:5000

# Vérifier la base de données
psql -U bellari_user -d bellari_concept -c "SELECT COUNT(*) FROM page;"
```

## 🛠️ Maintenance

### Mise à Jour du Code

```bash
git pull origin main
source .venv/bin/activate
pip install -r requirements.txt
sudo systemctl restart bellari
```

### Réinitialiser la Base de Données

⚠️ **ATTENTION: Cela supprimera toutes les données!**

```bash
python3 -c "from app import app, db; app.app_context().push(); db.drop_all(); db.create_all()"
python3 init_data.py
```

## 🐛 Dépannage

### Le serveur ne démarre pas

```bash
# Vérifier les logs
tail -n 50 logs/error.log

# Vérifier que le port n'est pas utilisé
sudo lsof -i :5000

# Tester la connexion à la base de données
psql -U bellari_user -d bellari_concept -c "SELECT 1;"
```

### Erreur "relation does not exist"

```bash
# Recréer les tables
python3 -c "from app import app, db; app.app_context().push(); db.create_all()"
```

### Problèmes de permissions

```bash
# Donner les bonnes permissions
sudo chown -R www-data:www-data /chemin/vers/projet
sudo chmod -R 755 /chemin/vers/projet
```

## 📱 Support

Pour toute question ou problème:
- Email: bellari.groupe@gmail.com
- Téléphone: +212 6 35 50 24 61

## 📝 License

Copyright © 2025 Bellari Concept. Tous droits réservés.
