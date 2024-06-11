from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class Guest(Base):
    __tablename__ = 'guests'
    
    guest_id = Column(Integer, primary_key=True)
    guest_name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    event_id = Column(Integer, ForeignKey('events.event_id'))
    event = relationship('Event', back_populates='guests')
