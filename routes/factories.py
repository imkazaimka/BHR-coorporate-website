from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required
from utils.models import db, NewsPost
from utils.forms import NewsForm

# Create the blueprint
factories_bp = Blueprint('factories', __name__, url_prefix='/about/factories')

@factories_bp.route('/')
def factories():
    return render_template('factories.html')

@factories_bp.route('/bhr-navoiy')
def bhr():
    return render_template('bhr-navoiy.html')


@factories_bp.route('/bhr-bukhara')
def bhr_bukhara():
    return render_template('bhr-bukhara.html')


@factories_bp.route('/cotton-cleaning')
def cotton_cleaning():
    return render_template('cotton-cleaning.html')
