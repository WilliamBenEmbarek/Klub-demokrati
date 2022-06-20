from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



@app.get("/tracks/{track_id}", response_model=schemas.Track)
def read_track(track_id: int, db: Session = Depends(get_db)):
    db_track = crud.get_track(db, track_id=track_id)
    if db_track is None:
        raise HTTPException(status_code=404, detail="Track not found")
    return db_track

@app.post("/tracks/", response_model=schemas.Track)
def create_track(track: schemas.TrackCreate, db: Session = Depends(get_db)):
    return crud.create_track(db=db, track=track)

@app.get("/shout_outs/{shout_out_id}", response_model=schemas.ShoutOut)
def read_shout_out(shout_out_id: int, db: Session = Depends(get_db)):
    db_shout_out = crud.get_shout_out(db, shout_out_id=shout_out_id)
    if db_shout_out is None:
        raise HTTPException(status_code=404, detail="Shout out not found")
    return db_shout_out

@app.post("/shout_outs/", response_model=schemas.ShoutOut)
def create_shout_out(shout_out: schemas.ShoutOutCreate, db: Session = Depends(get_db)):
    return crud.create_shout_out(db=db, shout_out=shout_out)


# Below classes are sample code from FastAPI
@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)


@app.get("/users/", response_model=List[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@app.post("/users/{user_id}/items/", response_model=schemas.Item)
def create_item_for_user(
    user_id: int, item: schemas.ItemCreate, db: Session = Depends(get_db)
):
    return crud.create_user_item(db=db, item=item, user_id=user_id)


@app.get("/items/", response_model=List[schemas.Item])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = crud.get_items(db, skip=skip, limit=limit)
    return items
