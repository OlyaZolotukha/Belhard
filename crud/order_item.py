from typing import Optional

from sqlalchemy.orm import Session
from sqlalchemy import select, update, delete
from sqlalchemy.exc import IntegrityError

from models import OrderItem, create_sync_session


class CRUDOrderItem:
    @staticmethod
    @create_sync_session
    def add(order_id: int, product_article: int, session: Session = None) -> Optional[OrderItem]:
        order_item = OrderItem(
            order_id=order_id,
            product_article=product_article
        )
        session.add(order_id)
        try:
            session.commit()
        except IntegrityError:
            pass
        else:
            session.refresh(order_id)
            return order_item

    @staticmethod
    @create_sync_session
    def get(order_item_id: int, session: Session = None) -> Optional[OrderItem]:
        order_item_id = session.execute(
            select(OrderItem).where(OrderItem.order_id == order_item_id)
        )
        order_item_id = order_item_id.first()
        if order_item_id:
            return order_item_id[0]

    @staticmethod
    @create_sync_session
    def all(order_item_id: int = None, session: Session = None) -> list[OrderItem]:
        if order_item_id:
            order_items = session.execute(
                select(OrderItem)
                .where(OrderItem.order_id == order_item_id)
                .order_by(OrderItem.id)
            )
        else:
            order_items = session.execute(
                select(OrderItem)
                .order_by(OrderItem.id)
            )
        return [order_item[0] for order_item in order_items]

    @staticmethod
    @create_sync_session
    def delete(order_item_id: int = None, session: Session = None) -> None:
        session.execute(
            delete(OrderItem)
            .where(OrderItem.id == order_item_id)
        )
        session.commit()

    @staticmethod
    @create_sync_session
    def update(order_item_id: int, order_id: int = None, session: Session = None) -> bool:
        if order_id:
            session.execute(
                update(OrderItem)
                .where(OrderItem.id == order_item_id)
                .values(
                    order_item_id=order_item_id if order_item_id else OrderItem.id
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
