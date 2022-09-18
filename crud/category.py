from typing import Optional, List, Tuple

from sqlalchemy.orm import Session
from sqlalchemy import select, update, delete
from sqlalchemy.exc import IntegrityError

from models import Category, Product, create_sync_session


class CRUDCategory:

    @staticmethod
    @create_sync_session
    def add(
            name: str,
            parent_id: int = None,
            session: Session = None
    ) -> Optional[Category]:
        category = Category(
            name=name,
            parent_id=parent_id
        )
        session.add(category)
        try:
            session.commit()
        except IntegrityError:
            pass
        else:
            session.refresh(category)
            return category

    @staticmethod
    @create_sync_session
    def get(category_id: int, session: Session = None) -> Optional[Category]:
        category = session.execute(
            select(Category).where(Category.id == category_id)
        )
        category = category.first()
        if category:
            return category[0]

    @staticmethod
    @create_sync_session
    def all(parent_id: int = None, session: Session = None) -> List[Category]:
        if parent_id:
            categories = session.execute(
                select(Category)
                .where(Category.parent_id == parent_id)
                .order_by(Category.id)
            )
        else:
            categories = session.execute(
                select(Category)
                .order_by(Category.id)
            )
        return [category[0] for category in categories]

    @staticmethod
    @create_sync_session
    def delete(category_id: int, session: Session = None) -> None:
        session.execute(
            delete(Category)
            .where(Category.id == category_id)
        )
        session.commit()

    @staticmethod
    @create_sync_session
    def update(
            category_id: int,
            name: str = None,
            parent_id: int = None,
            session: Session = None
    ) -> bool:
        if name or parent_id:
            session.execute(
                update(Category)
                .where(Category.id == category_id)
                .values(
                    name=name if name else Category.name,
                    parent_id=parent_id if parent_id else Category.parent_id
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
    def join(
            category_id: int = None,
            session: Session = None
    ) -> List[Tuple[Category, Product]]:
        if category_id:
            response = session.execute(
                select(Category, Product)
                .join(Product, Category.id == Product.category_id)
                .where(Category.id == category_id)
            )
        else:
            response = session.execute(
                select(Category, Product)
                .join(Product, Category.id == Product.category_id)
            )
        return response.all()
