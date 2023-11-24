#!/usr/bin/python3
"""
Prints all 'City' objects from the database
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from model_city import City, Base
from model_state import State

if __name__ == "__main__":
    # Connect to the MySQL server
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    # Create a Session object
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query all City objects and join with the corresponding State object
    city_state_join = (
            session.query(City, State)
            .join(State, City.state_id == State.id)
            )

    # Sort the results by City ID in ascending order
    sorted_city_state_join = city_state_join.order_by(City.id.asc())

    # Iterate over the sorted City-State pairs
    for city, state in sorted_city_state_join:
        print(f"{state.name}: ({city.id}) {city.name}")

    # Close the Session
    session.close()
