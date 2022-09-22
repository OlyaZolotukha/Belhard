from typing import Optional, List, Tuple

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, delete
from sqlalchemy.exc import IntegrityError

from models import Order, OrderItem, create_async_session


class CRUDOrder:
    @staticmethod
    @create_async_session
    async def add(user_id: int, is_paid: bool, session: AsyncSession = None) -> Optional[Order]:
        order = Order(
            user_id=user_id,
            is_paid=is_paid
        )
        session.add(order)
        try:
            await session.commit()
        except IntegrityError:
            pass
        else:
            await session.refresh(order)
            return order

    @staticmethod
    @create_async_session
    async def get(order_id: int, session: AsyncSession = None) -> Optional[Order]:
        order = await session.execute(
            select(Order).where(Order.id == order_id)
        )
        order = order.first()
        if order:
            return order[0]

    @staticmethod
    @create_async_session
    async def all(user_id: int = None, session: AsyncSession = None) -> List[Order]:
        if user_id:
            orders = await session.execute(
                select(Order)
                .where(Order.user_id == user_id)
                .order_by(Order.data_created)
            )
        else:
            orders = await session.execute(
                select(Order)
                .order_by(Order.data_created)
            )
        return [order[0] for order in orders]

    @staticmethod
    @create_async_session
    async def delete(order_id: int, session: AsyncSession = None) -> None:
        await session.execute(
            delete(Order)
            .where(Order.id == order_id)
        )
        await session.commit()

    @staticmethod
    @create_async_session
    async def update(order_id: int, is_paid: bool, session: AsyncSession = None) -> bool:
        if is_paid:
            await session.execute(
                update(Order)
                .where(Order.id == order_id)
                . values(
                    is_paid=is_paid if is_paid else Order.is_paid
                )
            )
            try:
                await session.commit()
            except IntegrityError:
                return False
            else:
                return True
        else:
            return False

    @staticmethod
    @create_async_session
    async def join(order_id: int = None, session: AsyncSession = None) -> List[Tuple[Order, OrderItem]]:
        if order_id:
            response = await session.execute(
                select(Order, OrderItem)
                .join(OrderItem, Order.id == OrderItem.order_id)
                .where(Order.id == order_id)
            )
        else:
            response = await session.execute(
                select(Order, OrderItem)
                .join(OrderItem, Order.id == OrderItem.order_id)
            )
        return response.all()
