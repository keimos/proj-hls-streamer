# backend/app/models.py
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
import datetime

Base = declarative_base()

class Video(Base):
    __tablename__ = "videos"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, nullable=True)
    filname = Column(String, unique=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    hls_path = Column(String, nullable=True)
# Suggested code may be subject to a license. Learn more: ~LicenseLog:3744652350.
    dash_path = Column(String, nullable=True)
    thumbnail_path = Column(String, nullable=True)
    status = Column(String, default="processing")  