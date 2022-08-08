#!/usr/bin/python3
"""Definition of the State class"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class State(Base):
    """
    Inherits from Base
    """
    __tablename__ = "states"
    id = Column(Integer, autoincrement=True, nullable=False,
                unique=True, primary_key=True)
    name = Column(String(128), nullable=False)
