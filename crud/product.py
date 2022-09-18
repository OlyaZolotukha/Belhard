from typing import Optional, List, Tuple

from sqlalchemy.orm import Session
from sqlalchemy import select, update, delete
from sqlalchemy.exc import IntegrityError

from models import Product, OrderItem, create_sync_session


class CRUDProduct:
    @staticmethod
    @create_sync_session
    def add(
            name: str,
            price: float = None,
            descr: str = None,
            category_id: int = None,
            session: Session = None
    ) -> Optional[Product]:
        product = Product(
            name=name,
            price=price,
            descr=descr,
            category_id=category_id,
        )
        session.add(product)
        try:
            session.commit()
        except IntegrityError:
            pass
        else:
            session.refresh(product)
            return product

    @staticmethod
    @create_sync_session
    def get(article: int, session: Session = None) -> Optional[Product]:
        product = session.execute(
            select(Product).where(Product.article == article)
        )
        product = product.first()
        if product:
            return product[0]

    @staticmethod
    @create_sync_session
    def all(category_id: int = None, session: Session = None) -> List[Product]:
        if category_id:
            products = session.execute(
                select(Product)
                .where(Product.category_id == category_id)
                .order_by(Product.article)
            )
        else:
            products = session.execute(
                select(Product)
                .order_by(Product.article)
            )
        return [product[0] for product in products]

    @staticmethod
    @create_sync_session
    def delete(article: int, session: Session = None) -> None:
        session.execute(
            delete(Product)
            .where(Product.article == article)
        )
        session.commit()

    @staticmethod
    @create_sync_session
    def update(
            article: int,
            name: str = None,
            price: float = None,
            descr: str = None,
            category_id: int = None,
            session: Session = None
    ) -> bool:
        if name or price or descr or category_id:
            session.execute(
                update(Product)
                .where(Product.article == article)
                .values(
                    name=name if name else Product.name,
                    price=price if price else Product.price,
                    descr=descr if descr else Product.decsr,
                    category_id=category_id if category_id else Product.category_id
                )
            )
            try:
                session.commit()
            except IntegrityError:
                return False
            else:
                return True
        else:
            return False

    @staticmethod
    @create_sync_session
    def join(article: int = None, session: Session = None) -> List[Tuple[Product, OrderItem]]:
        if article:
            response = session.execute(
                select(Product, OrderItem)
                .join(OrderItem, Product.article == OrderItem.product_article)
                .where(Product.article == article)
            )
        response = session.execute(
            select(Product, OrderItem)
            .join(OrderItem, Product.article == OrderItem.product_article)
        )
        return response.all()
