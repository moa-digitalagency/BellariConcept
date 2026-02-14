import os
from sqlalchemy import text, inspect
from werkzeug.security import generate_password_hash

def check_and_migrate_schema():
    """
    Checks the database schema and applies migrations if necessary.
    This is a manual migration system to ensure robustness on VPS.
    """
    from app import app, db

    print("Checking database schema...")
    with app.app_context():
        inspector = inspect(db.engine)
        existing_tables = inspector.get_table_names()

        # 1. Ensure Tables Exist
        db.create_all()
        print("✅ Tables checked/created.")

        # 2. Check Columns (Manual Migration Logic)
        # Define critical columns to check. Format: Table -> [(Column, Type)]
        schema_checks = {
            'user': [
                ('username', 'VARCHAR(80)'),
                ('password_hash', 'VARCHAR(255)'),
                ('created_at', 'TIMESTAMP')
            ],
            'page': [
                ('slug', 'VARCHAR(100)'),
                ('title', 'VARCHAR(200)'),
                ('meta_description', 'VARCHAR(300)'),
                ('is_active', 'BOOLEAN'),
                ('created_at', 'TIMESTAMP'),
                ('updated_at', 'TIMESTAMP')
            ],
            'section': [
                ('page_id', 'INTEGER'),
                ('section_type', 'VARCHAR(50)'),
                ('language_code', 'VARCHAR(5)'),
                ('order_index', 'INTEGER'),
                ('heading', 'VARCHAR(300)'),
                ('subheading', 'VARCHAR(300)'),
                ('content', 'TEXT'),
                ('button_text', 'VARCHAR(100)'),
                ('button_link', 'VARCHAR(200)'),
                ('image_url', 'VARCHAR(300)'),
                ('background_image', 'VARCHAR(300)'),
                ('background_color', 'VARCHAR(20)'),
                ('is_active', 'BOOLEAN'),
                ('created_at', 'TIMESTAMP')
            ],
            'image': [
                ('filename', 'VARCHAR(300)'),
                ('original_filename', 'VARCHAR(300)'),
                ('alt_text', 'VARCHAR(200)'),
                ('file_size', 'INTEGER'),
                ('width', 'INTEGER'),
                ('height', 'INTEGER'),
                ('uploaded_at', 'TIMESTAMP')
            ],
            'site_settings': [
                ('key', 'VARCHAR(100)'),
                ('value', 'TEXT'),
                ('description', 'VARCHAR(300)'),
                ('updated_at', 'TIMESTAMP')
            ]
        }

        # Handling for PostgreSQL (VPS) vs SQLite (Dev)
        for table, columns in schema_checks.items():
            if table in existing_tables:
                # inspector.get_columns returns a list of dicts with 'name', 'type', etc.
                existing_columns = [c['name'] for c in inspector.get_columns(table)]
                for col_name, col_type in columns:
                    if col_name not in existing_columns:
                        print(f"⚠️  Column '{col_name}' missing in table '{table}'. Adding...")
                        try:
                            # For SQLite, ALTER TABLE ADD COLUMN is limited but works for simple types in newer versions.
                            # For Postgres, standard syntax works.
                            stmt = f"ALTER TABLE {table} ADD COLUMN {col_name} {col_type}"

                            # Execute raw SQL
                            with db.engine.connect() as conn:
                                conn.execute(text(stmt))
                                conn.commit()

                            print(f"✅ Column '{col_name}' added to '{table}'.")
                        except Exception as e:
                            print(f"❌ Failed to add column '{col_name}' to '{table}': {e}")

def init_pwa_settings():
    """
    Initialize PWA settings in SiteSettings table if they don't exist.
    """
    from app import app, db, SiteSettings

    print("Checking PWA settings...")
    with app.app_context():
        # Default PWA settings
        defaults = {
            'pwa_enabled': 'false',
            'pwa_display_mode': 'default',  # 'default' or 'custom'
            'pwa_app_name': 'Bellari Concept',
            'pwa_icon_url': '/static/logo.png',
            'pwa_short_name': 'Bellari',
            'pwa_theme_color': '#ffffff',
            'pwa_background_color': '#ffffff',
            'pwa_description': 'Bellari Concept - Luxury Interior Design',
            'pwa_start_url': '/',
            'site_favicon': '/static/logo.png',
            'whatsapp_number': '243860493345',
            'consultation_url': 'https://tidycal.com/moamyoneart/consultation-gratuite-15-min'
        }

        changes_made = False
        for key, value in defaults.items():
            setting = SiteSettings.query.filter_by(key=key).first()
            if not setting:
                print(f"Adding default setting: {key} = {value}")
                db.session.add(SiteSettings(key=key, value=value))
                changes_made = True
            else:
                pass # Setting exists

        if changes_made:
            db.session.commit()
            print("PWA settings initialized.")
        else:
            print("PWA settings up to date.")

