from flask import Blueprint, redirect, render_template, request, send_from_directory, url_for
from flask_login import current_user

index_views = Blueprint("index_views", __name__, template_folder="../templates")


@index_views.route("/", methods=["GET"])
def index_page():
    return render_template("index.html")
    # if current_user.is_authenticated():
    #     return render_template("index.html")
    # return redirect(url_for('index_views.login_page'))

@index_views.route("/login", methods=['GET'])
def login_page():
    return render_template('login.html')

@index_views.route("/signup", methods=['GET'])
def signup_page():
    return render_template('signup.html')
