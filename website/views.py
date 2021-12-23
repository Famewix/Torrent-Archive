from flask import Blueprint, render_template, url_for, flash, request, redirect
import datetime
import os
from .forms import PostForm, LoginForm
from .models import User, Post
from . import app, db, bcrypt
from flask_login import login_user, current_user, logout_user, login_required


views = Blueprint("views", __name__)

@views.route("/")
@views.route("/home")
def home():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(per_page=2, page=page)
    return render_template("index.html", posts=posts)

@views.route("/browse")
def browse():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.title).paginate(per_page=2, page=page)
    return render_template("browse.html", posts=posts)

@views.route("/search")
def search():
    q = request.args.get('q')
    if q:
        searched_posts = Post.query.filter(Post.title.contains(q))
        return render_template('search.html', posts=searched_posts)
    else:
        posts = []
        return render_template('search.html', posts=posts)

@views.route("/login", methods=["POST", "GET"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("views.home"))

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            flash('Successfully Logged in.', 'success')
            return redirect(url_for('views.home'))
        else:
            flash('Invalid username or password.', 'danger')
    return render_template("login.html", form=form)

@views.route("/post", methods=['GET','POST'])
@login_required
def post():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data, category=form.category.data ,magnet_url=form.magnet.data, author=current_user)
        db.session.add(post)
        db.session.commit()
        flash('Post successful.', 'success')
    else:
        if request.method != 'GET':
            flash('Fill the form correctly.', 'danger')
    return render_template("post.html", form=form)


@views.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('views.home'))

@views.route("/about")
def about():
    return render_template("about.html")