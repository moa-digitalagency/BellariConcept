from app import app, db, User, Page, Section, SiteSettings
from werkzeug.security import generate_password_hash

def init_database():
    with app.app_context():
        print("Creating admin user...")
        if not User.query.first():
            admin = User(
                username='admin',
                password_hash=generate_password_hash('admin123')
            )
            db.session.add(admin)
            db.session.commit()
            print("Admin user created: username='admin', password='admin123'")
        
        print("Creating pages...")
        if not Page.query.first():
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
            print(f"Created {len(pages_data)} pages")
            
            print("Creating sections for pages...")
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
                print(f"Created {len(sections_data)} sections for home page")
            
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
                print(f"Created {len(sections_data)} sections for about page")
            
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
                print(f"Created {len(sections_data)} sections for services page")
        
        print("\nDatabase initialization complete!")
        print("You can now log in to the admin panel:")
        print("  Username: admin")
        print("  Password: admin123")
        print("  URL: /admin/login")

if __name__ == '__main__':
    init_database()
