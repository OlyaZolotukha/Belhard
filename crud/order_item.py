from typing import Optional

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, delete
from sqlalchemy.exc import IntegrityError

from models import OrderItem, create_async_session


class CRUDOrderItem:
    @staticmethod
    @create_async_session
    async def add(order_id: int, product_article: int, session: AsyncSession = None) -> Optional[OrderItem]:
        order_item = OrderItem(
            order_id=order_id,
            product_article=product_article
        )
        session.add(order_id)
        try:
            await session.commit()
        except IntegrityError:
            pass
        else:
            await session.refresh(order_id)
            return order_item

    @staticmethod
    @create_async_session
    async def get(order_item_id: int, session: AsyncSession = None) -> Optional[OrderItem]:
        order_item_id = await session.execute(
            select(OrderItem).where(OrderItem.order_id == order_item_id)
        )
        order_item_id = order_item_id.first()
        if order_item_id:
            return order_item_id[0]

    @staticmethod
    @create_async_session
    async def all(order_item_id: int = None, session: AsyncSession = None) -> list[OrderItem]:
        if order_item_id:
            order_items = await session.execute(
                select(OrderItem)
                .where(OrderItem.order_id == order_item_id)
                .order_by(OrderItem.id)
            )
        else:
            order_items = await session.execute(
                select(OrderItem)
                .order_by(OrderItem.id)
            )
        return [order_item[0] for order_item in order_items]

    @staticmethod
    @create_async_session
    async def delete(order_item_id: int = None, session: AsyncSession = None) -> None:
        await session.execute(
            delete(OrderItem)
            .where(OrderItem.id == order_item_id)
        )
        await session.commit()

    @staticmethod
    @create_async_session
    async def update(order_item_id: int, order_id: int = None, session: AsyncSession = None) -> bool:
        if order_id:
            await session.execute(
                update(OrderItem)
                .where(OrderItem.id == order_item_id)
                .values(
                    order_item_id=order_item_id if order_item_id else OrderItem.id
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
