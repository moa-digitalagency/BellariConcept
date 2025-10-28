#!/bin/bash

echo "========================================"
echo "  Fix .env File - Bellari Concept      "
echo "========================================"
echo ""

# Check if .env exists
if [ ! -f .env ]; then
    echo "❌ .env file not found!"
    echo "Run ./deploy.sh to create a new one."
    exit 1
fi

echo "Current .env file found. Let's fix the DATABASE_URL..."
echo ""

# Backup current .env
cp .env .env.backup
echo "✓ Backup created: .env.backup"
echo ""

# Read current values from .env
source .env

echo "Current configuration:"
echo "  PGUSER: ${PGUSER}"
echo "  PGDATABASE: ${PGDATABASE}"
echo "  PGHOST: ${PGHOST}"
echo "  PGPORT: ${PGPORT}"
echo ""

# Ask if user wants to keep these values or enter new ones
read -p "Do you want to keep these database settings? (y/n): " keep_settings

if [[ $keep_settings =~ ^[Nn]$ ]]; then
    echo ""
    echo "Enter new database configuration:"
    read -p "Database host [${PGHOST}]: " new_host
    new_host=${new_host:-${PGHOST}}
    
    read -p "Database port [${PGPORT}]: " new_port
    new_port=${new_port:-${PGPORT}}
    
    read -p "Database name [${PGDATABASE}]: " new_db
    new_db=${new_db:-${PGDATABASE}}
    
    read -p "Database user [${PGUSER}]: " new_user
    new_user=${new_user:-${PGUSER}}
    
    read -s -p "Database password: " new_password
    echo ""
    
    PGHOST=$new_host
    PGPORT=$new_port
    PGDATABASE=$new_db
    PGUSER=$new_user
    PGPASSWORD=$new_password
fi

# Generate new SESSION_SECRET if it's empty or too short
if [ -z "$SESSION_SECRET" ] || [ ${#SESSION_SECRET} -lt 32 ]; then
    echo "Generating new SESSION_SECRET..."
    SESSION_SECRET=$(openssl rand -hex 32)
fi

# Build correct DATABASE_URL
DATABASE_URL="postgresql://${PGUSER}:${PGPASSWORD}@${PGHOST}:${PGPORT}/${PGDATABASE}"

# Create new .env file
cat > .env << EOF
# Database Configuration
DATABASE_URL=${DATABASE_URL}
PGHOST=${PGHOST}
PGPORT=${PGPORT}
PGUSER=${PGUSER}
PGPASSWORD=${PGPASSWORD}
PGDATABASE=${PGDATABASE}

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

echo ""
echo "✓ .env file has been fixed!"
echo ""
echo "New DATABASE_URL format:"
echo "  ${DATABASE_URL}"
echo ""
echo "You can now run: ./deploy.sh"
echo ""
