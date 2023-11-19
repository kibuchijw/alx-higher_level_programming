from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from model_state import Base, State

if __name__ == "__main__":
    # Connect to the MySQL server
    engine = create_engine('mysql+pymysql://username:password@localhost:3306/database_name')

    # Create a Session object
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query all State objects
    states = session.query(State).order_by(State.id.asc())

    # Print the results
    for state in states:
        print(f"{state.id} - {state.name}")

    # Close the Session
    session.close()

