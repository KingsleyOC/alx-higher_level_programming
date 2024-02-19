#!/usr/bin/python3
"""Script that creates the State "California" with the City "San Francisco"
from the database hbtn_0e_100_usa"""

from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from relationship_state import Base, State
from relationship_city import City
import sys

if __name__ == "__main__":
    # Connect to MySQL server using SQLAlchemy
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    # Create tables in the database if not already exist
    Base.metadata.create_all(engine)

    # Create a session to interact with the database
    session = Session(engine)

    # Create a new State "California"
    california = State(name="California")

    # Create a new City "San Francisco" and associate it with the State
    san_francisco = City(name="San Francisco", state=california)

    # Add the State and City objects to the session
    session.add(california)
    session.add(san_francisco)

    # Commit the changes to the database
    session.commit()

    # Close the session
    session.close()
