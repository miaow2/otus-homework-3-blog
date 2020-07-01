from logging import getLogger

from flask import Blueprint, redirect, render_template, request, url_for
from flask_login import (
    current_user,
    login_user,
    logout_user,
    login_required,
)
from werkzeug.exceptions import BadRequest, InternalServerError

from models import User
from models.db import Session


logger = getLogger(__name__)

auth = Blueprint("auth", __name__)


@auth.route("/register/", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("home"))

    if request.method == "GET":
        return render_template("auth/register.html", user=current_user)

    username = request.form.get("username")
    password = request.form.get("password")
    if not (username and len(username) >= 3 and password and len(password) >= 4):
        return render_template(
            "auth/register.html",
            error_text="Username has to be at least 3 symbols and pass min 5",
            user=current_user,
        )
    if Session.query(User).filter_by(username=username).count():
        return render_template(
            "auth/register.html",
            error_text=f"Username {username!r} already exists!",
            user=current_user,
        )

    user = User(username, password)
    Session.add(user)

    try:
        Session.commit()
    except Exception as e:
        logger.exception("Error creating user!")
        raise InternalServerError(f"Could not create new user! Error: {e}")

    login_user(user)
    return redirect(url_for("home"))


@auth.route("/login/", methods=["GET", "POST"], endpoint="login")
def login():
    if current_user.is_authenticated:
        return redirect(url_for("home"))

    if request.method == "GET":
        return render_template("auth/login.html", user=current_user)

    username = request.form.get("username")
    password = request.form.get("password")

    user = Session.query(User).filter_by(username=username).one_or_none()

    if not user:
        return render_template("auth/login.html", error_text="User not found")

    if user.password != User.hash_password(password):
        return render_template(
            "auth/login.html",
            error_text="Invalid username or password!",
            user=current_user,
        )

    login_user(user)
    return redirect(url_for("home"))


@auth.route("/logout/", endpoint="logout")
def logout():
    logout_user()
    return redirect(url_for("home"))


@auth.route("/profile/", endpoint="profile")
@login_required
def profile():
    return render_template("auth/profile.html", user=current_user)
