import os
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify, send_from_directory, session
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
from datetime import datetime
from PIL import Image as PILImage
import secrets

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get("SESSION_SECRET")
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {
    "pool_recycle": 300,
    "pool_pre_ping": True,
}
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
app.config['ADMIN_INIT_ALLOWED'] = os.getenv('ADMIN_INIT_ALLOWED', 'false').lower() == 'true'
app.config['LANGUAGES'] = ['fr', 'en']
app.config['DEFAULT_LANGUAGE'] = 'fr'

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'webp'}

os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'admin_login'

def get_language():
    return session.get('language', app.config['DEFAULT_LANGUAGE'])

@app.context_processor
def inject_site_settings():
    settings_dict = {}
    for setting in SiteSettings.query.all():
        settings_dict[setting.key] = setting.value
    
    logo_url = settings_dict.get('site_logo', '/static/logo.png')
    return {
        'site_settings': settings_dict,
        'site_logo': logo_url,
        'site_name': settings_dict.get(f'site_name_{get_language()}', 'Bellari Concept'),
        'meta_keywords': settings_dict.get('default_meta_keywords', ''),
        'og_image': settings_dict.get('default_og_image', ''),
        'google_analytics_id': settings_dict.get('google_analytics_id', '')
    }

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class Page(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    slug = db.Column(db.String(100), unique=True, nullable=False)
    title = db.Column(db.String(200), nullable=False)
    meta_description = db.Column(db.String(300))
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    sections = db.relationship('Section', backref='page', lazy=True, cascade='all, delete-orphan')

class Section(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    page_id = db.Column(db.Integer, db.ForeignKey('page.id'), nullable=False)
    section_type = db.Column(db.String(50), nullable=False)
    language_code = db.Column(db.String(5), default='fr', nullable=False)
    order_index = db.Column(db.Integer, default=0)
    heading = db.Column(db.String(300))
    subheading = db.Column(db.String(300))
    content = db.Column(db.Text)
    button_text = db.Column(db.String(100))
    button_link = db.Column(db.String(200))
    image_url = db.Column(db.String(300))
    background_image = db.Column(db.String(300))
    background_color = db.Column(db.String(20))
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class Image(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(300), nullable=False)
    original_filename = db.Column(db.String(300), nullable=False)
    alt_text = db.Column(db.String(200))
    file_size = db.Column(db.Integer)
    width = db.Column(db.Integer)
    height = db.Column(db.Integer)
    uploaded_at = db.Column(db.DateTime, default=datetime.utcnow)

class SiteSettings(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    key = db.Column(db.String(100), unique=True, nullable=False)
    value = db.Column(db.Text)
    description = db.Column(db.String(300))
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/set_language/<lang>')
def set_language(lang):
    if lang in app.config['LANGUAGES']:
        session['language'] = lang
    return redirect(request.referrer or url_for('index'))

@app.route('/')
def index():
    lang = get_language()
    page = Page.query.filter_by(slug='home', is_active=True).first()
    if page:
        sections = Section.query.filter_by(page_id=page.id, language_code=lang, is_active=True).order_by(Section.order_index).all()
    else:
        sections = []
    return render_template('index.html', page=page, sections=sections, lang=lang)

@app.route('/about')
def about():
    lang = get_language()
    page = Page.query.filter_by(slug='about', is_active=True).first()
    if page:
        sections = Section.query.filter_by(page_id=page.id, language_code=lang, is_active=True).order_by(Section.order_index).all()
    else:
        sections = []
    return render_template('about.html', page=page, sections=sections, lang=lang)

@app.route('/services')
def services():
    lang = get_language()
    page = Page.query.filter_by(slug='services', is_active=True).first()
    if page:
        sections = Section.query.filter_by(page_id=page.id, language_code=lang, is_active=True).order_by(Section.order_index).all()
    else:
        sections = []
    return render_template('services.html', page=page, sections=sections, lang=lang)

@app.route('/portfolio')
def portfolio():
    lang = get_language()
    page = Page.query.filter_by(slug='portfolio', is_active=True).first()
    if page:
        sections = Section.query.filter_by(page_id=page.id, language_code=lang, is_active=True).order_by(Section.order_index).all()
    else:
        sections = []
    return render_template('portfolio.html', page=page, sections=sections, lang=lang)

@app.route('/contact')
def contact():
    lang = get_language()
    page = Page.query.filter_by(slug='contact', is_active=True).first()
    if page:
        sections = Section.query.filter_by(page_id=page.id, language_code=lang, is_active=True).order_by(Section.order_index).all()
    else:
        sections = []
    return render_template('contact.html', page=page, sections=sections, lang=lang)

@app.route('/admin/login', methods=['GET', 'POST'])
def admin_login():
    if current_user.is_authenticated:
        return redirect(url_for('admin_dashboard'))
    
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(username=username).first()
        
        if user and check_password_hash(user.password_hash, password):
            login_user(user)
            return redirect(url_for('admin_dashboard'))
        else:
            flash('Invalid username or password', 'error')
    
    return render_template('admin/login.html')

@app.route('/admin/logout')
@login_required
def admin_logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/admin')
@login_required
def admin_dashboard():
    pages = Page.query.all()
    images = Image.query.order_by(Image.uploaded_at.desc()).limit(10).all()
    lang = request.args.get('lang', 'fr')
    return render_template('admin/dashboard.html', pages=pages, images=images, lang=lang)

@app.route('/admin/pages')
@login_required
def admin_pages():
    pages = Page.query.all()
    lang = request.args.get('lang', 'fr')
    return render_template('admin/pages.html', pages=pages, lang=lang)

@app.route('/admin/page/<int:page_id>')
@login_required
def admin_edit_page(page_id):
    page = Page.query.get_or_404(page_id)
    all_sections = Section.query.filter_by(page_id=page_id).order_by(Section.order_index).all()
    images = Image.query.order_by(Image.uploaded_at.desc()).all()
    lang = request.args.get('lang', 'fr')
    
    paired = set()
    section_groups = []
    
    for i, section in enumerate(all_sections):
        if section.id in paired:
            continue
            
        pair = {'fr': None, 'en': None}
        pair[section.language_code] = section
        paired.add(section.id)
        
        other_lang = 'en' if section.language_code == 'fr' else 'fr'
        best_match = None
        best_score = float('inf')
        
        for j, other_section in enumerate(all_sections[i+1:], start=i+1):
            if (other_section.id in paired or 
                other_section.language_code != other_lang or
                other_section.section_type != section.section_type):
                continue
            
            distance = abs(other_section.order_index - section.order_index)
            
            if distance < best_score:
                best_score = distance
                best_match = other_section
                
            if distance == 0:
                break
        
        if best_match:
            pair[other_lang] = best_match
            paired.add(best_match.id)
        
        order_idx = section.order_index
        section_groups.append(((order_idx, section.section_type), pair))
    
    return render_template('admin/edit_page.html', page=page, section_groups=section_groups, images=images, lang=lang)

@app.route('/admin/page/<int:page_id>/update', methods=['POST'])
@login_required
def admin_update_page(page_id):
    page = Page.query.get_or_404(page_id)
    page.title = request.form.get('title')
    page.meta_description = request.form.get('meta_description')
    page.is_active = 'is_active' in request.form
    db.session.commit()
    lang = request.form.get('lang', request.args.get('lang', 'fr'))
    flash('Page updated successfully', 'success')
    return redirect(url_for('admin_edit_page', page_id=page_id, lang=lang))

@app.route('/admin/section/<int:section_id>/update', methods=['POST'])
@login_required
def admin_update_section(section_id):
    section = Section.query.get_or_404(section_id)
    section.heading = request.form.get('heading')
    section.subheading = request.form.get('subheading')
    section.content = request.form.get('content')
    section.button_text = request.form.get('button_text')
    section.button_link = request.form.get('button_link')
    section.image_url = request.form.get('image_url')
    section.background_image = request.form.get('background_image')
    section.is_active = 'is_active' in request.form
    db.session.commit()
    lang = request.form.get('lang', request.args.get('lang', 'fr'))
    flash('Section updated successfully', 'success')
    return redirect(url_for('admin_edit_page', page_id=section.page_id, lang=lang))

@app.route('/admin/section/create', methods=['POST'])
@login_required
def admin_create_section():
    page_id = request.form.get('page_id')
    order_index = request.form.get('order_index')
    if order_index is None:
        order_index = Section.query.filter_by(page_id=page_id).count()
    section = Section(
        page_id=page_id,
        section_type=request.form.get('section_type', 'text'),
        language_code=request.form.get('language_code', 'fr'),
        heading=request.form.get('heading'),
        subheading=request.form.get('subheading'),
        content=request.form.get('content'),
        order_index=int(order_index)
    )
    db.session.add(section)
    db.session.commit()
    lang = request.form.get('lang', request.args.get('lang', 'fr'))
    flash('Section created successfully', 'success')
    return redirect(url_for('admin_edit_page', page_id=page_id, lang=lang))

@app.route('/admin/section/create_both', methods=['POST'])
@login_required
def admin_create_section_both():
    page_id = request.form.get('page_id')
    section_type = request.form.get('section_type', 'text')
    order_index = Section.query.filter_by(page_id=page_id).count()
    
    section_fr = Section(
        page_id=page_id,
        section_type=section_type,
        language_code='fr',
        heading=request.form.get('heading_fr'),
        subheading=request.form.get('subheading_fr'),
        content=request.form.get('content_fr'),
        order_index=order_index
    )
    db.session.add(section_fr)
    
    section_en = Section(
        page_id=page_id,
        section_type=section_type,
        language_code='en',
        heading=request.form.get('heading_en'),
        subheading=request.form.get('subheading_en'),
        content=request.form.get('content_en'),
        order_index=order_index
    )
    db.session.add(section_en)
    
    db.session.commit()
    lang = request.form.get('lang', request.args.get('lang', 'fr'))
    flash('Sections created successfully for both languages', 'success')
    return redirect(url_for('admin_edit_page', page_id=page_id, lang=lang))

@app.route('/admin/section/<int:section_id>/delete', methods=['POST'])
@login_required
def admin_delete_section(section_id):
    section = Section.query.get_or_404(section_id)
    page_id = section.page_id
    db.session.delete(section)
    db.session.commit()
    lang = request.form.get('lang', request.args.get('lang', 'fr'))
    flash('Section deleted successfully', 'success')
    return redirect(url_for('admin_edit_page', page_id=page_id, lang=lang))

@app.route('/admin/images')
@login_required
def admin_images():
    images = Image.query.order_by(Image.uploaded_at.desc()).all()
    return render_template('admin/images.html', images=images)

@app.route('/admin/upload', methods=['POST'])
@login_required
def admin_upload():
    if 'file' not in request.files:
        return jsonify({'error': 'No file provided'}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400
    
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        unique_filename = f"{secrets.token_hex(8)}_{filename}"
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], unique_filename)
        file.save(filepath)
        
        with PILImage.open(filepath) as img:
            width, height = img.size
        
        file_size = os.path.getsize(filepath)
        
        image = Image(
            filename=unique_filename,
            original_filename=filename,
            alt_text=request.form.get('alt_text', ''),
            file_size=file_size,
            width=width,
            height=height
        )
        db.session.add(image)
        db.session.commit()
        
        return jsonify({
            'success': True,
            'image': {
                'id': image.id,
                'url': f'/static/uploads/{unique_filename}',
                'filename': unique_filename
            }
        })
    
    return jsonify({'error': 'Invalid file type'}), 400

@app.route('/admin/image/<int:image_id>/delete', methods=['POST'])
@login_required
def admin_delete_image(image_id):
    image = Image.query.get_or_404(image_id)
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], image.filename)
    if os.path.exists(filepath):
        os.remove(filepath)
    db.session.delete(image)
    db.session.commit()
    flash('Image deleted successfully', 'success')
    return redirect(url_for('admin_images'))

