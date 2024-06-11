# models/base.py
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()
engine = create_engine('sqlite:///event_planner.db')
Session = sessionmaker(bind=engine)
session = Session()
