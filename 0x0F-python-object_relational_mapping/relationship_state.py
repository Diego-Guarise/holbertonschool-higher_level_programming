#!/usr/bin/python3
"""City relationship"""


from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from relationship_city import City, Base

Base = declarative_base()


class State(Base):
    """class state"""
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    cities = relationship('City', backref='state',
                          cascade='all, delete-orphan')
