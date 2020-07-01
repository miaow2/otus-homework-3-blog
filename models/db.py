from sqlalchemy import Column, create_engine, Integer
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base, declared_attr


engine = create_engine("sqlite:///blog.db")


class Base:
    @declared_attr
    def __tablename__(cls):
        return f"blog_{cls.__name__.lower()}s"

    id = Column(Integer, primary_key=True)


session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)
Base = declarative_base(cls=Base, bind=engine)
