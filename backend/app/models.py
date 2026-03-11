from sqlalchemy import Column, Integer, String, Float
from .database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String, unique=True)
    role = Column(String)  # donor or ngo
    latitude = Column(Float)
    longitude = Column(Float)


class Donation(Base):
    __tablename__ = "donations"

    id = Column(Integer, primary_key=True, index=True)
    food_type = Column(String)
    quantity = Column(Integer)
    latitude = Column(Float)
    longitude = Column(Float)
    expiry_time = Column(String)
    status = Column(String, default="available")