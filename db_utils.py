from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Base

DB_USER = "postgres"
DB_PASSWORD = "123"
DB_HOST = "localhost"
DB_NAME = "myshop2"


def get_session():
    str_connection = f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"
    print(str_connection)
    engine = create_engine(str_connection)
    Session = sessionmaker(bind=engine)
    session = Session()
    return session, engine


def create_all_tables():
    engine = get_session()
    Base.metadata.create_all(bind=engine)


if __name__ == '__main__':
    create_all_tables()
