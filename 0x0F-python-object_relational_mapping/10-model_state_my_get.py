#!/usr/bin/python3
"""
Prints the 'State' object with the 'name'
passed as argument from the database 'hbtn_0e_6_usa'
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from model_state import Base, State

if __name__ == "__main__":
    # Connect to the MySQL server
    if __name__ == "__main__":
        engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                               .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                               pool_pre_ping=True)
    Base.metadata.create_all(engine)

    # Create a Session object
    Session = sessionmaker(bind=engine)
    session = Session()

    # Try to find the state with the specified name
    state = sys.argv[4]
    state_name = session.query(State).filter_by(name=state).first()

    # Check if a state with the specified name exists
    if state_name:
        # Print the state's id
        print(state_name.id)
    else:
        # Display "Not found" if no matching state is found
        print("Not found")

    # Close the Session
    session.close()
