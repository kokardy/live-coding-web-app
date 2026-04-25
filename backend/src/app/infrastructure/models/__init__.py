from .base import Base

from .staff import Staff
from .department import Department
from .job import Job
from .specialty import Specialty
from .question import Question, Tag

__all__ = [
    "Base",
    "Department",
    "Job",
    "Question",
    "Specialty",
    "Staff",
    "Tag",
]
