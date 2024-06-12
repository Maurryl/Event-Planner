# from sqlalchemy import Column, Integer, String, ForeignKey
# from sqlalchemy.orm import relationship
# from .base import Base

# class Guest(Base):
#     __tablename__ = 'guests'
    
#     guest_id = Column(Integer, primary_key=True)
#     guest_name = Column(String, nullable=False)
#     email = Column(String, unique=True, nullable=False)
#     event_id = Column(Integer, ForeignKey('events.event_id'))
#     event = relationship('Event', back_populates='guests')
# models/guest.py

from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from .base import Base

class Guest(Base):
    __tablename__ = 'guests'

    guest_id = Column(Integer, primary_key=True, autoincrement=True)
    guest_name = Column(String, nullable=False)
    guest_email = Column(String, nullable=False, unique=True)
    guest_phone = Column(String, nullable=True)
    rsvp_status = Column(String, nullable=False)
    invitation_sent = Column(Boolean, default=False)
    special_requests = Column(String, nullable=True)

    # Relationship with EventGuest
    events = relationship("Event", secondary="guest_event", back_populates="guests")

    def __repr__(self):
        return f"<Guest(guest_name='{self.guest_name}', guest_email='{self.guest_email}', rsvp_status='{self.rsvp_status}')>"
