from typing import Optional, List, Tuple

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, delete
from sqlalchemy.exc import IntegrityError

from models import User, Order, create_async_session


class CRUDUser:
    @staticmethod
    @create_async_session
    async def add(name: str, email: str, session: AsyncSession = None) -> Optional[User]:
        user = User(
            name=name,
            email=email
        )
        session.add(user)
        try:
            await session.commit()
        except IntegrityError:
            pass
        else:
            await session.refresh(user)
            return user

    @staticmethod
    @create_async_session
    async def get(user_id: int, session: AsyncSession = None) -> Optional[User]:
        user = await session.execute(select(User).where(User.id == user_id))
        user = user.first()
        if user:
            return user[0]

    @staticmethod
    @create_async_session
    async def all(name: str = None, session: AsyncSession = None) -> List[User]:
        if name:
            users = await session.execute(
                select(User)
                .where(User.name == name)
                .order_by(User.id)
            )
        else:
            users = await session.execute(
                select(User)
                .order_by(User.id)
            )
        return [user[0] for user in users]

    @staticmethod
    @create_async_session
    async def delete(user_id: int = None, session: AsyncSession = None) -> None:
        await session.execute(
            delete(User)
            .where(User.id == user_id)
        )
        await session.commit()

    @staticmethod
    @create_async_session
    async def update(user_id: int, name: str = None, email: str = None, session: AsyncSession = None) -> bool:
        if name or email:
            await session.execute(
                update(User)
                .where(User.id == user_id)
                .values(
                    name=name if name else User.name,
                    email=email if email else User.email
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
    async def join(user_id: int = None, session: AsyncSession = None) -> List[Tuple[User, Order]]:
        if user_id:
            response = await session.execute(
                select(User, Order)
                .join(Order, User.id == Order.user_id)
                .where(User.id == user_id)
            )
        else:
            response = await session.execute(
                select(User, Order)
                .join(Order, User.id == Order.user_id)
            )
        return response.all()
