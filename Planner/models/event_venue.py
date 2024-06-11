from sqlalchemy import Column, Integer, ForeignKey, Time
from .base import Base

class EventVenue(Base):
    __tablename__ = 'event_venues'

    event_venue_id = Column(Integer, primary_key=True)
    event_id = Column(Integer, ForeignKey('events.event_id'))
    venue_id = Column(Integer, ForeignKey('venues.venue_id'))
    setup_start_time = Column(Time)
    cleanup_end_time = Column(Time)