@app.route('/admin/normalize-sections')
@login_required
def normalize_sections():
    pages = Page.query.all()
    for page in pages:
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
                    fr_sections[i].order_index = new_order
                if i < len(en_sections):
                    en_sections[i].order_index = new_order
                new_order += 1
    
    db.session.commit()
    flash('Sections normalized successfully! All FR/EN pairs now share the same order_index.', 'success')
    return redirect(url_for('admin_dashboard'))

@app.route('/admin/init-db')
@login_required
def init_db():
    if not app.config['ADMIN_INIT_ALLOWED']:
        flash('Database initialization is disabled for security reasons', 'error')
        return redirect(url_for('admin_dashboard'))
    
    with app.app_context():
        db.create_all()
        
        if not User.query.first():
            flash('WARNING: Using default admin credentials. CHANGE PASSWORD IMMEDIATELY!', 'error')
            admin = User(
                username='admin',
                password_hash=generate_password_hash('admin123')
            )
            db.session.add(admin)
        
        if not Page.query.first():
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
                db.session.commit()
                
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
        
        db.session.commit()
        flash('Database initialized successfully!', 'success')
        return redirect(url_for('admin_dashboard'))

@app.route('/admin/settings', methods=['GET', 'POST'])
@login_required
def admin_settings():
    if request.method == 'POST':
        settings_to_update = [
            ('site_logo', request.form.get('site_logo')),
            ('site_name_fr', request.form.get('site_name_fr')),
            ('site_name_en', request.form.get('site_name_en')),
            ('default_meta_keywords', request.form.get('default_meta_keywords')),
            ('default_og_image', request.form.get('default_og_image')),
            ('google_analytics_id', request.form.get('google_analytics_id')),
            ('facebook_url', request.form.get('facebook_url')),
            ('instagram_url', request.form.get('instagram_url')),
            ('linkedin_url', request.form.get('linkedin_url'))
        ]
        
        for key, value in settings_to_update:
            if value is not None:
                setting = SiteSettings.query.filter_by(key=key).first()
                if setting:
                    setting.value = value
                else:
                    setting = SiteSettings(key=key, value=value)
                    db.session.add(setting)
        
        db.session.commit()
        flash('Settings updated successfully', 'success')
        return redirect(url_for('admin_settings'))
    
    settings_dict = {}
    for setting in SiteSettings.query.all():
        settings_dict[setting.key] = setting.value
    
    images = Image.query.order_by(Image.uploaded_at.desc()).all()
    return render_template('admin/settings.html', settings=settings_dict, images=images)

