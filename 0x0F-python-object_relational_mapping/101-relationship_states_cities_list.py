#!/usr/bin/python3
""" Get state"""


if __name__ == "__main__":
    import sys
    from model_state import Base, State
    from sqlalchemy.orm import Session
    from sqlalchemy import (create_engine)
    from model_city import City

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'
        .format(sys.argv[1], sys.argv[2], sys.argv[3]),
        pool_pre_ping=True)

    Base.metadata.create_all(engine)

    session = Session(engine)
    state = session.query(State, City).order_by(City.id)\
        .filter(City.state_id == State.id).all()
    for i in state:
        print("{}: ({}) {}".format(i.State.name, i.City.id, i.City.name))
    session.close()
