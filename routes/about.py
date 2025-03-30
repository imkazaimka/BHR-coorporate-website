from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required
from utils.models import db, NewsPost
from utils.forms import NewsForm

# Create the blueprint
about_bp = Blueprint('about', __name__, url_prefix='/about')

@about_bp.route('/')
def about():
    return render_template('about.html')


@about_bp.route('/partners')
def partners():
    return render_template('partners.html')


@about_bp.route('/production')
def production():
    return render_template('production.html')


@about_bp.route('/farmlands')
def farmlands():
    return render_template('farmlands.html')


@about_bp.route('/team')
def team():
    return render_template('team.html')


@about_bp.route('/history')
def history():
    return render_template('history.html')


