from sqlalchemy import BIGINT, UUID, Column, ForeignKey, String, Table, Text, TIMESTAMP, func
from sqlalchemy.orm import relationship

from .base import Base


class Tag(Base):
    """分類タグ"""

    __tablename__ = "tags"

    id = Column(BIGINT, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False, unique=True)

    def __repr__(self) -> str:
        return f"{self.name}"


class Question(Base):
    __tablename__ = "questions"

    id = Column(UUID, primary_key=True)
    title = Column(String(255), nullable=False)

    asker = Column(String(255), nullable=False)
    asker_department_id = Column(BIGINT, ForeignKey("departments.id"), nullable=True)
    asker_department = relationship("Department", backref="questions")
    question = Column(Text, nullable=False, default="")

    answerer_id = Column(BIGINT, ForeignKey("staffs.id"), nullable=True)
    answerer = relationship(
        "Staff", backref="answered_questions", foreign_keys=[answerer_id]
    )
    answer = Column(Text, nullable=False, default="")

    tags = relationship("Tag", secondary="question_tags", backref="questions")

    input_staff_id = Column(BIGINT, ForeignKey("staffs.id"), nullable=False)
    input_staff = relationship(
        "Staff", foreign_keys=[input_staff_id], backref="input_questions"
    )

    created_at = Column(TIMESTAMP, nullable=False, server_default=func.now())


    def __repr__(self) -> str:
        return f"Q:{self.title}"


Table(
    "question_tags",
    Base.metadata,
    Column("question_id", UUID, ForeignKey("questions.id"), primary_key=True),
    Column("tag_id", BIGINT, ForeignKey("tags.id"), primary_key=True),
)
