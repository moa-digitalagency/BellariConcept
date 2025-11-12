# ✅ Checklist de Déploiement VPS - Bellari Concept

## 🔧 Avant le Déploiement

### 1. Vérifier les Fichiers Requis
- [ ] Tous les fichiers du dossier `/static/images/` sont présents
- [ ] Le fichier `static/logo.png` existe
- [ ] Le dossier `static/uploads/` est créé avec les permissions d'écriture
- [ ] Le fichier `templates/` contient tous les templates HTML

### 2. Configuration de la Base de Données
- [ ] PostgreSQL est installé et démarré
- [ ] Variable d'environnement `DATABASE_URL` est configurée
  ```bash
  export DATABASE_URL="postgresql://user:password@localhost/bellari_db"
  ```
- [ ] La base de données existe :
  ```bash
  psql -c "CREATE DATABASE bellari_db;"
  ```

### 3. Variables d'Environnement Requises
Créer un fichier `.env` avec :
```bash
# Session Secret (générer avec: python -c "import secrets; print(secrets.token_hex(32))")
SESSION_SECRET=votre_secret_key_ici

# Database URL
DATABASE_URL=postgresql://user:password@localhost/bellari_db

# Pour permettre l'init manuelle (optionnel, déconseillé en prod)
ADMIN_INIT_ALLOWED=false
```

## 🚀 Installation sur VPS

### 1. Installer les Dépendances Système
```bash
# Ubuntu/Debian
sudo apt update
sudo apt install python3 python3-pip python3-venv postgresql postgresql-contrib nginx
```

### 2. Cloner le Projet
```bash
cd /var/www/
git clone [votre-repo] bellari-concept
cd bellari-concept
```

### 3. Installer uv et les Dépendances Python
```bash
# Installer uv
curl -LsSf https://astral.sh/uv/install.sh | sh

# Installer les dépendances
uv sync
```

### 4. Vérifier les Fichiers Statiques
```bash
# Vérifier que toutes les images sont présentes
ls -la static/images/
# Devrait contenir:
# - modern_construction__a427a1cf.jpg
# - modern_construction__e4781d44.jpg
# - professional_electri_984ae0e8.jpg
# - plumber_fixing_pipes_d4c8be18.jpg
# - painter_painting_wal_be02294b.jpg
# - hvac_air_conditionin_8336dff9.jpg
# - swimming_pool_mainte_0698f0ec.jpg

# Créer le dossier uploads
mkdir -p static/uploads
chmod 755 static/uploads
```

### 5. Initialisation Automatique de la Base de Données
**✨ IMPORTANT : L'application s'initialise automatiquement !**

Au premier démarrage, l'application va :
- ✅ Créer toutes les tables nécessaires
- ✅ Insérer les pages (home, about, services, etc.)
- ✅ Insérer TOUTES les sections incluant :
  - **Hero Section** (slider principal)
  - **Section "Notre Promesse"** (expertise)
  - Sections features, why_us, cta
- ✅ Créer un compte admin par défaut (admin/admin123)

**Aucune action manuelle requise !**

Pour vérification manuelle (optionnel) :
```bash
# Vérifier que les sections existent
uv run python -c "from auto_init import ensure_database_initialized; ensure_database_initialized()"
```

### 6. Tester l'Application Localement
```bash
# Démarrer avec gunicorn
uv run gunicorn --bind 0.0.0.0:8000 --workers 4 main:app

# Visiter http://votre-ip:8000
# Vérifier que le hero slider s'affiche
# Vérifier que la section "Notre Promesse" s'affiche
```

## 🔍 Vérifications Post-Déploiement

### 1. Vérifier les Sections Critiques
Ouvrir le site et vérifier :
- [ ] **Hero Slider** s'affiche avec l'image de fond
- [ ] **Section "Notre Promesse"** (avec image et texte) est visible
- [ ] Boutons "NOS SERVICES" et "CONTACTEZ-NOUS" fonctionnent
- [ ] Toutes les 6 cartes de services s'affichent avec images
- [ ] Changement de langue FR/EN fonctionne

### 2. Vérifier la Base de Données
```bash
# Se connecter à PostgreSQL
psql -U postgres -d bellari_db

# Vérifier les sections
SELECT section_type, language_code, heading FROM section WHERE page_id = (SELECT id FROM page WHERE slug = 'home');
```

