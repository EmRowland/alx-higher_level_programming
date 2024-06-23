#!/usr/bin/python3
"""
Deletes all State objects with a name containing the letter 'a'.
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
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(username, password, database),
                           pool_pre_ping=True)

    # Create session
    Session = sessionmaker(bind=engine)

    # Context manager for session handling
    with Session() as session:
        # Query for states containing 'a' in their name
        states_to_delete = session.query(State).filter(State.name.like('%a%')).all()
        
        if states_to_delete:
            for state in states_to_delete:
                session.delete(state)
            session.commit()
            print("Deleted {} states.".format(len(states_to_delete)))
        else:
            print("No states found with names containing 'a'.")



