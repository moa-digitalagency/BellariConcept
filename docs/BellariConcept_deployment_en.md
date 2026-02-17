> **© MOA Digital Agency (myoneart.com) - Author: Aisance KALONJI**
> *This code is the exclusive property of MOA Digital Agency. Internal use only. Any unauthorized reproduction or distribution is strictly prohibited.*

[Passer à la version Française](./BellariConcept_deployment.md)

# Deployment Guide - Bellari Concept

## 1. System Requirements
*   **OS:** Ubuntu 22.04 LTS (Recommended) or Debian 11+.
*   **Language:** Python 3.11 or higher.
*   **Web Server:** Nginx (Reverse Proxy).
*   **Database:** SQLite (Default) or PostgreSQL (Production).
*   **Access:** Root or sudo privileges.

## 2. Automated Deployment
The `deploy.sh` script automates dependency installation and initial configuration.

```bash
# Make the script executable
chmod +x deploy.sh

# Run deployment
./deploy.sh
```

The script will:
1.  Check Python version.
2.  Create a virtual environment `.venv`.
3.  Install dependencies via `uv` (if available) or `pip`.
4.  Prompt for database credentials.
5.  Generate the `.env` file if missing.

## 3. Manual Deployment
If you cannot use the automatic script, follow these steps:

### 3.1 Installation
```bash
# 1. Clone the repository (if applicable)
git clone <private_repo_url>
cd bellari-concept

# 2. Create virtual environment
python3 -m venv .venv
source .venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt
```

### 3.2 Configuration
Create a `.env` file at the root:
```ini
SESSION_SECRET=your_very_long_secret_key
DATABASE_URL=sqlite:///bellari.db
ADMIN_USERNAME=admin
ADMIN_PASSWORD=your_strong_password
FLASK_ENV=production
```

### 3.3 Initialization
Run the initialization script to create tables and the admin user:
```bash
python init_db.py
```
*Note: This script also handles manual schema migrations.*

## 4. Verification
Before starting the server, use the verification script:
```bash
python verify_deployment.py
```
It will scan:
*   Folder structure (`static`, `templates`).
*   Database connection.
*   Presence of critical files.

## 5. Production Server (Gunicorn)
Start the application with Gunicorn:
```bash
gunicorn -w 4 -b 0.0.0.0:8000 app:app
```

Then configure Nginx to proxy traffic from port 80/443 to port 8000.
