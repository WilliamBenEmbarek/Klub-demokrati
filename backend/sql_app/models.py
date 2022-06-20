from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class Track(Base):
  __tablename__ = "tracks"

  id = Column(Integer, primary_key=True, index=True)
  title = Column(String, index=True)
  artist = Column(String, index=True)
  album_image_path = Column(String, index=True)
  track_path = Column(String, index=True)
  votes = Column(Integer, index=True)


class ShoutOut(Base):
  __tablename__ = "shout_outs"

  id = Column(Integer, primary_key=True, index=True)
  title = Column(String, index=True)
  description = Column(String, index=True)
  shout_out_path = Column(String, index=True)


# Below classes are sample code from FastAPI
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    items = relationship("Item", back_populates="owner")


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="items")
