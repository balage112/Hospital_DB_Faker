from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from A_login_0 import user, password

def cr_engine():
    CONNECTION_STRING = f"mysql+mysqlconnector://{user}:{password}@localhost:3306/hospital"
    return create_engine(CONNECTION_STRING)

def cr_seassion():
    Seassion = sessionmaker(bind=cr_engine())
    return Seassion()