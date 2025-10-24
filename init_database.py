import os
import sys

print("=" * 60)
print("BELLARI CONCEPT - Database Initialization")
print("=" * 60)
print()
print("This script will initialize the database with:")
print("  - Database tables")
print("  - Default admin user (username: admin, password: admin123)")
print("  - Sample pages and content")
print()
print("WARNING: This should ONLY be run during initial setup!")
print()

response = input("Continue? (yes/no): ")
if response.lower() != 'yes':
    print("Initialization cancelled.")
    sys.exit(0)

from app import app, db, User, Page, Section
from werkzeug.security import generate_password_hash

with app.app_context():
    print("\nCreating database tables...")
    db.create_all()
    
    if not User.query.first():
        print("Creating default admin user...")
        admin = User(
            username='admin',
            password_hash=generate_password_hash('admin123')
        )
        db.session.add(admin)
        print("  ✓ Admin user created")
        print("  ⚠️  USERNAME: admin")
        print("  ⚠️  PASSWORD: admin123")
        print("  ⚠️  IMPORTANT: Change this password immediately after first login!")
    else:
        print("  ✓ Admin user already exists")
    
    if not Page.query.first():
        print("\nCreating default pages and content...")
        pages_data = [
            {'slug': 'home', 'title': 'Bellari Concept - Luxury Interior Design', 'meta_description': 'Transform your space with Bellari Concept\'s luxury interior design services'},
            {'slug': 'about', 'title': 'About Us - Bellari Concept', 'meta_description': 'Learn about our design philosophy and expertise'},
            {'slug': 'services', 'title': 'Our Services - Bellari Concept', 'meta_description': 'Explore our comprehensive interior design services'},
            {'slug': 'portfolio', 'title': 'Portfolio - Bellari Concept', 'meta_description': 'View our stunning interior design projects'},
            {'slug': 'contact', 'title': 'Contact Us - Bellari Concept', 'meta_description': 'Get in touch with our design team'}
        ]
        
        for page_data in pages_data:
            page = Page(**page_data)
            db.session.add(page)
            db.session.flush()
            print(f"  ✓ Created page: {page.slug}")
            
            if page.slug == 'home':
                sections_data = [
                    {
                        'section_type': 'hero',
                        'heading': 'BELLARI CONCEPT',
                        'subheading': 'Luxury Interior Design & Architecture',
                        'content': 'Transform your space into a masterpiece of elegance and functionality',
                        'button_text': 'Explore Our Work',
                        'button_link': '/portfolio',
                        'order_index': 0
                    },
                    {
                        'section_type': 'intro',
                        'heading': 'Creating Timeless Spaces',
                        'content': 'At Bellari Concept, we blend sophisticated design with practical functionality to create interiors that inspire and endure. Our team of expert designers brings your vision to life with meticulous attention to detail and an unwavering commitment to excellence.',
                        'order_index': 1
                    },
                    {
                        'section_type': 'features',
                        'heading': 'Our Expertise',
                        'content': 'Residential Design • Commercial Spaces • Luxury Renovations • Custom Furniture • Art Curation • Project Management',
                        'order_index': 2
                    }
                ]
                
                for section_data in sections_data:
                    section = Section(page_id=page.id, **section_data)
                    db.session.add(section)
            
            elif page.slug == 'about':
                sections_data = [
                    {
                        'section_type': 'hero',
                        'heading': 'About Bellari Concept',
                        'subheading': 'Design Excellence Since 2010',
                        'order_index': 0
                    },
                    {
                        'section_type': 'text',
                        'heading': 'Our Story',
                        'content': 'Founded with a passion for creating exceptional spaces, Bellari Concept has established itself as a leader in luxury interior design. Our philosophy combines timeless elegance with contemporary innovation, resulting in spaces that are both beautiful and functional.',
                        'order_index': 1
                    },
                    {
                        'section_type': 'text',
                        'heading': 'Our Approach',
                        'content': 'We believe that great design starts with understanding our clients. Every project begins with a deep dive into your lifestyle, preferences, and aspirations. This personalized approach ensures that each space we create is uniquely yours.',
                        'order_index': 2
                    }
                ]
                
                for section_data in sections_data:
                    section = Section(page_id=page.id, **section_data)
                    db.session.add(section)
            
            elif page.slug == 'services':
                sections_data = [
                    {
                        'section_type': 'hero',
                        'heading': 'Our Services',
                        'subheading': 'Comprehensive Design Solutions',
                        'order_index': 0
                    },
                    {
                        'section_type': 'service',
                        'heading': 'Interior Design',
                        'content': 'Complete interior design services for residential and commercial spaces. From concept to completion, we handle every detail with precision and care.',
                        'order_index': 1
                    },
                    {
                        'section_type': 'service',
                        'heading': 'Space Planning',
                        'content': 'Expert space planning that maximizes functionality while maintaining aesthetic appeal. We create layouts that flow naturally and enhance your daily experience.',
                        'order_index': 2
                    },
                    {
                        'section_type': 'service',
                        'heading': 'Custom Furniture',
                        'content': 'Bespoke furniture design and curation. Each piece is selected or designed to complement your space perfectly and stand the test of time.',
                        'order_index': 3
                    }
                ]
                
                for section_data in sections_data:
                    section = Section(page_id=page.id, **section_data)
                    db.session.add(section)
            
            elif page.slug == 'contact':
                sections_data = [
                    {
                        'section_type': 'hero',
                        'heading': 'Get In Touch',
                        'subheading': 'Let\'s Create Something Beautiful Together',
                        'order_index': 0
                    },
                    {
                        'section_type': 'contact',
                        'heading': 'Contact Information',
                        'content': 'Email: info@bellariconcept.com\nPhone: +1 (555) 123-4567\nAddress: 123 Design Avenue, Suite 100\nNew York, NY 10001',
                        'order_index': 1
                    }
                ]
                
                for section_data in sections_data:
                    section = Section(page_id=page.id, **section_data)
                    db.session.add(section)
    else:
        print("  ✓ Pages already exist")
    
    db.session.commit()
    print("\n" + "=" * 60)
    print("✓ Database initialization complete!")
    print("=" * 60)
    print("\nNext steps:")
    print("  1. Start the server: python app.py")
    print("  2. Visit: http://localhost:5000/admin/login")
    print("  3. Login with username: admin, password: admin123")
    print("  4. IMMEDIATELY change your password!")
    print()
