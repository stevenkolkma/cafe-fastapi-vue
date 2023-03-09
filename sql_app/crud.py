from sqlalchemy.orm import Session
import models, schemas

def get_cafes(db: Session, skip: int = 0, limit: int = 20):
    lists = db.query(models.Cafe).offset(skip).limit(limit).all()
    print(lists)
    return lists

def get_cafe_byId(db: Session, cafe_id: int):
    cafe = db.query(models.Cafe).filter(models.Cafe.id == cafe_id).first()
    print(cafe)
    return cafe

def get_cafe_by_name(db: Session, name: str):
    cafe = db.query(models.Cafe).filter(models.Cafe.name == name).first()
    print(cafe)
    return cafe

def get_drinks_by_cafeId(db: Session, cafe_id: int):
    drink = db.query(models.Cafe).filter(models.Cafe.id == cafe_id).first()
    print(drink)
    return drink

def create_cafe(db:Session, cafe: schemas.Cafe):
    db_cafe = models.Cafe(**cafe.dict())
    db.add(db_cafe)
    db.commit()
    db.refresh(db_cafe)
    return db_cafe
