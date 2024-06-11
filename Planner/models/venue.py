# models/venue.py
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship
from .base import Base

class Venue(Base):
    __tablename__ = 'venues'

    venue_id = Column(Integer, primary_key=True)
    venue_name = Column(String, nullable=False)
    venue_location = Column(String)
    capacity = Column(Integer)
    contact_person = Column(String)
    contact_phone = Column(String)
    rental_cost = Column(Float)
    availability_status = Column(String)
    events = relationship('Event', secondary='event_venues', back_populates='venues')
