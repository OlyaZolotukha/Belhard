from typing import Optional, List, Tuple

from sqlalchemy.orm import Session
from sqlalchemy import select, update, delete
from sqlalchemy.exc import IntegrityError

from models import Order, OrderItem, create_sync_session


class CRUDOrder:
    @staticmethod
    @create_sync_session
    def add(user_id: int, is_paid: bool, session: Session = None) -> Optional[Order]:
        order = Order(
            user_id=user_id,
            is_paid=is_paid
        )
        session.add(order)
        try:
            session.commit()
        except IntegrityError:
            pass
        else:
            session.refresh(order)
            return order

    @staticmethod
    @create_sync_session
    def get(order_id: int, session: Session = None) -> Optional[Order]:
        order = session.execute(
            select(Order).where(Order.id == order_id)
        )
        order = order.first()
        if order:
            return order[0]

    @staticmethod
    @create_sync_session
    def all(user_id: int = None, session: Session = None) -> List[Order]:
        if user_id:
            orders = session.execute(
                select(Order)
                .where(Order.user_id == user_id)
                .order_by(Order.data_created)
            )
        else:
            orders = session.execute(
                select(Order)
                .order_by(Order.data_created)
            )
        return [order[0] for order in orders]

    @staticmethod
    @create_sync_session
    def delete(order_id: int, session: Session = None) -> None:
        session.execute(
            delete(Order)
            .where(Order.id == order_id)
        )
        session.commit()

    @staticmethod
    @create_sync_session
    def update(order_id: int, is_paid: bool, session: Session = None) -> bool:
        if is_paid:
            session.execute(
                update(Order)
                .where(Order.id == order_id)
                . values(
                    is_paid=is_paid if is_paid else Order.is_paid
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
    def join(order_id: int = None, session: Session = None) -> List[Tuple[Order, OrderItem]]:
        if order_id:
            response = session.execute(
                select(Order, OrderItem)
                .join(OrderItem, Order.id == OrderItem.order_id)
                .where(Order.id == order_id)
            )
        else:
            response = session.execute(
                select(Order, OrderItem)
                .join(OrderItem, Order.id == OrderItem.order_id)
            )
        return response.all()
