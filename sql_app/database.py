# import SQLAlchemy parts
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# create a database url for sqlalchemy
SQLALCHEMY_DATABASE_URL = "ADD_DATABASE_URL_HERE"

# create SQLAlchemy enginne
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# create SessionLocal class with sessionmaker
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# base class, will use later to create models or classes
Base = declarative_base()
