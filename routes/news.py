from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required
from utils.models import db, NewsPost
from utils.forms import NewsForm

# Create the blueprint
news_bp = Blueprint('news', __name__, url_prefix='/news')

# Routes in this blueprint
@news_bp.route('/')
def news():
    posts = NewsPost.query.order_by(NewsPost.date_posted.desc()).all()
    return render_template('news.html', posts=posts)

@news_bp.route('/<int:post_id>')
def news_post(post_id):
    post = NewsPost.query.get_or_404(post_id)
    return render_template('news_post.html', post=post)

@news_bp.route('/admin/new', methods=['GET', 'POST'])
@login_required
def new_post():
    form = NewsForm()
    if form.validate_on_submit():
        post = NewsPost(title=form.title.data, content=form.content.data)
        db.session.add(post)
        db.session.commit()
        flash('News post added successfully!', 'success')
        return redirect(url_for('news.news'))
    return render_template('new_post.html', form=form)