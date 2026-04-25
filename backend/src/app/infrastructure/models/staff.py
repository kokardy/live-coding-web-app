from sqlalchemy import BIGINT, Column, String

from .base import Base


class Staff(Base):
    """スタッフ"""

    __tablename__ = "staff"

    id = Column(BIGINT, primary_key=True, autoincrement=True)
    code = Column(String(8), nullable=False, unique=True)
    name = Column(String(255), nullable=False)

    def __repr__(self) -> str:
        return f"{self.code}:{self.name}"
