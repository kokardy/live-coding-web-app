from sqlalchemy import BIGINT, Column, String

from .base import Base


class InformationSource(Base):
    """情報源マスタ"""

    __tablename__ = "information_sources"

    id = Column(BIGINT, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False, unique=True)

    def __repr__(self) -> str:
        return f"{self.name}"
