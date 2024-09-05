from sqlalchemy import Column, Integer, String, Date, Float, Boolean, ForeignKey, LargeBinary
from sqlalchemy.orm import DeclarativeBase, relationship


class Base(DeclarativeBase): pass


class Employees(Base):
    """Сотрудник"""
    __tablename__ = 'employees'
    id_employee = Column(Integer(), primary_key=True)
    family = Column(String(50), nullable=False)
    name = Column(String(50), nullable=False)
    suraname = Column(String(50))
    job_title = Column(String(100))
    address = Column(String(255), nullable=False)
    home_phone = Column(String(10), nullable=False)
    birthday = Column(Date(), nullable=False)


class Client(Base):
    """Заказчик"""
    __tablename__ = 'client'
    id_client = Column(Integer(), primary_key=True)
    fullname = Column(String(150), nullable=False)
    address = Column(String(255), nullable=False)
    phone = Column(String(10), nullable=False)
    orders = relationship("Orders", backref="order")



class Provider(Base):
    """Поставщик"""
    __tablename__ = 'provider'
    id_provider = Column(Integer(), primary_key=True)
    name_of_provider = Column(String(50), nullable=False)
    representative = Column(String(100))
    speak_to = Column(String(100))
    phone = Column(String(10), nullable=False)
    address = Column(String(255), nullable=False)
    supplies = relationship("Supply", backref="supply")


class Supply(Base):
    """Поступление"""
    __tablename__ = 'supply'
    id_supply = Column(Integer(), primary_key=True)
    id_provider = Column(Integer(), ForeignKey('provider.id_provider'))
    data_of_supply = Column(Date(), nullable=False)


class Products(Base):
    """Товары"""
    __tablename__ = 'products'
    id_product = Column(Integer(), primary_key=True)
    id_supply = Column(Integer(), ForeignKey('supply.id_supply'))
    name_of_product = Column(String(50), nullable=False)
    specifications = Column(String(255), nullable=False)
    description = Column(String(255), nullable=False)
    image = Column(LargeBinary())
    purchase_cost = Column(Float())
    availability = Column(Boolean())
    quantity = Column(Integer())
    selling_price = Column(Float())


class Orders(Base):
    """Заказы"""
    __tablename__ = 'orders'
    id_order = Column(Integer(), primary_key=True)
    id_employee = Column(Integer(), ForeignKey('employees.id_employee'))
    id_product = Column(Integer(), ForeignKey('products.id_product'))
    id_client = Column(Integer(), ForeignKey('client.id_client'))
    posting_date = Column(Date(), nullable=False)
    execution_date = Column(Date(), nullable=False)
