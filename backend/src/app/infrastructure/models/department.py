from sqlalchemy import BIGINT, Column, String

from .base import Base


class Department(Base):
    """
    部署

    病棟名、外来名、検査部門など
    """

    __tablename__ = "department"

    id = Column(BIGINT, primary_key=True, autoincrement=True)
    code = Column(String(8), nullable=False, unique=True)
    name = Column(String(255), nullable=False)

    def __repr__(self) -> str:
        return f"{self.code}:{self.name}"
