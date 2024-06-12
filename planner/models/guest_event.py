# models/guest_event.py

from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class GuestEvent(Base):
    __tablename__ = 'guest_event'

    guest_id = Column(Integer, ForeignKey('guests.guest_id'), primary_key=True)
    event_id = Column(Integer, ForeignKey('events.event_id'), primary_key=True)

    guest = relationship("Guest", back_populates="events")
    event = relationship("Event", back_populates="guests")

    def __repr__(self):
        return f"<GuestEvent(guest_id={self.guest_id}, event_id={self.event_id})>"
