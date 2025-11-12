#!/usr/bin/env python3
"""
Script de vérification pré-déploiement
Vérifie que tous les fichiers requis et la base de données sont prêts
"""

import os
import sys
from pathlib import Path

def check_static_files():
    """Vérifie que tous les fichiers statiques requis sont présents"""
    print("🔍 Vérification des fichiers statiques...")
    
    required_images = [
        'static/images/modern_construction__a427a1cf.jpg',
        'static/images/modern_construction__e4781d44.jpg',
        'static/images/professional_electri_984ae0e8.jpg',
        'static/images/plumber_fixing_pipes_d4c8be18.jpg',
        'static/images/painter_painting_wal_be02294b.jpg',
        'static/images/hvac_air_conditionin_8336dff9.jpg',
        'static/images/swimming_pool_mainte_0698f0ec.jpg'
    ]
    
    missing = []
    for img in required_images:
        if not os.path.exists(img):
            missing.append(img)
            print(f"  ❌ Manquant: {img}")
        else:
            size = os.path.getsize(img)
            print(f"  ✅ Trouvé: {img} ({size:,} bytes)")
    
    if missing:
        print(f"\n⚠️  {len(missing)} fichier(s) manquant(s)")
        return False
    else:
        print(f"\n✅ Tous les fichiers statiques requis sont présents ({len(required_images)} fichiers)")
        return True

def check_directories():
    """Vérifie que les répertoires requis existent"""
    print("\n🔍 Vérification des répertoires...")
    
    required_dirs = [
        'static',
        'static/images',
        'static/uploads',
        'templates',
        'templates/admin'
    ]
    
    missing = []
    for dir_path in required_dirs:
        if not os.path.exists(dir_path):
            missing.append(dir_path)
            print(f"  ❌ Manquant: {dir_path}")
        else:
            print(f"  ✅ Trouvé: {dir_path}")
    
    if missing:
        print(f"\n⚠️  {len(missing)} répertoire(s) manquant(s)")
        return False
    else:
        print(f"\n✅ Tous les répertoires requis existent")
        return True

def check_database():
    """Vérifie que la base de données contient les données essentielles"""
    print("\n🔍 Vérification de la base de données...")
    
    try:
        from app import app, db, Page, Section
        
        with app.app_context():
            pages_count = Page.query.count()
            print(f"  ℹ️  Pages dans la DB: {pages_count}")
            
            if pages_count == 0:
                print("  ⚠️  La base de données est vide!")
                print("  ℹ️  L'auto-initialisation se déclenchera au premier démarrage")
                return True
            
            home_page = Page.query.filter_by(slug='home').first()
            if not home_page:
                print("  ❌ Page 'home' non trouvée!")
                return False
            print(f"  ✅ Page 'home' trouvée (ID: {home_page.id})")
            
            hero_sections = Section.query.filter_by(
                page_id=home_page.id, 
                section_type='hero'
            ).count()
            print(f"  ℹ️  Sections Hero: {hero_sections}")
            
            expertise_sections = Section.query.filter_by(
                page_id=home_page.id, 
                section_type='expertise'
            ).count()
            print(f"  ℹ️  Sections Expertise (Notre Promesse): {expertise_sections}")
            
            if hero_sections < 2:
                print("  ❌ Sections Hero manquantes (besoin de 2: FR+EN)")
                return False
            print("  ✅ Sections Hero présentes (FR+EN)")
            
            if expertise_sections < 2:
                print("  ❌ Sections Expertise manquantes (besoin de 2: FR+EN)")
                return False
            print("  ✅ Sections Expertise (Notre Promesse) présentes (FR+EN)")
            
            all_sections = Section.query.filter_by(page_id=home_page.id).count()
            print(f"  ℹ️  Total sections page d'accueil: {all_sections}")
            
            print("\n✅ La base de données contient toutes les sections critiques")
            return True
            
    except Exception as e:
        print(f"  ❌ Erreur lors de la vérification de la DB: {e}")
        return False

def check_environment():
    """Vérifie que les variables d'environnement sont configurées"""
    print("\n🔍 Vérification des variables d'environnement...")
    
    required_env = {
        'DATABASE_URL': 'URL de connexion PostgreSQL',
        'SESSION_SECRET': 'Secret pour les sessions Flask'
    }
    
    missing = []
    for var, description in required_env.items():
        value = os.getenv(var)
        if not value:
            missing.append(var)
            print(f"  ❌ Manquant: {var} ({description})")
        else:
            masked = value[:20] + '...' if len(value) > 20 else value
            print(f"  ✅ Défini: {var} = {masked}")
    
    if missing:
        print(f"\n⚠️  {len(missing)} variable(s) d'environnement manquante(s)")
        return False
    else:
        print(f"\n✅ Toutes les variables d'environnement requises sont définies")
        return True

def main():
    """Exécute toutes les vérifications"""
    print("=" * 70)
    print("🚀 VÉRIFICATION PRÉ-DÉPLOIEMENT - BELLARI CONCEPT")
    print("=" * 70)
    
    results = {
        'Répertoires': check_directories(),
        'Fichiers statiques': check_static_files(),
        'Variables d\'environnement': check_environment(),
        'Base de données': check_database()
    }
    
    print("\n" + "=" * 70)
    print("📊 RÉSUMÉ DE LA VÉRIFICATION")
    print("=" * 70)
    
    for check, passed in results.items():
        status = "✅ PASS" if passed else "❌ FAIL"
        print(f"{status} - {check}")
    
    all_passed = all(results.values())
    
    print("=" * 70)
    if all_passed:
        print("✅ TOUTES LES VÉRIFICATIONS ONT RÉUSSI!")
        print("\n🎉 Le site est prêt pour le déploiement sur VPS")
        print("\nProchaines étapes:")
        print("  1. Copier tous les fichiers sur le VPS")
        print("  2. Installer les dépendances: uv sync")
        print("  3. Configurer les variables d'environnement")
        print("  4. Démarrer avec: uv run gunicorn --bind 0.0.0.0:8000 --workers 4 main:app")
        print("  5. Vérifier que le hero slider et la section 'Notre Promesse' s'affichent")
        return 0
    else:
        print("❌ CERTAINES VÉRIFICATIONS ONT ÉCHOUÉ!")
        print("\n⚠️  Veuillez corriger les problèmes avant le déploiement")
        return 1

if __name__ == '__main__':
    sys.exit(main())
