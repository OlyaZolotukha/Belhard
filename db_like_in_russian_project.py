from datetime import datetime
from sqlalchemy.orm import declarative_base

from sqlalchemy import Column, SmallInteger, VARCHAR, ForeignKey, TIMESTAMP, DECIMAL, BOOLEAN

Base = declarative_base()


class Category(Base):
    __tablename__: str = 'categories'

    id = Column(SmallInteger, primary_key=True)
    parent_id = Column(SmallInteger, ForeignKey('categories.id', ondelete='CASCADE'))
    is_published = Column(BOOLEAN, default=False, nullable=False)
    name = Column(VARCHAR(20), nullable=False, unique=True)


class Product(Base):
    __tablename__: str = 'products'

    id = Column(SmallInteger, primary_key=True)
    category_id = Column(SmallInteger, ForeignKey('categories.id', ondelete='CASCADE'))
    price = Column(DECIMAL(8, 2), default=0)
    media = Column(VARCHAR(170), default=False)
    total = Column(DECIMAL(8, 2), default=0)
    is_published = Column(BOOLEAN, default=False, nullable=False)
    name = Column(VARCHAR(20), nullable=False, unique=True)


class Language(Base):
    __tablename__: str = 'languages'

    id = Column(SmallInteger, primary_key=True)
    language_code = Column(VARCHAR(2), nullable=False)


class BotUser(Base):
    __tablename__: str = 'bot_users'

    id = Column(SmallInteger, primary_key=True)
    is_blocked = Column(BOOLEAN, default=False, nullable=False)
    balance = Column(DECIMAL(8, 2), default=0)
    language_id = Column(SmallInteger, ForeignKey('languages.id', ondelete='CASCADE'))


class Status(Base):
    __tablename__: str = 'statuses'

    id = Column(SmallInteger, primary_key=True)
    name = Column(VARCHAR(20), nullable=False, unique=True)


class Invoice(Base):
    __tablename__: str = 'invoices'

    id = Column(SmallInteger, primary_key=True)
    bot_user_id = Column(SmallInteger, ForeignKey('bot_users.id', ondelete='CASCADE'))
    data_create = Column(TIMESTAMP, default=datetime.utcnow())
    total = Column(DECIMAL(8, 2), default=0)
    status_id = Column(SmallInteger, ForeignKey('statuses.id', ondelete='CASCADE'))


class Order(Base):
    __tablename__: str = 'orders'

    id = Column(SmallInteger, primary_key=True)
    bot_user_id = Column(SmallInteger, ForeignKey('bot_users.id', ondelete='CASCADE'))
    data_create = Column(TIMESTAMP, default=datetime.utcnow())
    status_id = Column(SmallInteger, ForeignKey('statuses.id', ondelete='CASCADE'))
    invoice_id = Column(SmallInteger, ForeignKey('invoices.id', ondelete='CASCADE'))


class OrderItem(Base):
    __tablename__: str = 'order_items'

    id = Column(SmallInteger, primary_key=True)
    product_id = Column(SmallInteger, ForeignKey('products.id', ondelete='CASCADE'))
    total = Column(DECIMAL(8, 2), default=0)
