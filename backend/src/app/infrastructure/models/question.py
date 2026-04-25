from sqlalchemy import BIGINT, TEXT, UUID, Column, ForeignKey, String, Table, func
from sqlalchemy.orm import relationship

from .base import Base


class Question(Base):
    __tablename__ = "question"

    id = Column(UUID, primary_key=True)
    title = Column(String(255), nullable=False)

    asker_id = Column(ForeignKey("staff.id"), nullable=True)
    asker = relationship("Staff", backref="questions", foreign_keys=[asker_id])

    asker_department_id = Column(ForeignKey("department.id"), nullable=True)
    asker_department = relationship("Department", backref="questions")

    answerer_id = Column(ForeignKey("staff.id"), nullable=True)
    answerer = relationship(
        "Staff", backref="answered_questions", foreign_keys=[answerer_id]
    )

    question = Column(TEXT, nullable=False, default="")
    answer = Column(TEXT, nullable=False, default="")

    input_staff_id = Column(ForeignKey("staff.id"), nullable=False)
    input_staff = relationship(
        "Staff", backref="input_questions", foreign_keys=[input_staff_id]
    )
    created_at = Column(String(255), nullable=False, default=func.now())

    def __repr__(self) -> str:
        return f"Q({self.title} answered by: {self.answerer.name})"


class Tag(Base):
    __tablename__ = "tag"

    id = Column(BIGINT, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)

    def __repr__(self) -> str:
        return f"{self.name}"


QuestionTags = Table(
    "question_tags",
    Base.metadata,
    Column("question_id", ForeignKey("question.id"), primary_key=True),
    Column("tag_id", ForeignKey("tag.id"), primary_key=True),
)
