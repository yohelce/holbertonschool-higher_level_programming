#!/usr/bin/python3
""" State Model """

from relationship_state import Base
from sqlalchemy import Column, Integer, String, ForeignKey


class State(Base):
    """ Class of states table """
    __tablename__ = "states"
    id = Column(Integer, autoincrement=True, nullable=False,
                unique=True, primary_key=True)
    name = Column(String(128), nullable=False)
