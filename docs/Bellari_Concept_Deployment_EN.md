![Python 3.11](https://img.shields.io/badge/Python-3.11-blue?style=flat-square&logo=python) ![PostgreSQL 15](https://img.shields.io/badge/Database-PostgreSQL%2015-336791?style=flat-square&logo=postgresql) ![Status: Production](https://img.shields.io/badge/Status-Production-success?style=flat-square) ![License: Proprietary](https://img.shields.io/badge/License-Proprietary-red?style=flat-square) ![Owner: MOA Digital Agency](https://img.shields.io/badge/Owner-MOA%20Digital%20Agency-orange?style=flat-square)

# Bellari Concept - Deployment Guide

> **LEGAL NOTICE**
>
> This guide and the associated scripts are the exclusive property of **MOA Digital Agency**.
> Any external distribution is prohibited.

---

## 1. System Prerequisites
The CMS is optimized for deployment on Linux VPS (Ubuntu 20.04/22.04 recommended).

*   **OS:** Ubuntu 22.04 LTS (or equivalent)
*   **Language:** Python 3.11 or higher
*   **Database:** PostgreSQL 15+ (local or remote)
*   **Web Server:** Nginx (Reverse Proxy)

## 2. Automated Installation

The `deploy.sh` script automates 90% of the process.

### 2.1 Cloning and Launching
```bash
# 1. Clone the repository (Private access required)
git clone <REPO_URL>
cd bellari-concept

# 2. Make the script executable
chmod +x deploy.sh

# 3. Launch the installation
./deploy.sh
```

### 2.2 What the script does:
1.  **Verification:** Checks the Python version and the presence of `pip`.
2.  **Environment:** Requests PostgreSQL credentials and generates a secure `.env` file.
3.  **Virtualenv:** Creates a virtual environment in `.venv` and activates it.
4.  **Dependencies:** Installs packages listed in `requirements.txt`.
5.  **Database:**
    *   Verifies the PostgreSQL connection.
    *   Executes `init_db.py` to create tables and migrate schema if necessary.
    *   Creates a default administrator account if none exists.

## 3. Manual Configuration (.env)
If you do not wish to use the script, create a `.env` file at the root:

```ini
# Database
DATABASE_URL=postgresql://user:password@localhost:5432/bellari_concept

# Flask Security
SESSION_SECRET=your_very_long_and_random_secret_key
FLASK_ENV=production
FLASK_DEBUG=False

# Admin Configuration (Optional for init)
ADMIN_USERNAME=admin
ADMIN_PASSWORD=your_strong_password
ADMIN_INIT_ALLOWED=true

# Server
PORT=5000
HOST=0.0.0.0
```

## 4. Starting in Production

For production, use Gunicorn (installed via requirements.txt).

```bash
# Activate the environment
source .venv/bin/activate

# Launch with 4 workers (adjust according to CPU)
gunicorn --bind 0.0.0.0:5000 --workers 4 app:app
```

### Nginx Configuration (Recommended)
Create a server block to redirect traffic to port 5000.

```nginx
server {
    listen 80;
    server_name yourdomain.com;

    location / {
        proxy_pass http://127.0.0.1:5000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

## 5. Maintenance and Updates

### DB Initialization / Migration
The `init_db.py` script is idempotent. It can be safely rerun to:
*   Create new tables.
*   Add new columns (via the manual migration system).
*   Reset PWA settings to default.

```bash
python3 init_db.py
```

### Logs
*   **Gunicorn:** Defined during launch (e.g., `--access-logfile logs/access.log`).
*   **Flask:** Logs critical errors to `logs/error.log` (if configured).

---
*© 2024 MOA Digital Agency. All rights reserved.*
