from datetime import datetime
from flask import Flask, render_template, redirect, url_for, flash, request
from flask_login import LoginManager, login_user, logout_user, current_user
from flask_migrate import Migrate

from utils.config import Config
from utils.forms import ContactForm, NewsForm
from utils.models import db, User
from routes.about import about_bp
from routes.contact import contact_bp
from routes.factories import factories_bp
from routes.news import news_bp
from routes.products import products_bp
from routes.services import services_bp

# Initialize app
app = Flask(__name__)
app.config.from_object(Config)

# Initialize extensions
db.init_app(app)
migrate = Migrate(app, db)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

# Register Blueprints
app.register_blueprint(about_bp)
app.register_blueprint(contact_bp)
app.register_blueprint(factories_bp)
app.register_blueprint(news_bp)
app.register_blueprint(products_bp)
app.register_blueprint(services_bp)

# Inject current year into templates
@app.context_processor
def inject_year():
    return {'current_year': datetime.utcnow().year}

# Home route
@app.route('/')
def home():
    return render_template('home.html')

# User loader
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(username=username).first()

        if user and user.password == password:
            login_user(user)
            flash('Logged in successfully.', 'success')
            return redirect(url_for('news.new_post'))  # Assumes `new_post` is in `news_bp`
        else:
            flash('Invalid credentials', 'danger')
    return render_template('login.html')

if __name__ == "__main__":
    app.run(debug=True)