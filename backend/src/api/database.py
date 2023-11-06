from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine("postgresql://postgres:postgres977880@localhost:5432/delivery_db", echo=True)

Base = declarative_base()

Session = sessionmaker(bind=engine)

session = Session()
