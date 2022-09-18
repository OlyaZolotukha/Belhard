from sqlalchemy import (Column, SmallInteger, VARCHAR,
                        ForeignKey, TIMESTAMP, CHAR, DECIMAL, BOOLEAN)
from sqlalchemy.orm import declarative_base
from datetime import datetime

Base = declarative_base()


class Category(Base):
    __tablename__: str = 'categories'

    id = Column(SmallInteger, primary_key=True)
    name = Column(VARCHAR(20), nullable=False, unique=True)
    parent_id = Column(
        SmallInteger,
        ForeignKey('categories.id', ondelete='CASCADE')
    )


class Product(Base):
    __tablename__: str = 'products'

    article = Column(CHAR(6), primary_key=True)
    name = Column(VARCHAR(20), nullable=False)
    price = Column(DECIMAL(8, 2), default=0)
    data_created = Column(TIMESTAMP, default=datetime.utcnow())
    decsr = Column(VARCHAR(140))
    category_id = Column(
        SmallInteger,
        ForeignKey('categories.id', ondelete='CASCADE'),
        nullable=False
    )


class User(Base):
    __tablename__: str = 'users'

    id = Column(SmallInteger, primary_key=True)
    name = Column(VARCHAR(20), nullable=False)
    email = Column(VARCHAR(36), nullable=False, unique=True)


class Order(Base):
    __tablename__: str = 'orders'

    id = Column(SmallInteger, primary_key=True)
    user_id = Column(
        SmallInteger,
        ForeignKey('users.id', ondelete='CASCADE'),
        nullable=False
    )
    is_paid = Column(BOOLEAN, default=False, nullable=False)
    data_created = Column(TIMESTAMP, default=datetime.utcnow(), nullable=False)


class OrderItem(Base):
    __tablename__: str = 'order_items'

    id = Column(SmallInteger, primary_key=True)
    product_article = Column(
        CHAR(6),
        ForeignKey('products.article', ondelete='NO ACTION'),
        nullable=False)
    order_id = Column(
        SmallInteger,
        ForeignKey('orders.id', ondelete='CASCADE'),
        nullable=False
    )
