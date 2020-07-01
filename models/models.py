import hashlib

from datetime import datetime
from flask_login import UserMixin
from sqlalchemy import Column, DateTime, Integer, ForeignKey, String, Text
from sqlalchemy.orm import relationship

from .db import Base


class User(Base, UserMixin):
    username = Column(String(32), nullable=False, unique=True)
    _password = Column("password", String(32), nullable=False)

    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value: str):
        self._password = self.hash_password(value)

    @classmethod
    def hash_password(cls, value: str) -> str:
        return hashlib.md5(value.encode("utf-8")).hexdigest()

    def __repr__(self):
        return f"<User #{self.id} {self.username}>"

    posts = relationship("Post", back_populates="user")


class Post(Base):

    user_id = Column(Integer, ForeignKey(User.id), nullable=False)
    title = Column(String(50), nullable=False)
    text = Column(Text, nullable=False)
    date_created = Column(DateTime, default=datetime.utcnow)

    user = relationship(User, back_populates="posts")

    def __init__(self, title: str, text: str, user_id: int):
        self.title = title
        self.text = text
        self.user_id = user_id

    def __repr__(self):
        return f"<Post #{self.id} {self.title}>"

