from sqlalchemy.orm import Session

from . import models, schemas


def get_track(db: Session, track_id: int):
  return db.query(models.Track).filter(models.Track.id == track_id).first()

def create_track(db: Session, track: schemas.TrackCreate):
  db_track = models.Track(title=track.title, artist=track.artist, album_image_path=track.album_image_path, track_path=track.track_path, votes=track.votes)
  db.add(db_track)
  db.commit()
  db.refresh(db_track)
  return db_track

def get_shout_out(db: Session, shout_out_id: int):
  return db.query(models.ShoutOut).filter(models.ShoutOut.id == shout_out_id).first()

def create_shout_out(db: Session, track: schemas.ShoutOutCreate):
  db_shout_out = models.Track(title=shout_out.title, description=shout_out.description, shout_out_path=shout_out.shout_out_path)
  db.add(db_shout_out)
  db.commit()
  db.refresh(db_shout_out)
  return db_shout_out


# Below classes are sample code from FastAPI
def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.User(email=user.email, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Item).offset(skip).limit(limit).all()


def create_user_item(db: Session, item: schemas.ItemCreate, user_id: int):
    db_item = models.Item(**item.dict(), owner_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item