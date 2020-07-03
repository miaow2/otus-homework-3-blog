import os

from logging import getLogger

from flask import Flask, redirect, render_template, request, url_for
from flask_login import current_user, LoginManager
from sqlalchemy import desc


from models import Post, User
from models.db import Session
from views.auth import auth
from views.post import post


logger = getLogger(__name__)

app = Flask(__name__)
app.config.update(SECRET_KEY=os.environ.get("FLASK_SECRET_KEY"))

login_manager = LoginManager()
login_manager.init_app(app)

app.register_blueprint(auth, url_prefix="/auth")
app.register_blueprint(post, url_prefix="/post")


@login_manager.user_loader
def load_user(user_id):
    return Session.query(User).filter_by(id=user_id).one_or_none()


@app.route("/", endpoint="home")
def index():
    if current_user.is_authenticated:
        posts = Session.query(Post).order_by(desc(Post.id)).all()
        return render_template("index.html", posts=posts, user=current_user)
    return redirect(url_for("auth.login"))


@app.route("/contacts/", endpoint="contacts")
def contacts():
    return render_template("contacts.html", user=current_user)


@app.teardown_request
def remove_session(*args):
    Session.remove()


if __name__ == "__main__":
    app.run()
