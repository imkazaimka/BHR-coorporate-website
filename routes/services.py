from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required
from utils.models import db, NewsPost
from utils.forms import NewsForm

# Create the blueprint
services_bp = Blueprint('services', __name__, url_prefix='/services')

services_bp.route('/')
def services():
    return render_template('services.html')

services_bp.route('/spinning')
def spinning():
    return render_template('spinning.html')

services_bp.route('/garment-manufacturing')
def garment_manufacturing():
    return render_template('garment-manufacturing.html')

services_bp.route('/cotton-processing')
def cotton_processing():
    return render_template('cotton-processing.html')

