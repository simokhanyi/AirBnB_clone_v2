#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv


class State(BaseModel, Base):
    """State class / table model"""

    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade="all, delete", backref="state")

    if getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def cities(self):
            """The cities property"""
            from models import storage
            cities_list = []
            for city in storage.all("City").values():
                if city.state_id == self.id:
                    cities_list.append(city)
            return cities_list
