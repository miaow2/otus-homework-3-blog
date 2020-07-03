from logging import getLogger

from flask import Blueprint, redirect, render_template, request, url_for
from flask_login import (
    current_user,
    login_user,
    logout_user,
    login_required,
)
from werkzeug.exceptions import BadRequest, InternalServerError

from models import Post
from models.db import Session


logger = getLogger(__name__)

post = Blueprint("post", __name__)


def validate_user_credentials(username: str, password: str):
    if not (username and len(username) >= 3 and password and len(password) >= 4):
        raise BadRequest("Username has to be at least 3 symbols and pass min 4")


def get_username_and_password_from_form(form: dict):
    username = form.get("username")
    password = form.get("password")
    validate_user_credentials(username, password)
    return username, password


@post.route("/add/", methods=["GET", "POST"], endpoint="add_post")
@login_required
def add_post():

    if request.method == "GET":
        return render_template("post/add_post.html", user=current_user)

    title = request.form["title"]
    text = request.form["text"]
    if not title:
        return render_template(
            "post/add_post.html", error_text="Title can't be empty", user=current_user
        )
    if not text:
        return render_template(
            "post/add_post.html", error_text="Text can't be empty", user=current_user
        )
    new_post = Post(title, text, current_user.id)
    Session.add(new_post)
    try:
        Session.commit()
    except Exception as e:
        logger.exception("Error creating post!")
        raise InternalServerError(f"Could not create new post! Error: {e}")

    return redirect(url_for("home"))


@post.route("/<int:id>/")
@login_required
def post_view(id):
    post = Session.query(Post).filter_by(id=id).one_or_none()
    if post:
        return render_template("post/post.html", user=current_user, post=post)
    else:
        return redirect(url_for("home"))
