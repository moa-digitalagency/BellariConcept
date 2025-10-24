from app import app, db, Page, Section

def add_expertise_section():
    with app.app_context():
        home_page = Page.query.filter_by(slug='home').first()
        if not home_page:
            print("Error: Home page not found!")
            return
        
        existing_expertise = Section.query.filter_by(
            page_id=home_page.id,
            section_type='expertise'
        ).first()
        
        if existing_expertise:
            print("Expertise section already exists!")
            return
        
        sections_data = [
            {
                'page_id': home_page.id,
                'section_type': 'expertise',
                'language_code': 'fr',
                'heading': 'Nous vous aidons à réaliser les projets de vos rêves',
                'subheading': 'Excellence et expertise au service de vos ambitions',
                'content': 'Avec Bellari Concept, chaque projet est un gage de qualité. Notre équipe spécialisée offre une maîtrise technique inégalée, allant de la construction à l\'entretien de piscines. Nous mettons l\'excellence au cœur de tout ce que nous faisons, transformant vos visions en réalités durables et esthétiquement plaisantes.',
                'image_url': '/static/images/modern_construction__e4781d44.jpg',
                'order_index': 1,
                'is_active': True
            },
            {
                'page_id': home_page.id,
                'section_type': 'expertise',
                'language_code': 'en',
                'heading': 'We help you realize your dream projects',
                'subheading': 'Excellence and expertise at the service of your ambitions',
                'content': 'With Bellari Concept, each project is a guarantee of quality. Our specialized team offers unparalleled technical mastery, from construction to pool maintenance. We put excellence at the heart of everything we do, transforming your visions into lasting and aesthetically pleasing realities.',
                'image_url': '/static/images/modern_construction__e4781d44.jpg',
                'order_index': 1,
                'is_active': True
            }
        ]
        
        print("Updating order_index for existing sections...")
        existing_sections = Section.query.filter_by(page_id=home_page.id).filter(
            Section.order_index >= 1
        ).all()
        
        for section in existing_sections:
            section.order_index += 1
        
        print("Adding new expertise sections...")
        for section_data in sections_data:
            section = Section(**section_data)
            db.session.add(section)
        
        db.session.commit()
        print(f"✓ Successfully added {len(sections_data)} expertise sections!")
        print("  - The section is now visible between hero and services")
        print("  - Editable from admin panel at /admin")

if __name__ == '__main__':
    add_expertise_section()
