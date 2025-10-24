import os
import sys

print("=" * 60)
print("BELLARI CONCEPT - Database Update with Multilingual Content")
print("=" * 60)
print()

from app import app, db, Page, Section

with app.app_context():
    print("Updating database schema...")
    db.create_all()
    
    print("Clearing existing sections...")
    Section.query.delete()
    db.session.commit()
    
    print("\nCreating multilingual content...")
    
    pages = Page.query.all()
    for page in pages:
        if page.slug == 'home':
            sections_data = [
                {
                    'language_code': 'fr',
                    'section_type': 'hero',
                    'heading': 'BELLARI CONCEPT',
                    'subheading': 'Construction et Rénovation à Marrakech',
                    'content': 'Votre partenaire de choix à Marrakech pour tous vos projets de construction et de rénovation',
                    'button_text': 'En savoir plus',
                    'button_link': '/contact',
                    'image_url': '/static/images/modern_construction__a427a1cf.jpg',
                    'order_index': 0
                },
                {
                    'language_code': 'en',
                    'section_type': 'hero',
                    'heading': 'BELLARI CONCEPT',
                    'subheading': 'Construction and Renovation in Marrakech',
                    'content': 'Your partner of choice in Marrakech for all your construction and renovation projects',
                    'button_text': 'Learn More',
                    'button_link': '/contact',
                    'image_url': '/static/images/modern_construction__a427a1cf.jpg',
                    'order_index': 0
                },
                {
                    'language_code': 'fr',
                    'section_type': 'intro',
                    'heading': 'Nous vous aidons à réaliser les projets de vos rêves',
                    'content': 'Expertise sans compromis : Avec Bellari Concept, chaque projet est un gage de qualité. Notre équipe spécialisée offre une maîtrise technique inégalée, allant de la plomberie à la peinture. Nous mettons l\'excellence au cœur de tout ce que nous faisons, transformant vos visions en réalités durables et esthétiquement plaisantes.',
                    'image_url': '/static/images/modern_construction__e4781d44.jpg',
                    'order_index': 1
                },
                {
                    'language_code': 'en',
                    'section_type': 'intro',
                    'heading': 'We help you realize your dream projects',
                    'content': 'Uncompromising expertise: With Bellari Concept, each project is a guarantee of quality. Our specialized team offers unparalleled technical mastery, from plumbing to painting. We put excellence at the heart of everything we do, transforming your visions into lasting and aesthetically pleasing realities.',
                    'image_url': '/static/images/modern_construction__e4781d44.jpg',
                    'order_index': 1
                },
            ]
            
            for section_data in sections_data:
                section = Section(page_id=page.id, **section_data)
                db.session.add(section)
            print(f"  ✓ Created home page sections (FR & EN)")
        
        elif page.slug == 'about':
            sections_data = [
                {
                    'language_code': 'fr',
                    'section_type': 'hero',
                    'heading': 'À Propos de Bellari Concept',
                    'subheading': 'Expertise en Construction et Rénovation',
                    'order_index': 0
                },
                {
                    'language_code': 'en',
                    'section_type': 'hero',
                    'heading': 'About Bellari Concept',
                    'subheading': 'Expertise in Construction and Renovation',
                    'order_index': 0
                },
                {
                    'language_code': 'fr',
                    'section_type': 'text',
                    'heading': 'Notre Expertise',
                    'content': 'Expertise éprouvée • Approche centrée sur le client • Garantie de satisfaction\n\nAvec Bellari Concept, chaque projet est un gage de qualité. Notre équipe spécialisée offre une maîtrise technique inégalée.',
                    'order_index': 1
                },
                {
                    'language_code': 'en',
                    'section_type': 'text',
                    'heading': 'Our Expertise',
                    'content': 'Proven expertise • Client-centered approach • Satisfaction guarantee\n\nWith Bellari Concept, each project is a guarantee of quality. Our specialized team offers unparalleled technical mastery.',
                    'order_index': 1
                },
            ]
            
            for section_data in sections_data:
                section = Section(page_id=page.id, **section_data)
                db.session.add(section)
            print(f"  ✓ Created about page sections (FR & EN)")
        
        elif page.slug == 'services':
            sections_data = [
                {
                    'language_code': 'fr',
                    'section_type': 'hero',
                    'heading': 'Nos Services',
                    'subheading': 'Services de maintenance efficaces et fiables',
                    'order_index': 0
                },
                {
                    'language_code': 'en',
                    'section_type': 'hero',
                    'heading': 'Our Services',
                    'subheading': 'Efficient and reliable maintenance services',
                    'order_index': 0
                },
                {
                    'language_code': 'fr',
                    'section_type': 'service',
                    'heading': 'Construction et Rénovation',
                    'content': 'De la conception à la réalisation, nous offrons des services complets de construction et de rénovation pour des bâtiments résidentiels et commerciaux.',
                    'image_url': '/static/images/modern_construction__a427a1cf.jpg',
                    'order_index': 1
                },
                {
                    'language_code': 'en',
                    'section_type': 'service',
                    'heading': 'Construction and Renovation',
                    'content': 'From design to completion, we offer comprehensive construction and renovation services for residential and commercial buildings.',
                    'image_url': '/static/images/modern_construction__a427a1cf.jpg',
                    'order_index': 1
                },
                {
                    'language_code': 'fr',
                    'section_type': 'service',
                    'heading': 'Électricité',
                    'content': 'Nous nous chargeons de toute installation électrique, de la mise en place de circuits à l\'installation de systèmes d\'éclairage complexes.',
                    'image_url': '/static/images/professional_electri_984ae0e8.jpg',
                    'order_index': 2
                },
                {
                    'language_code': 'en',
                    'section_type': 'service',
                    'heading': 'Electrical',
                    'content': 'We handle all electrical installations, from circuit setup to complex lighting systems installation.',
                    'image_url': '/static/images/professional_electri_984ae0e8.jpg',
                    'order_index': 2
                },
                {
                    'language_code': 'fr',
                    'section_type': 'service',
                    'heading': 'Plomberie',
                    'content': 'Des installations sanitaires aux réparations d\'urgence, notre équipe d\'experts en plomberie garantit un service impeccable.',
                    'image_url': '/static/images/plumber_fixing_pipes_d4c8be18.jpg',
                    'order_index': 3
                },
                {
                    'language_code': 'en',
                    'section_type': 'service',
                    'heading': 'Plumbing',
                    'content': 'From sanitary installations to emergency repairs, our team of plumbing experts guarantees impeccable service.',
                    'image_url': '/static/images/plumber_fixing_pipes_d4c8be18.jpg',
                    'order_index': 3
                },
                {
                    'language_code': 'fr',
                    'section_type': 'service',
                    'heading': 'Peinture et Décoration',
                    'content': 'Nous transformons les espaces avec des solutions de peinture et de décoration personnalisées qui reflètent votre style et améliorent votre confort.',
                    'image_url': '/static/images/painter_painting_wal_be02294b.jpg',
                    'order_index': 4
                },
                {
                    'language_code': 'en',
                    'section_type': 'service',
                    'heading': 'Painting and Decoration',
                    'content': 'We transform spaces with customized painting and decoration solutions that reflect your style and enhance your comfort.',
                    'image_url': '/static/images/painter_painting_wal_be02294b.jpg',
                    'order_index': 4
                },
                {
                    'language_code': 'fr',
                    'section_type': 'service',
                    'heading': 'Climatisation',
                    'content': 'Gardez votre espace confortable en toutes saisons avec nos solutions de climatisation haut de gamme, parfaitement adaptées à vos besoins.',
                    'image_url': '/static/images/hvac_air_conditionin_8336dff9.jpg',
                    'order_index': 5
                },
                {
                    'language_code': 'en',
                    'section_type': 'service',
                    'heading': 'Air Conditioning',
                    'content': 'Keep your space comfortable in all seasons with our high-end air conditioning solutions, perfectly adapted to your needs.',
                    'image_url': '/static/images/hvac_air_conditionin_8336dff9.jpg',
                    'order_index': 5
                },
                {
                    'language_code': 'fr',
                    'section_type': 'service',
                    'heading': 'Entretien de Piscine',
                    'content': 'Profitez d\'une piscine impeccable toute l\'année avec notre service d\'entretien professionnel qui inclut le nettoyage, l\'équilibrage chimique et la maintenance du système de filtration.',
                    'image_url': '/static/images/swimming_pool_mainte_0698f0ec.jpg',
                    'order_index': 6
                },
                {
                    'language_code': 'en',
                    'section_type': 'service',
                    'heading': 'Pool Maintenance',
                    'content': 'Enjoy an impeccable pool all year round with our professional maintenance service that includes cleaning, chemical balancing, and filtration system maintenance.',
                    'image_url': '/static/images/swimming_pool_mainte_0698f0ec.jpg',
                    'order_index': 6
                },
            ]
            
            for section_data in sections_data:
                section = Section(page_id=page.id, **section_data)
                db.session.add(section)
            print(f"  ✓ Created services page sections (FR & EN)")
        
        elif page.slug == 'contact':
            sections_data = [
                {
                    'language_code': 'fr',
                    'section_type': 'hero',
                    'heading': 'Contactez-Nous',
                    'subheading': 'Besoin de Professionnels du Bâtiment ?',
                    'order_index': 0
                },
                {
                    'language_code': 'en',
                    'section_type': 'hero',
                    'heading': 'Contact Us',
                    'subheading': 'Need Building Professionals?',
                    'order_index': 0
                },
                {
                    'language_code': 'fr',
                    'section_type': 'contact',
                    'heading': 'Informations de Contact',
                    'content': 'Email: bellari.groupe@gmail.com\nTéléphone: +212 6 35 50 24 61\nHeures d\'ouverture: 8:00 – 18:00\nLocalisation: Marrakech, Maroc',
                    'order_index': 1
                },
                {
                    'language_code': 'en',
                    'section_type': 'contact',
                    'heading': 'Contact Information',
                    'content': 'Email: bellari.groupe@gmail.com\nPhone: +212 6 35 50 24 61\nOpening Hours: 8:00 – 18:00\nLocation: Marrakech, Morocco',
                    'order_index': 1
                },
            ]
            
            for section_data in sections_data:
                section = Section(page_id=page.id, **section_data)
                db.session.add(section)
            print(f"  ✓ Created contact page sections (FR & EN)")
    
    db.session.commit()
    print("\n" + "=" * 60)
    print("✓ Database updated successfully!")
    print("=" * 60)
    print("\nThe website now supports:")
    print("  • French (default)")
    print("  • English")
    print("  • Real content from Bellari Concept")
    print("  • Service-specific images")
    print()
