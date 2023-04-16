#!/usr/bin/python3
"""
Lists all State objects that contain the letter a
from the database hbtn_0e_6_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
"""import modules"""

if __name__ == '__main__':
    # Get MySQL credentials
    mysql_user = sys.argv[1]
    mysql_pwd = sys.argv[2]
    mysql_db = sys.argv[3]

    # Setup connection and session to database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(mysql_user, mysql_pwd, mysql_db),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query database for states containing 'a'
    states = session.query(State).filter(State.name.
                                         like('%a%')).order_by(State.id)

    # Print out the results
    for state in states:
        print('{}: {}'.format(state.id, state.name))

    # If no results found
    if states.count() == 0:
        print('Nothing')
