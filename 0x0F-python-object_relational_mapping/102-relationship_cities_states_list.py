#!/usr/bin/python3
"""Script that lists all City objects from the database hbtn_0e_101_usa"""

from sqlalchemy import create_engine, text
from sqlalchemy.orm import Session
from relationship_city import Base, City, State
import sys

if __name__ == "__main__":
    # Connect to MySQL server using SQLAlchemy
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    # Create a session to interact with the database
    session = Session(engine)

    # Query to retrieve City objects and their associated State objects
    query = text("SELECT cities.id, cities.name, states.name FROM cities "
                 "JOIN states ON cities.state_id = states.id "
                 "ORDER BY cities.id")

    # Execute the query
    result = session.execute(query)

    # Fetch all the rows and print the results
    for row in result.fetchall():
        print("{}: {} -> {}".format(row[0], row[1], row[2]))

    # Close the session
    session.close()
