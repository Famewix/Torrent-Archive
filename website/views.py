from flask import Blueprint, render_template, url_for, flash, request, redirect
import datetime
import os
from .forms import PostForm, LoginForm
from .models import User, Post
from . import app, db, bcrypt
from flask_login import login_user, current_user, logout_user, login_required


posts = [
    {
        'title': 'Torrent 1',
        'magnet': 'kaljnskndhnakishdihaiushihdaishdihaishdihaishdahsdihahsihaihsdhasidhiahidhiashdia',
        'category': 'movie',
        'posted': '26 March, 2021'
    },
    {
        'title': 'Torrent 2',
        'magnet': 'kaljnskndhnakishdihaiushihdaishdihaishdihaishdahsdihahsihaihsdhasidhiahidhiashdia',
        'category': 'movie',
        'posted': '26 March, 2021'
    },
    {
        'title': 'Torrent 3',
        'magnet': 'llllaljnskndhnakishdihaiushihdaishdihaishdihaishdahsdihahsihaihsdhasidhiahidhiashdia',
        'category': 'movie',
        'posted': '26 March, 2021'
    },
    {
        'title': 'Torrent 4',
        'magnet': 'awwwaljnskndhnakishdihaiushihdaishdihaishdihaishdahsdihahsihaihsdhasidhiahidhiashdia',
        'category': 'movie',
        'posted': '26 March, 2021'
    },
    {
        'title': 'Torrent 5',
        'magnet': 'kaljnskndhnakishdihaiushihdaishdihaishdihaishdahsdihahsihaihsdhasidhiahidhiashdia',
        'category': 'movie',
        'posted': '26 March, 2021'
    },
]


views = Blueprint("views", __name__)

@views.route("/")
@views.route("/home")
def home():
    return render_template("index.html", posts=posts)


@views.route("/about")
def about():
    return render_template("about.html")

@views.route("/login", methods=["POST", "GET"])
def login():
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
def post():
    form = PostForm()
    if form.validate_on_submit():
        flash('Post successful.', 'success')
    else:
        if request.method != 'GET':
            flash('Fill the form correctly.', 'danger')
    return render_template("post.html", form=form)