#!/usr/bin/python3
"""Allates via SQLAlchemy"""


if __name__ == "__main__":
    import sys
    from model_state import Base, State
    from sqlalchemy.orm import Session
    from sqlalchemy import (create_engine)

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'
        .format(sys.argv[1], sys.argv[2], sys.argv[3]),
        pool_pre_ping=True)

    Base.metadata.create_all(engine)

    session = Session(engine)
    state = session.query(State).first()
    if state:
        print("{}: {}".format(state.id, state.name))
    else:
        print("Nothing")
    session.close()
