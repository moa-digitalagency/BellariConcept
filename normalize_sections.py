import os
from app import app, db, Page, Section

with app.app_context():
    print("Starting section normalization...")
    pages = Page.query.all()
    total_updated = 0
    
    for page in pages:
        print(f"\nProcessing page: {page.title}")
        sections_by_type_lang = {}
        
        for section in Section.query.filter_by(page_id=page.id).order_by(Section.order_index).all():
            key = (section.section_type, section.language_code)
            if key not in sections_by_type_lang:
                sections_by_type_lang[key] = []
            sections_by_type_lang[key].append(section)
        
        new_order = 0
        section_types_seen = set()
        
        for section_type in set(st for st, _ in sections_by_type_lang.keys()):
            if section_type in section_types_seen:
                continue
            section_types_seen.add(section_type)
            
            fr_sections = sections_by_type_lang.get((section_type, 'fr'), [])
            en_sections = sections_by_type_lang.get((section_type, 'en'), [])
            
            max_pairs = max(len(fr_sections), len(en_sections))
            for i in range(max_pairs):
                if i < len(fr_sections):
                    old_order = fr_sections[i].order_index
                    fr_sections[i].order_index = new_order
                    if old_order != new_order:
                        print(f"  FR {section_type} #{i}: {old_order} -> {new_order}")
                        total_updated += 1
                        
                if i < len(en_sections):
                    old_order = en_sections[i].order_index
                    en_sections[i].order_index = new_order
                    if old_order != new_order:
                        print(f"  EN {section_type} #{i}: {old_order} -> {new_order}")
                        total_updated += 1
                        
                new_order += 1
    
    db.session.commit()
    print(f"\n✓ Migration complete! Updated {total_updated} sections.")
    print("All FR/EN section pairs now share the same order_index.")
