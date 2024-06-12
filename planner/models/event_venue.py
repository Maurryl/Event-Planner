from sqlalchemy import Column, Integer, ForeignKey, Time
from sqlalchemy.orm import relationship
from .base import Base

class EventVenue(Base):
    __tablename__ = 'event_venues'

    event_venue_id = Column(Integer, primary_key=True)
    event_id = Column(Integer, ForeignKey('events.event_id'))
    venue_id = Column(Integer, ForeignKey('venues.venue_id'))
    setup_start_time = Column(Time)
    cleanup_end_time = Column(Time)

    event = relationship("Event", back_populates="event_venues")
    venue = relationship("Venue", back_populates="event_venues")

    def __repr__(self):
        return f"<EventVenue(event_id={self.event_id}, venue_id={self.venue_id}, setup_start_time='{self.setup_start_time}', cleanup_end_time='{self.cleanup_end_time}')>"

