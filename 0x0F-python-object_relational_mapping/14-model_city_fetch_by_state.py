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
    Base.metadata.create_all(engine)
    # Context manager for session handling
    with Session() as session:
        # Query for all City objects, joining with State to get state names
        cities = session.query(State, City).join(City).order_by(City.id).all()
        for state, city in cities:
            print('{}: ({}) {}'.format(state.name, city.id, city.name))
        session.close()