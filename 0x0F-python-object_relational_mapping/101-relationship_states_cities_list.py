#!/usr/bin/python3
"""
Creates the 'State' Californias with the 'City' San Francisco
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import State
from relationship_city import Base, City


if __name__ == "__main__":
    # Connect to the MySQL server
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # List all State objects and corresponding City ojects
    for state in session.query(State).order_by(State.id):
        print(f"{state.id} {state.name}")
        for city in state.cities:
            print(f"    {city.id}: {city.name}")

    # Commit the changes
    session.commit()
