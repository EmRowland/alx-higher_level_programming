#!/usr/bin/python3
"""
Prints all City objects from the database hbtn_0e_14_usa.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

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
        # Query for all City objects, joining with State to get state names
        cities = session.query(City).join(State).order_by(City.id).all()

        if cities:
            for city in cities:
                print(
                    "{}: ({}) {}".format(
                        city.state.name,
                        city.id,
                        city.name))
        else:
            print("No cities found.")
