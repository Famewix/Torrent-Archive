from flask import Blueprint, render_template, url_for
import datetime
import os

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