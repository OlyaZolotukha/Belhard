from typing import Optional, List, Tuple

from sqlalchemy.orm import Session
from sqlalchemy import select, update, delete
from sqlalchemy.exc import IntegrityError

from models import User, Order, create_sync_session


class CRUDUser:
    @staticmethod
    @create_sync_session
    def add(name: str, email: str, session: Session = None) -> Optional[User]:
        user = User(
            name=name,
            email=email
        )
        session.add(user)
        try:
            session.commit()
        except IntegrityError:
            pass
        else:
            session.refresh(user)
            return user

    @staticmethod
    @create_sync_session
    def get(user_id: int, session: Session = None) -> Optional[User]:
        user = session.execute(select(User).where(User.id == user_id))
        user = user.first()
        if user:
            return user[0]

    @staticmethod
    @create_sync_session
    def all(name: str = None, session: Session = None) -> List[User]:
        if name:
            users = session.execute(
                select(User)
                .where(User.name == name)
                .order_by(User.id)
            )
        else:
            users = session.execute(
                select(User)
                .order_by(User.id)
            )
        return [user[0] for user in users]

    @staticmethod
    @create_sync_session
    def delete(user_id: int = None, session: Session = None) -> None:
        session.execute(
            delete(User)
            .where(User.id == user_id)
        )
        session.commit()

    @staticmethod
    @create_sync_session
    def update(user_id: int, name: str = None, email: str = None, session: Session = None) -> bool:
        if name or email:
            session.execute(
                update(User)
                .where(User.id == user_id)
                .values(
                    name=name if name else User.name,
                    email=email if email else User.email
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
    def join(user_id: int = None, session: Session = None) -> List[Tuple[User, Order]]:
        if user_id:
            response = session.execute(
                select(User, Order)
                .join(Order, User.id == Order.user_id)
                .where(User.id == user_id)
            )
        else:
            response = session.execute(
                select(User, Order)
                .join(Order, User.id == Order.user_id)
            )
        return response.all()
