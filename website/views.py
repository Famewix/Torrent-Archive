from flask import Blueprint, render_template, url_for, flash, request
import datetime
import os
from .forms import PostForm, LoginForm

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
        flash('Successfully Logged in.', 'success')
    else:
        if request.method != 'GET':
            flash('error', 'danger')
    return render_template("login.html", form=form)

@views.route("/post", methods=['GET','POST'])
def post():
    form = PostForm()
    if form.validate_on_submit():
        flash('Post successful.', 'success')
    else:
        if request.method != 'GET':
            flash('error', 'danger')
    return render_template("post.html", form=form)