from typing import Optional, List, Tuple

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, delete
from sqlalchemy.exc import IntegrityError

from models import Category, Product, create_async_session


class CRUDCategory:

    @staticmethod
    @create_async_session
    async def add(
            name: str,
            parent_id: int = None,
            session: AsyncSession = None
    ) -> Optional[Category]:
        category = Category(
            name=name,
            parent_id=parent_id
        )
        session.add(category)
        try:
            await session.commit()
        except IntegrityError:
            pass
        else:
            await session.refresh(category)
            return category

    @staticmethod
    @create_async_session
    async def get(category_id: int, session: AsyncSession = None) -> Optional[Category]:
        category = await session.execute(
            select(Category).where(Category.id == category_id)
        )
        category = category.first()
        if category:
            return category[0]

    @staticmethod
    @create_async_session
    async def all(parent_id: int = None, session: AsyncSession = None) -> List[Category]:
        if parent_id:
            categories = await session.execute(
                select(Category)
                .where(Category.parent_id == parent_id)
                .order_by(Category.id)
            )
        else:
            categories = await session.execute(
                select(Category)
                .order_by(Category.id)
            )
        return [category[0] for category in categories]

    @staticmethod
    @create_async_session
    async def delete(category_id: int, session: AsyncSession = None) -> None:
        await session.execute(
            delete(Category)
            .where(Category.id == category_id)
        )
        await session.commit()

    @staticmethod
    @create_async_session
    async def update(
            category_id: int,
            name: str = None,
            parent_id: int = None,
            session: AsyncSession = None
    ) -> bool:
        if name or parent_id:
            await session.execute(
                update(Category)
                .where(Category.id == category_id)
                .values(
                    name=name if name else Category.name,
                    parent_id=parent_id if parent_id else Category.parent_id
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
    async def join(
            category_id: int = None,
            session: AsyncSession = None
    ) -> List[Tuple[Category, Product]]:
        if category_id:
            response = await session.execute(
                select(Category, Product)
                .join(Product, Category.id == Product.category_id)
                .where(Category.id == category_id)
            )
        else:
            response = await session.execute(
                select(Category, Product)
                .join(Product, Category.id == Product.category_id)
            )
        return response.all()
