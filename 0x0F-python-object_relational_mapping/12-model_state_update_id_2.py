#!/usr/bin/python3
"""
Changes the name of a State object in the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == '__main__':
    # Get the input arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Create the engine to access the db and session to interact with it
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(mysql_username, mysql_password,
                                   database_name),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Get the State object with id = 2
    state = session.query(State).filter(State.id == 2).first()

    # Change the name of the state to "New Mexico"
    if state:
        state.name = "New Mexico"
        session.commit()
    else:
        print("Nothing")
