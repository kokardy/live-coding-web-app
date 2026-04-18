from sqlalchemy import BIGINT, Column, String

from .base import Base


class Specialty(Base):
    """診療科マスタ"""

    __tablename__ = "specialties"

    id = Column(BIGINT, primary_key=True, autoincrement=True)
    code = Column(String(10), nullable=False, unique=True)
    name = Column(String(255), nullable=False)

    def __repr__(self) -> str:
        return f"{self.code}: {self.name}"
