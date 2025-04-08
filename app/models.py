# app/models.py
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from .database import Base

class Song(Base):
    __tablename__ = "songs"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), index=True)
    artist = Column(String(100), index=True)
    genre = Column(String(50))
    added_at = Column(DateTime(timezone=True), server_default=func.now())

# Add more models here (e.g., User, Rating) later