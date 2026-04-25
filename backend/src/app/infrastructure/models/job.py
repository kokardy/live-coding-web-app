from .base import Base


from sqlalchemy import Column, BIGINT, String


class Job(Base):
    """
    職種

    医師、看護師、薬剤師、検査技師など
    """

    __tablename__ = "job"

    id = Column(BIGINT, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)

    def __repr__(self) -> str:
        return f"{self.name}"
