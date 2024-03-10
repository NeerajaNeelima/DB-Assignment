from sqlalchemy import Column, Integer, String, Text, DateTime, Boolean, Numeric, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class ProductCategory(Base):
    __tablename__ = 'product_category'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    desc = Column(Text)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    modified_at = Column(DateTime, default=datetime.datetime.utcnow)
    deleted_at = Column(DateTime)
    products = relationship('Product', back_populates='category')

class ProductInventory(Base):
    __tablename__ = 'product_inventory'
    id = Column(Integer, primary_key=True)
    SKU = Column(String(255), nullable=False)
    quantity = Column(Integer, nullable=False)
    category_id = Column(Integer, ForeignKey('product_category.id'))
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    inventory_id = Column(Integer)
    modified_at = Column(DateTime, default=datetime.datetime.utcnow)
    price = Column(Numeric(10, 2))
    deleted_at = Column(DateTime)
    discount_id = Column(Integer, ForeignKey('discount.id'))
    created_at_discount = Column(DateTime)
    modified_at_discount = Column(DateTime)

class Discount(Base):
    __tablename__ = 'discount'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    desc = Column(Text)
    discount_percent = Column(Numeric(5, 2), nullable=False)
    active = Column(Boolean, nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    modified_at = Column(DateTime, default=datetime.datetime.utcnow)
    deleted_at = Column(DateTime)

class Product(Base):
    __tablename__ = 'product'
    id = Column(Integer, primary_key=True)