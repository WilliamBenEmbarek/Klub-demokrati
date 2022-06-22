from typing import List, Union

from pydantic import BaseModel


class TrackBase(BaseModel):
  title: str
  artist: str
  album_image_path: str
  track_path: str
  votes: int


class TrackCreate(TrackBase):
  pass


class Track(TrackBase):
  id: int

  class Config:
    orm_mode = True


class ShoutOutBase(BaseModel):
  title: str
  description: str
  track_path: str


class ShoutOutCreate(ShoutOutBase):
  pass


class ShoutOut(ShoutOutBase):
  id: int

  class Config:
    orm_mode = True


# Below classes are sample code from FastAPI
class ItemBase(BaseModel):
    title: str
    description: Union[str, None] = None


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    items: List[Item] = []

    class Config:
        orm_mode = True
