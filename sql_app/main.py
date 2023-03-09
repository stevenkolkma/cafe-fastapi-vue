from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
import models, database, schemas, crud
models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

origins = ["*"]

app.add_middleware(
  CORSMiddleware, 
  allow_origins=origins, 
  allow_credentials=True, 
  allow_methods=["*"],
  allow_headers=["*"]
)

def get_db():
  db = database.SessionLocal()
  try:
    yield db
  finally:
    db.close()


@app.get("/cafes", response_model=list[schemas.Cafe])
def get_cafes(db: Session = Depends(get_db)):
  return crud.get_cafes(db)

@app.post("/cafes", response_model=schemas.Cafe)
def create_list(cafe: schemas.Cafe, db: Session = Depends(get_db)):
  return crud.create_cafe(db, cafe=cafe)
