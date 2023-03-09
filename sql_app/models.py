from database import Base
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship


class Cafe(Base):
    __tablename__ = "cafes"
    
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    name = Column(String, index=True)
    address = Column(String, index=True)

    # drinks = relationship("Drink", back_populates="cafe")

class Drink(Base):
    __tablename__ = "drinks"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    name = Column(String, index=True)
    price = Column(String, index=True)
    description = Column(String, index=True)
    cafe_id = Column(Integer, ForeignKey("drinks.id"))

    # cafe = relationship("Cafe", back_populates="drinks")