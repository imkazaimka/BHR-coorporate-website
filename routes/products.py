from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required
from utils.models import db, NewsPost
from utils.forms import NewsForm

# Create the blueprint
products_bp = Blueprint('products', __name__, url_prefix='/products')


@products_bp.route('/')
def products():
    return render_template('products.html')

@products_bp.route('/catalog')
def catalog():
    return render_template('catalog.html')

@products_bp.route('/fabrics')
def fabrics():
    return render_template('fabrics.html')

@products_bp.route('/ready-made-garments')
def ready_made_garments():
    return render_template('ready-made-garments.html')

@products_bp.route('/yarn')
def yarn():
    return render_template('yarn.html')