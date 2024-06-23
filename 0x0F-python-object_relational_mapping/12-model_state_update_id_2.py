#!/usr/bin/python3
"""
Changes the name of the State object with id = 2 to "New Mexico".
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Create the engine
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            username,
            password,
            database),
        pool_pre_ping=True)

    # Create session
    Session = sessionmaker(bind=engine)

    # Context manager for session handling
    with Session() as session:
        # Query for the state with id = 2
        state_to_update = session.query(State).filter_by(id=2).first()

        if state_to_update:
            # Update the name attribute
            state_to_update.name = "New Mexico"
            session.commit()
            print("State name updated successfully!")
        else:
            print("State with id = 2 not found.")
