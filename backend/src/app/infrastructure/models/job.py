from sqlalchemy import BIGINT, Column, String

from .base import Base


class Job(Base):
    """職種マスタ"""

    __tablename__ = "jobs"

    id = Column(BIGINT, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False, unique=True)

    def __repr__(self) -> str:
        return f"{self.name}"
