from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required
from utils.models import db, NewsPost
from utils.forms import NewsForm

# Create the blueprint
contact_bp = Blueprint('contact', __name__, url_prefix='/contact')


@contact_bp.route('/')
def contact():
    return render_template('contact.html')

@contact_bp.route('/form')
def form():
    return render_template('form.html')
