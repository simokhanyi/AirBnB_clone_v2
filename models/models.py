#!/usr/bin/python3
"""
Module containing SQLAlchemy models for the AirBnB Clone project.
"""


from sqlalchemy import Column, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


Base = declarative_base()


class State(Base):
    """
    State model class representing a state in the AirBnB Clone project.
    """
    __tablename__ = 'states'
    id = Column(String(60), primary_key=True)
    name = Column(String(128), nullable=False)