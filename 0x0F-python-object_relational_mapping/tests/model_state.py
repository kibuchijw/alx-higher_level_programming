#!/usr/bin/python3
"""
Contains class definition of a 'State'
and and instance 'Base = declarative_base()'
"""
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    __tablename__ = "states"
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)


# Connect to the MySQL server on localhost at port 3306
engine = create_engine('mysql://username:password@localhost:3306/database_name')

if __name__ == "__main__":
    # Create tables by calling create_all() with the engine
    Base.metadata.create_all(engine)
