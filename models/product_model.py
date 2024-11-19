from sqlalchemy import Column, Integer, String
from init_db import Base

class Product(Base):
    __tablename__ = 'product'
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    product_number = Column(String, unique=True, index=True)
    product_name = Column(String, unique=True, index=True)
    unit_price = Column(Integer)
    stock = Column(Integer)
    spec = Column(String)
    detail = Column(String)