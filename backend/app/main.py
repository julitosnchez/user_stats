import schemas
import crud
import models

from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from db import get_db, engine

models.Base.metadata.create_all(bind=engine)


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/user/{user_id}", response_model=schemas.User)
def create_user(user_id: int, db: Session = Depends(get_db)):
    return crud.get_user(db=db, user_id=user_id)


@app.post("/user/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db=db, user=user)
