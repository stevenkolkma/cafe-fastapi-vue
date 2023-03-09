from database import Base
from sqlalchemy import Column, String


class User(Base):
    __tablename__ = "users"

    name = Column(String, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)

