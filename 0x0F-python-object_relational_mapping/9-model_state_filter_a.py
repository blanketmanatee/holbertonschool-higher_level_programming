#!/usr/bin/python3


if __name__ == "__main__":
    from sqlalchemy import (create_engine)
    from sqlalchemy.orm import sessionmaker
    from model_state import Base, State
    from sys import argv
    Session = sessionmaker()
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_pring=True)
    session = Session(bind=engine)
    Base.metadata.create_all(engine)
    instances = session.query(State).filter(State.name.link('%a%'))\
                .order_by(State.id).all()
    if instances:
        for instance in instances:
            if 'a' in instance.name:
                print("{}: {}".format(instance.id, instance.name))
    session.close()
