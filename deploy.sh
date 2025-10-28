#!/bin/bash

set -e

echo "========================================"
echo "  BELLARI CONCEPT - Deployment Script  "
echo "========================================"
echo ""

PROJECT_NAME="bellari-concept"
PYTHON_VERSION="3.11"
VENV_DIR=".venv"
LOG_DIR="logs"

echo "[1/8] Checking system requirements..."
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python ${PYTHON_VERSION} or higher."
    exit 1
fi

PYTHON_CMD=$(command -v python3)
CURRENT_VERSION=$($PYTHON_CMD --version | cut -d' ' -f2)
echo "✓ Python found: $CURRENT_VERSION"

if ! command -v pip3 &> /dev/null; then
    echo "❌ pip3 is not installed. Please install pip3."
    exit 1
fi
echo "✓ pip3 found"

echo ""
echo "[2/8] Setting up environment variables..."

if [ ! -f .env ]; then
    echo "Creating .env file from template..."
    echo "Please provide the following information:"
    echo ""
    read -p "Database host [localhost]: " db_host
    db_host=${db_host:-localhost}
    
    read -p "Database port [5432]: " db_port
    db_port=${db_port:-5432}
    
    read -p "Database name [bellari_concept]: " db_name
    db_name=${db_name:-bellari_concept}
    
    read -p "Database user: " db_user
    read -s -p "Database password: " db_password
    echo ""
    
    SESSION_SECRET=$(openssl rand -hex 32)
    
    cat > .env << EOF
# Database Configuration
DATABASE_URL=postgresql://${db_user}:${db_password}@${db_host}:${db_port}/${db_name}
PGHOST=${db_host}
PGPORT=${db_port}
PGUSER=${db_user}
PGPASSWORD=${db_password}
PGDATABASE=${db_name}

# Flask Configuration
SESSION_SECRET=${SESSION_SECRET}
FLASK_ENV=production
FLASK_DEBUG=False

# Admin Configuration
ADMIN_INIT_ALLOWED=false

# Server Configuration
PORT=5000
HOST=0.0.0.0
EOF
    echo "✓ .env file created with your configuration"
else
    echo "✓ .env file already exists"
fi

if [ -f .env ]; then
    source .env
    echo "✓ Environment variables loaded"
    
    # Validate DATABASE_URL format
    if [ -z "$DATABASE_URL" ]; then
        echo "❌ DATABASE_URL is empty in .env file"
        echo "Please run: ./fix_env.sh to fix your .env file"
        exit 1
    fi
    
    if [[ ! "$DATABASE_URL" =~ ^postgresql:// ]]; then
        echo "❌ DATABASE_URL has incorrect format in .env file"
        echo "Expected format: postgresql://user:password@host:port/database"
        echo "Current value: $DATABASE_URL"
        echo ""
        echo "Please run: ./fix_env.sh to fix your .env file"
        exit 1
    fi
    
    echo "✓ DATABASE_URL format validated"
else
    echo "❌ .env file not found"
    exit 1
fi

echo ""
echo "[3/8] Creating virtual environment..."
if [ ! -d "$VENV_DIR" ]; then
    $PYTHON_CMD -m venv $VENV_DIR
    echo "✓ Virtual environment created at $VENV_DIR"
else
    echo "✓ Virtual environment already exists"
fi

source $VENV_DIR/bin/activate
echo "✓ Virtual environment activated"

echo ""
echo "[4/8] Upgrading pip..."
pip install --upgrade pip
echo "✓ pip upgraded"

echo ""
echo "[5/8] Installing Python dependencies..."
if [ -f requirements.txt ]; then
    pip install -r requirements.txt
    echo "✓ Dependencies installed from requirements.txt"
else
    echo "Creating requirements.txt..."
    cat > requirements.txt << EOF
email-validator==2.1.0
flask==3.0.0
flask-login==0.6.3
flask-sqlalchemy==3.1.1
gunicorn==21.2.0
pillow==10.1.0
psycopg2-binary==2.9.9
python-dotenv==1.0.0
werkzeug==3.0.1
EOF
    pip install -r requirements.txt
    echo "✓ Dependencies installed"
fi

echo ""
echo "[6/8] Checking PostgreSQL database connection..."
if [ -z "$DATABASE_URL" ]; then
    echo "❌ DATABASE_URL not set in environment variables"
    echo "Please set DATABASE_URL in .env file"
    exit 1
fi

echo "Testing database connection..."
python3 << EOF
import os
import sys
try:
    from sqlalchemy import create_engine
    engine = create_engine(os.getenv('DATABASE_URL'))
    with engine.connect() as conn:
        print("✓ Database connection successful")
except Exception as e:
    print(f"❌ Database connection failed: {e}")
    print("Please check your DATABASE_URL in .env file")
    sys.exit(1)
EOF

echo ""
echo "[7/8] Initializing database schema..."
python3 << EOF
from app import app, db
import os

with app.app_context():
    try:
        db.create_all()
        print("✓ Database tables created successfully")
    except Exception as e:
        print(f"❌ Error creating database tables: {e}")
        import sys
        sys.exit(1)
EOF

echo ""
echo "Do you want to initialize the database with default data? (y/n)"
read -p "This will create admin user and sample content: " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    python3 init_data.py
    echo "✓ Database initialized with default data"
    echo ""
    echo "╔════════════════════════════════════════╗"
    echo "║   ADMIN CREDENTIALS (CHANGE ASAP!)     ║"
    echo "╠════════════════════════════════════════╣"
    echo "║ Username: admin                        ║"
    echo "║ Password: admin123                     ║"
    echo "║ URL: /admin/login                      ║"
    echo "╚════════════════════════════════════════╝"
    echo ""
fi

echo ""
echo "[8/8] Setting up log directory..."
if [ ! -d "$LOG_DIR" ]; then
    mkdir -p $LOG_DIR
    echo "✓ Log directory created at $LOG_DIR"
else
    echo "✓ Log directory already exists"
fi

echo ""
echo "========================================"
echo "   Deployment Complete! ✓              "
echo "========================================"
echo ""
echo "To start the application:"
echo ""
echo "  Development mode (with auto-reload):"
echo "    source $VENV_DIR/bin/activate"
echo "    gunicorn --bind 0.0.0.0:5000 --reload main:app"
echo ""
echo "  Production mode:"
echo "    source $VENV_DIR/bin/activate"
echo "    gunicorn --bind 0.0.0.0:5000 --workers 4 main:app"
echo ""
echo "  With logging:"
echo "    gunicorn --bind 0.0.0.0:5000 --workers 4 \\"
echo "      --access-logfile $LOG_DIR/access.log \\"
echo "      --error-logfile $LOG_DIR/error.log \\"
echo "      main:app"
echo ""
echo "The application will be available at: http://localhost:5000"
echo ""
echo "⚠️  IMPORTANT POST-DEPLOYMENT STEPS:"
echo "  1. Change the admin password immediately at /admin/login"
echo "  2. Update .env with production-ready SECRET_KEY"
echo "  3. Review and customize the content in the admin panel"
echo "  4. Configure your web server (nginx/apache) for production"
echo "  5. Set up SSL/TLS certificates for HTTPS"
echo "  6. Configure firewall rules"
echo "  7. Set up regular database backups"
echo ""
