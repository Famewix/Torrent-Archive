from flask import Blueprint, render_template, url_for
import datetime
import os


views = Blueprint("views", __name__)

@views.route("/")
@views.route("/home")
def home():
    return render_template("index.html")


@views.route("/about")
def about():
    return render_template("about.html")