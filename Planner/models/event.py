from sqlalchemy import Column, Integer, String, Date, Time, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class Event(Base):
    __tablename__ = 'events'
    
    event_id = Column(Integer, primary_key=True)
    event_name = Column(String, nullable=False)
    event_description = Column(String)
    event_date = Column(Date)
    event_time = Column(Time)
    guests = relationship('Guest', back_populates='event')
    venues = relationship('Venue', secondary='event_venues', back_populates='events')

    # # Relationship with EventVenue
    # event_venues = relationship("EventVenue", back_populates="event")

    # def __repr__(self):
    #     return f"<Event(event_name='{self.event_name}', event_date='{self.event_date}')>"


