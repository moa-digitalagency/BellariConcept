from app import app, db, Section, Page
from werkzeug.security import generate_password_hash

with app.app_context():
    # Get the services page
    services_page = Page.query.filter_by(slug='services').first()
    
    if services_page:
        # Delete old service sections but keep the hero
        Section.query.filter_by(page_id=services_page.id, section_type='service').delete()
        
        # Define the 6 services with images - French version
        services_fr = [
            {
                'heading': 'Construction',
                'content': 'Construction complète de projets résidentiels et commerciaux. De la conception à la réalisation, nous gérons chaque détail avec précision et soin.',
                'image_url': '/static/images/modern_construction__a427a1cf.jpg',
                'language_code': 'fr',
                'order_index': 1
            },
            {
                'heading': 'Électricité',
                'content': 'Installation électrique professionnelle pour tous types de bâtiments. Nos électriciens certifiés assurent des installations sûres et conformes aux normes.',
                'image_url': '/static/images/professional_electri_984ae0e8.jpg',
                'language_code': 'fr',
                'order_index': 2
            },
            {
                'heading': 'Plomberie',
                'content': 'Services de plomberie complets incluant installation, réparation et maintenance. Solutions efficaces pour vos systèmes d\'eau et sanitaires.',
                'image_url': '/static/images/plumber_fixing_pipes_d4c8be18.jpg',
                'language_code': 'fr',
                'order_index': 3
            },
            {
                'heading': 'Peinture',
                'content': 'Services de peinture professionnelle pour intérieurs et extérieurs. Finitions impeccables avec des matériaux de qualité supérieure.',
                'image_url': '/static/images/painter_painting_wal_be02294b.jpg',
                'language_code': 'fr',
                'order_index': 4
            },
            {
                'heading': 'Climatisation',
                'content': 'Installation et maintenance de systèmes de climatisation. Solutions adaptées au climat de Marrakech pour votre confort optimal.',
                'image_url': '/static/images/hvac_air_conditionin_8336dff9.jpg',
                'language_code': 'fr',
                'order_index': 5
            },
            {
                'heading': 'Entretien de Piscine',
                'content': 'Entretien complet et réparation de piscines. Maintenez votre piscine en parfait état toute l\'année avec nos services professionnels.',
                'image_url': '/static/images/swimming_pool_mainte_0698f0ec.jpg',
                'language_code': 'fr',
                'order_index': 6
            }
        ]
        
        # English version
        services_en = [
            {
                'heading': 'Construction',
                'content': 'Complete construction of residential and commercial projects. From design to completion, we handle every detail with precision and care.',
                'image_url': '/static/images/modern_construction__a427a1cf.jpg',
                'language_code': 'en',
                'order_index': 1
            },
            {
                'heading': 'Electrical',
                'content': 'Professional electrical installation for all types of buildings. Our certified electricians ensure safe installations that meet all standards.',
                'image_url': '/static/images/professional_electri_984ae0e8.jpg',
                'language_code': 'en',
                'order_index': 2
            },
            {
                'heading': 'Plumbing',
                'content': 'Complete plumbing services including installation, repair and maintenance. Efficient solutions for your water and sanitary systems.',
                'image_url': '/static/images/plumber_fixing_pipes_d4c8be18.jpg',
                'language_code': 'en',
                'order_index': 3
            },
            {
                'heading': 'Painting',
                'content': 'Professional painting services for interiors and exteriors. Impeccable finishes with superior quality materials.',
                'image_url': '/static/images/painter_painting_wal_be02294b.jpg',
                'language_code': 'en',
                'order_index': 4
            },
            {
                'heading': 'Air Conditioning',
                'content': 'Installation and maintenance of air conditioning systems. Solutions adapted to Marrakech\'s climate for your optimal comfort.',
                'image_url': '/static/images/hvac_air_conditionin_8336dff9.jpg',
                'language_code': 'en',
                'order_index': 5
            },
            {
                'heading': 'Pool Maintenance',
                'content': 'Complete pool maintenance and repair. Keep your pool in perfect condition all year round with our professional services.',
                'image_url': '/static/images/swimming_pool_mainte_0698f0ec.jpg',
                'language_code': 'en',
                'order_index': 6
            }
        ]
        
        # Add all services (both languages)
        for service_data in services_fr + services_en:
            section = Section(
                page_id=services_page.id,
                section_type='service',
                **service_data
            )
            db.session.add(section)
        
        db.session.commit()
        print("✓ Services mis à jour avec succès avec les images!")
        print(f"✓ Ajouté {len(services_fr)} services en français")
        print(f"✓ Ajouté {len(services_en)} services en anglais")
    else:
        print("✗ Page services non trouvée")
