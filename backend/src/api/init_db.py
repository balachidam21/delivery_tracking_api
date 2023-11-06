from database import Base, engine
from models import Order, Product, User

Base.metadata.create_all(bind=engine)
