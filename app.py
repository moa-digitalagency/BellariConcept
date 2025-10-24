import os
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify, send_from_directory
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
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
app.config['ADMIN_INIT_ALLOWED'] = os.getenv('ADMIN_INIT_ALLOWED', 'false').lower() == 'true'

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'webp'}

os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'admin_login'

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
    order_index = db.Column(db.Integer, default=0)
    heading = db.Column(db.String(300))
    subheading = db.Column(db.String(300))
    content = db.Column(db.Text)
    button_text = db.Column(db.String(100))
    button_link = db.Column(db.String(200))
    image_url = db.Column(db.String(300))
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

@app.route('/')
def index():
    page = Page.query.filter_by(slug='home', is_active=True).first()
    if page:
        sections = Section.query.filter_by(page_id=page.id, is_active=True).order_by(Section.order_index).all()
    else:
        sections = []
    return render_template('index.html', page=page, sections=sections)

@app.route('/about')
def about():
    page = Page.query.filter_by(slug='about', is_active=True).first()
    if page:
        sections = Section.query.filter_by(page_id=page.id, is_active=True).order_by(Section.order_index).all()
    else:
        sections = []
    return render_template('about.html', page=page, sections=sections)

@app.route('/services')
def services():
    page = Page.query.filter_by(slug='services', is_active=True).first()
    if page:
        sections = Section.query.filter_by(page_id=page.id, is_active=True).order_by(Section.order_index).all()
    else:
        sections = []
    return render_template('services.html', page=page, sections=sections)

@app.route('/portfolio')
def portfolio():
    page = Page.query.filter_by(slug='portfolio', is_active=True).first()
    if page:
        sections = Section.query.filter_by(page_id=page.id, is_active=True).order_by(Section.order_index).all()
    else:
        sections = []
    return render_template('portfolio.html', page=page, sections=sections)

@app.route('/contact')
def contact():
    page = Page.query.filter_by(slug='contact', is_active=True).first()
    if page:
        sections = Section.query.filter_by(page_id=page.id, is_active=True).order_by(Section.order_index).all()
    else:
        sections = []
    return render_template('contact.html', page=page, sections=sections)

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
    return render_template('admin/dashboard.html', pages=pages, images=images)

@app.route('/admin/pages')
@login_required
def admin_pages():
    pages = Page.query.all()
    return render_template('admin/pages.html', pages=pages)

@app.route('/admin/page/<int:page_id>')
@login_required
def admin_edit_page(page_id):
    page = Page.query.get_or_404(page_id)
    sections = Section.query.filter_by(page_id=page_id).order_by(Section.order_index).all()
    return render_template('admin/edit_page.html', page=page, sections=sections)

@app.route('/admin/page/<int:page_id>/update', methods=['POST'])
@login_required
def admin_update_page(page_id):
    page = Page.query.get_or_404(page_id)
    page.title = request.form.get('title')
    page.meta_description = request.form.get('meta_description')
    page.is_active = 'is_active' in request.form
    db.session.commit()
    flash('Page updated successfully', 'success')
    return redirect(url_for('admin_edit_page', page_id=page_id))

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
    section.is_active = 'is_active' in request.form
    db.session.commit()
    flash('Section updated successfully', 'success')
    return redirect(url_for('admin_edit_page', page_id=section.page_id))

@app.route('/admin/section/create', methods=['POST'])
@login_required
def admin_create_section():
    page_id = request.form.get('page_id')
    section = Section(
        page_id=page_id,
        section_type=request.form.get('section_type', 'text'),
        heading=request.form.get('heading'),
        content=request.form.get('content'),
        order_index=Section.query.filter_by(page_id=page_id).count()
    )
    db.session.add(section)
    db.session.commit()
    flash('Section created successfully', 'success')
    return redirect(url_for('admin_edit_page', page_id=page_id))

@app.route('/admin/section/<int:section_id>/delete', methods=['POST'])
@login_required
def admin_delete_section(section_id):
    section = Section.query.get_or_404(section_id)
    page_id = section.page_id
    db.session.delete(section)
    db.session.commit()
    flash('Section deleted successfully', 'success')
    return redirect(url_for('admin_edit_page', page_id=page_id))

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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