@app.route('/admin/upload-logo', methods=['POST'])
@login_required
def admin_upload_logo():
    if 'file' not in request.files:
        return jsonify({'error': 'No file provided'}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400
    
    if file and allowed_file(file.filename):
        filename = 'logo.' + file.filename.rsplit('.', 1)[1].lower()
        filepath = os.path.join('static', filename)
        file.save(filepath)
        
        setting = SiteSettings.query.filter_by(key='site_logo').first()
        if setting:
            setting.value = f'/static/{filename}'
        else:
            setting = SiteSettings(key='site_logo', value=f'/static/{filename}')
            db.session.add(setting)
        
        db.session.commit()
        
        return jsonify({
            'success': True,
            'logo_url': f'/static/{filename}'
        })
    
    return jsonify({'error': 'Invalid file type'}), 400

def get_setting(key, default=''):
    setting = SiteSettings.query.filter_by(key=key).first()
    return setting.value if setting else default

@app.route('/sitemap.xml')
def sitemap():
    from flask import Response
    from urllib.parse import urljoin
    
    base_url = request.url_root.rstrip('/')
    
    pages_xml = []
    pages_xml.append('<?xml version="1.0" encoding="UTF-8"?>')
    pages_xml.append('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">')
    
    pages = Page.query.filter_by(is_active=True).all()
    
    for page in pages:
        if page.slug == 'home':
            loc = base_url + '/'
        else:
            loc = base_url + '/' + page.slug
        
        lastmod = page.updated_at.strftime('%Y-%m-%d') if page.updated_at else datetime.utcnow().strftime('%Y-%m-%d')
        
        priority = '1.0' if page.slug == 'home' else '0.8'
        
        pages_xml.append('  <url>')
        pages_xml.append(f'    <loc>{loc}</loc>')
        pages_xml.append(f'    <lastmod>{lastmod}</lastmod>')
        pages_xml.append('    <changefreq>weekly</changefreq>')
        pages_xml.append(f'    <priority>{priority}</priority>')
        pages_xml.append('  </url>')
    
    pages_xml.append('</urlset>')
    
    sitemap_xml = '\n'.join(pages_xml)
    
    response = Response(sitemap_xml, mimetype='application/xml')
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    return response

@app.route('/robots.txt')
def robots():
    from flask import Response
    
    base_url = request.url_root.rstrip('/')
    
    robots_txt = f"""User-agent: *
Allow: /

# Disallow admin and private areas
Disallow: /admin/
Disallow: /admin/*

# Sitemap
Sitemap: {base_url}/sitemap.xml
"""
    
    response = Response(robots_txt, mimetype='text/plain')
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    return response

app.jinja_env.globals.update(get_setting=get_setting)

with app.app_context():
    from auto_init import ensure_database_initialized
    ensure_database_initialized()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
