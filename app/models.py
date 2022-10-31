from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import declarative_base

from app.config import DATABASE_URL


Base = declarative_base()


def get_connection():
    engine = create_engine(DATABASE_URL, connect_args={'check_same_thread': False})
    # the second arg 'check_same_thread' allows to skip thread warnings
    session = Session(bind=engine.connect())
    return session


class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    name = Column(String)


class Category(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True)
    name = Column(String)


class Store(Base):
    __tablename__ = 'store'

    id = Column(Integer, primary_key=True)
    category_id = Column(Integer)
    product_id = Column(Integer)
