#!/usr/bin/python3
"""
Script that prints the State object with the name passed as
argument from the database hbtn_0e_6_usa.
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
"""import modules"""


if __name__ == '__main__':
    user = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    # dialect+driver://username:password@host:port/database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(user, password, db_name))

    Base.metadata.create_all(engine)

    # create session factory bound to the engine
    Session = sessionmaker(bind=engine)

    # create session
    session = Session()

    # query State objects that contain the letter a
    query = session.query(State).filter(State.name == state_name).first()

    if query:
        print(query.id)
    else:
        print('Not found')

    session.close()
