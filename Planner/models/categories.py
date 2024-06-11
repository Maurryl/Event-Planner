# models/categories.py

from sqlalchemy import Column, Integer, String
from .base import Base

class Category(Base):
    __tablename__ = 'categories'

    category_id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String)

    def __init__(self, name, description=None):
        self.name = name
        self.description = description

    def __repr__(self):
        return f"<Category(name='{self.name}', description='{self.description}')>"
