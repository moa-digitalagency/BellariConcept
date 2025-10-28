# 🔧 Deployment Fix - DATABASE_URL Error

## ❌ Current Problem

Your `.env` file has:
```bash
DATABASE_URL=postgresql://:@localhost:5432/bellari_concept
```

The username and password are **missing** between `://` and `@`!

## ✅ The Fix

Replace your entire `.env` file content with this:

```bash
# Database Configuration
DATABASE_URL=postgresql://bellari:bellari54321@localhost:5432/bellari_concept
PGHOST=localhost
PGPORT=5432
PGUSER=bellari
PGPASSWORD=bellari54321
PGDATABASE=bellari_concept

# Flask Configuration
SESSION_SECRET=dbd4cdd5c46f7727596d8829bd93b221aae4d3526560d7f69ac93bab8e48c7c9
FLASK_ENV=production
FLASK_DEBUG=False

# Admin Configuration
ADMIN_INIT_ALLOWED=false

# Server Configuration
PORT=5000
HOST=0.0.0.0
```

## 🚀 Quick Copy Command

On your VPS, run this command to fix it instantly:

```bash
cat > .env << 'EOF'
# Database Configuration
DATABASE_URL=postgresql://bellari:bellari54321@localhost:5432/bellari_concept
PGHOST=localhost
PGPORT=5432
PGUSER=bellari
PGPASSWORD=bellari54321
PGDATABASE=bellari_concept

# Flask Configuration
SESSION_SECRET=dbd4cdd5c46f7727596d8829bd93b221aae4d3526560d7f69ac93bab8e48c7c9
FLASK_ENV=production
FLASK_DEBUG=False

# Admin Configuration
ADMIN_INIT_ALLOWED=false

# Server Configuration
PORT=5000
HOST=0.0.0.0
EOF
```

## ✅ Then Run Deployment

```bash
./deploy.sh
```

## 📝 What Changed

**Before:**
```
DATABASE_URL=postgresql://:@localhost:5432/bellari_concept
                        ^^
                   Missing user:pass
```

**After:**
```
DATABASE_URL=postgresql://bellari:bellari54321@localhost:5432/bellari_concept
                        ^^^^^^^^^^^^^^^^^^^
                        User and password added
```

That's it! The deployment will work now. 🎉