def init_content():
    """
    Auto-initializes the database with default content if it's empty.
    """
    from app import app, db, User, Page, Section

    print("Checking default content...")
    with app.app_context():
        try:
            if not Page.query.first():
                print("🔧 Initializing default content (Pages, Sections)...")

                pages_data = [
                    {'slug': 'home', 'title': 'Bellari Concept - Design d\'intérieur de luxe', 'meta_description': 'Transformez votre espace avec les services de design d\'intérieur de luxe de Bellari Concept'},
                    {'slug': 'about', 'title': 'À propos - Bellari Concept', 'meta_description': 'Découvrez notre philosophie de design et notre expertise'},
                    {'slug': 'services', 'title': 'Nos Services - Bellari Concept', 'meta_description': 'Explorez nos services complets de design d\'intérieur'},
                    {'slug': 'portfolio', 'title': 'Portfolio - Bellari Concept', 'meta_description': 'Découvrez nos magnifiques projets de design d\'intérieur'},
                    {'slug': 'contact', 'title': 'Contactez-nous - Bellari Concept', 'meta_description': 'Contactez notre équipe de design'}
                ]

                for page_data in pages_data:
                    page = Page(**page_data)
                    db.session.add(page)
                db.session.commit()

                # ... sections ...
                home_page = Page.query.filter_by(slug='home').first()
                if home_page:
                    sections_data = [
                        {
                            'page_id': home_page.id,
                            'section_type': 'hero',
                            'language_code': 'fr',
                            'heading': 'BELLARI CONCEPT',
                            'subheading': 'Construction & Rénovation à Marrakech',
                            'content': 'Votre partenaire de confiance pour tous vos projets de construction, rénovation et services techniques à Marrakech',
                            'order_index': 0
                        },
                        {
                            'page_id': home_page.id,
                            'section_type': 'hero',
                            'language_code': 'en',
                            'heading': 'BELLARI CONCEPT',
                            'subheading': 'Construction & Renovation in Marrakech',
                            'content': 'Your trusted partner for all construction, renovation and technical services projects in Marrakech',
                            'order_index': 0
                        },
                        {
                            'page_id': home_page.id,
                            'section_type': 'expertise',
                            'language_code': 'fr',
                            'heading': 'Nous vous aidons à réaliser les projets de vos rêves',
                            'subheading': 'Excellence et expertise au service de vos ambitions',
                            'content': 'Avec Bellari Concept, chaque projet est un gage de qualité. Notre équipe spécialisée offre une maîtrise technique inégalée, allant de la construction à l\'entretien de piscines. Nous mettons l\'excellence au cœur de tout ce que nous faisons, transformant vos visions en réalités durables et esthétiquement plaisantes.',
                            'image_url': '/static/images/modern_construction__e4781d44.jpg',
                            'order_index': 1
                        },
                        {
                            'page_id': home_page.id,
                            'section_type': 'expertise',
                            'language_code': 'en',
                            'heading': 'We help you realize your dream projects',
                            'subheading': 'Excellence and expertise at the service of your ambitions',
                            'content': 'With Bellari Concept, each project is a guarantee of quality. Our specialized team offers unparalleled technical mastery, from construction to pool maintenance. We put excellence at the heart of everything we do, transforming your visions into lasting and aesthetically pleasing realities.',
                            'image_url': '/static/images/modern_construction__e4781d44.jpg',
                            'order_index': 1
                        },
                        {
                            'page_id': home_page.id,
                            'section_type': 'features',
                            'language_code': 'fr',
                            'heading': 'Notre Expertise',
                            'content': 'Design Résidentiel • Espaces Commerciaux • Rénovations de Luxe • Mobilier Sur Mesure • Curation d\'Art • Gestion de Projet',
                            'order_index': 2
                        },
                        {
                            'page_id': home_page.id,
                            'section_type': 'features',
                            'language_code': 'en',
                            'heading': 'Our Expertise',
                            'content': 'Residential Design • Commercial Spaces • Luxury Renovations • Custom Furniture • Art Curation • Project Management',
                            'order_index': 2
                        },
                        {
                            'page_id': home_page.id,
                            'section_type': 'why_us',
                            'language_code': 'fr',
                            'heading': 'Pourquoi Bellari Concept ?',
                            'subheading': 'Qualité Garantie • Respect des Délais • Équipe Expérimentée',
                            'content': 'Des matériaux de première qualité et un savoir-faire professionnel. Vos projets livrés dans les temps convenus avec des professionnels qualifiés et passionnés.',
                            'order_index': 3
                        },
                        {
                            'page_id': home_page.id,
                            'section_type': 'why_us',
                            'language_code': 'en',
                            'heading': 'Why Bellari Concept?',
                            'subheading': 'Guaranteed Quality • On-Time Delivery • Experienced Team',
                            'content': 'Premium materials and professional craftsmanship. Your projects delivered on agreed timelines with qualified and passionate professionals.',
                            'order_index': 3
                        },
                        {
                            'page_id': home_page.id,
                            'section_type': 'cta',
                            'language_code': 'fr',
                            'heading': 'Prêt à Démarrer Votre Projet ?',
                            'subheading': 'Contactez-nous dès aujourd\'hui pour un devis gratuit et personnalisé',
                            'content': '',
                            'order_index': 4
                        },
                        {
                            'page_id': home_page.id,
                            'section_type': 'cta',
                            'language_code': 'en',
                            'heading': 'Ready to Start Your Project?',
                            'subheading': 'Contact us today for a free personalized quote',
                            'content': '',
                            'order_index': 4
                        }
                    ]

                    for section_data in sections_data:
                        section = Section(**section_data)
                        db.session.add(section)
                    db.session.commit()

                about_page = Page.query.filter_by(slug='about').first()
                if about_page:
                    sections_data = [
                        {
                            'page_id': about_page.id,
                            'section_type': 'hero',
                            'language_code': 'fr',
                            'heading': 'À Propos de Bellari Concept',
                            'subheading': 'Excellence en Design Depuis 2010',
                            'order_index': 0
                        },
                        {
                            'page_id': about_page.id,
                            'section_type': 'hero',
                            'language_code': 'en',
                            'heading': 'About Bellari Concept',
                            'subheading': 'Design Excellence Since 2010',
                            'order_index': 0
                        },
                        {
                            'page_id': about_page.id,
                            'section_type': 'text',
                            'language_code': 'fr',
                            'heading': 'Notre Histoire',
                            'content': 'Fondé avec une passion pour la création d\'espaces exceptionnels, Bellari Concept s\'est établi comme un leader dans le design d\'intérieur de luxe. Notre philosophie combine élégance intemporelle et innovation contemporaine, résultant en des espaces à la fois beaux et fonctionnels.',
                            'order_index': 1
                        },
                        {
                            'page_id': about_page.id,
                            'section_type': 'text',
                            'language_code': 'en',
                            'heading': 'Our Story',
                            'content': 'Founded with a passion for creating exceptional spaces, Bellari Concept has established itself as a leader in luxury interior design. Our philosophy combines timeless elegance with contemporary innovation, resulting in spaces that are both beautiful and functional.',
                            'order_index': 1
                        }
                    ]

                    for section_data in sections_data:
                        section = Section(**section_data)
                        db.session.add(section)
                    db.session.commit()

                services_page = Page.query.filter_by(slug='services').first()
                if services_page:
                    sections_data = [
                        {
                            'page_id': services_page.id,
                            'section_type': 'hero',
                            'language_code': 'fr',
                            'heading': 'Nos Services',
                            'subheading': 'Des solutions complètes pour tous vos besoins en construction et rénovation',
                            'order_index': 0
                        },
                        {
                            'page_id': services_page.id,
                            'section_type': 'hero',
                            'language_code': 'en',
                            'heading': 'Our Services',
                            'subheading': 'Comprehensive Design Solutions',
                            'order_index': 0
                        }
                    ]

                    for section_data in sections_data:
                        section = Section(**section_data)
                        db.session.add(section)
                    db.session.commit()

                print("✅ Default content initialized.")
            else:
                print("Default content already exists.")

            # Check Admin User
            if not User.query.first():
                admin_username = os.getenv('ADMIN_USERNAME')
                admin_password = os.getenv('ADMIN_PASSWORD')

                if admin_username and admin_password:
                    if len(admin_password) < 8:
                        print("⚠️  ADMIN_PASSWORD must be at least 8 characters!")
                        print("❌ Skipping admin user creation for security reasons")
                    else:
                        admin = User(
                            username=admin_username,
                            password_hash=generate_password_hash(admin_password)
                        )
                        db.session.add(admin)
                        db.session.commit()
                        print(f"✅ Admin user created: {admin_username}")
                else:
                    print("ℹ️  No admin credentials in environment variables")
                    print("ℹ️  Set ADMIN_USERNAME and ADMIN_PASSWORD to create an admin user")
            else:
                # User exists, good.
                pass

        except Exception as e:
            print(f"❌ Error during content initialization: {e}")

if __name__ == "__main__":
    check_and_migrate_schema()
    init_pwa_settings()
    init_content()