Vous devriez voir :
```
 section_type | language_code |              heading               
--------------+---------------+------------------------------------
 hero         | fr            | BELLARI CONCEPT
 hero         | en            | BELLARI CONCEPT
 expertise    | fr            | Nous vous aidons à réaliser...
 expertise    | en            | We help you realize...
 features     | fr            | Notre Expertise
 features     | en            | Our Expertise
 why_us       | fr            | Pourquoi Bellari Concept ?
 why_us       | en            | Why Bellari Concept?
 cta          | fr            | Prêt à Démarrer Votre Projet ?
 cta          | en            | Ready to Start Your Project?
```

### 3. Vérifier les Images
```bash
# Toutes les images doivent être accessibles
curl -I http://localhost:8000/static/images/modern_construction__e4781d44.jpg
# Devrait retourner HTTP 200
```

### 4. Tester le Panel Admin
- [ ] Aller sur `/admin/login`
- [ ] Se connecter avec admin/admin123
- [ ] **CHANGER LE MOT DE PASSE IMMÉDIATEMENT !**
- [ ] Vérifier que toutes les pages et sections sont présentes

## 🔒 Sécurité Post-Installation

### 1. Changer le Mot de Passe Admin
```python
# Via Python shell
uv run python
>>> from app import app, db, User
>>> from werkzeug.security import generate_password_hash
>>> with app.app_context():
...     admin = User.query.filter_by(username='admin').first()
...     admin.password_hash = generate_password_hash('NOUVEAU_MOT_DE_PASSE_FORT')
...     db.session.commit()
```

### 2. Désactiver l'Init Manuelle
Dans `.env` :
```bash
ADMIN_INIT_ALLOWED=false
```

## 🌐 Configuration Nginx (Production)

```nginx
server {
    listen 80;
    server_name votre-domaine.com;

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }

    location /static/ {
        alias /var/www/bellari-concept/static/;
        expires 30d;
        add_header Cache-Control "public, immutable";
    }
}
```

## 🔄 Service Systemd (Auto-Démarrage)

Créer `/etc/systemd/system/bellari.service` :
```ini
[Unit]
Description=Bellari Concept Website
After=network.target postgresql.service

[Service]
User=www-data
Group=www-data
WorkingDirectory=/var/www/bellari-concept
Environment="PATH=/root/.local/bin:/usr/local/bin:/usr/bin:/bin"
ExecStart=/root/.cargo/bin/uv run gunicorn --bind 0.0.0.0:8000 --workers 4 --timeout 120 main:app
Restart=always

[Install]
WantedBy=multi-user.target
```

Activer le service :
```bash
sudo systemctl daemon-reload
sudo systemctl enable bellari
sudo systemctl start bellari
sudo systemctl status bellari
```

## 🐛 Dépannage

### Problème : Hero Section ne s'affiche pas
**Cause** : Base de données vide
**Solution** :
```bash
# Forcer la réinitialisation
uv run python auto_init.py
# Redémarrer l'application
sudo systemctl restart bellari
```

### Problème : Section "Notre Promesse" manquante
**Cause** : Sections 'expertise' manquantes en DB
**Solution** :
```bash
# Vérifier les sections
psql -U postgres -d bellari_db -c "SELECT COUNT(*) FROM section WHERE section_type='expertise';"
# Devrait retourner 2 (FR + EN)

# Si 0, réinitialiser
uv run python auto_init.py
```

### Problème : Images ne s'affichent pas
**Cause** : Fichiers manquants ou permissions incorrectes
**Solution** :
```bash
# Vérifier les permissions
ls -la static/images/
chmod 755 static/images/
chmod 644 static/images/*

# Vérifier que les fichiers existent
ls static/images/*.jpg
```

### Problème : 500 Internal Server Error
**Cause** : Database URL invalide ou DB non accessible
**Solution** :
```bash
# Tester la connexion DB
psql $DATABASE_URL -c "SELECT 1;"

# Vérifier les logs
journalctl -u bellari -n 100
```

## ✅ Checklist Finale

- [ ] Hero slider s'affiche correctement
- [ ] Section "Notre Promesse" visible avec image
- [ ] Toutes les 6 cartes de services visibles
- [ ] Changement de langue fonctionne
- [ ] Admin accessible et mot de passe changé
- [ ] Images chargent correctement
- [ ] Formulaire de contact fonctionne
- [ ] Site accessible via le domaine
- [ ] SSL/HTTPS configuré (recommandé)
- [ ] Sauvegardes automatiques de la DB configurées

## 📞 Support

Si problèmes persistent :
1. Vérifier les logs : `journalctl -u bellari -f`
2. Vérifier la base de données
3. Tester en mode debug local
4. Vérifier les permissions des fichiers
