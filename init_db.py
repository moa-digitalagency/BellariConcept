from app import app, db, SiteSettings

def init_pwa_settings():
    """
    Initialize PWA settings in SiteSettings table if they don't exist.
    """
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
            'pwa_start_url': '/'
        }

        changes_made = False
        for key, value in defaults.items():
            setting = SiteSettings.query.filter_by(key=key).first()
            if not setting:
                print(f"Adding default setting: {key} = {value}")
                db.session.add(SiteSettings(key=key, value=value))
                changes_made = True
            else:
                print(f"Setting exists: {key} = {setting.value}")

        if changes_made:
            db.session.commit()
            print("PWA settings initialized.")
        else:
            print("No changes needed.")

if __name__ == "__main__":
    init_pwa_settings()
