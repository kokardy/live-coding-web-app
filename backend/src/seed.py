import uuid

from sqlalchemy import create_engine
from sqlalchemy.orm import create_session

from app.infrastructure.models import (
    Department,
    InformationSource,
    Job,
    Question,
    Specialty,
    Staff,
)

DSN = "postgresql+psycopg://postgres:password@localhost/app"


def create_departments() -> list[Department]:
    return [Department(code=f"D{i + 1:03}", name=f"department{i + 1:03}") for i in range(100)]


def create_information_sources() -> list[InformationSource]:
    return [InformationSource(name=f"InfoSource{i + 1}") for i in range(10)]


def create_jobs() -> list[Job]:
    return [Job(name=f"Job{i + 1}") for i in range(10)]


def create_specialties() -> list[Specialty]:
    return [Specialty(code=f"S{i + 1:03}", name=f"Specialty{i + 1:03}") for i in range(10)]


def create_staffs() -> list[Staff]:
    return [Staff(code=f"ST{i + 1:03}", name=f"Staff{i + 1:03}") for i in range(100)]


def create_questions(
    departments: list[Department], staffs: list[Staff]
) -> list[Question]:
    questions = []
    # To ensure foreign keys exist, we'll assign the first elements
    for i in range(100):
        q = Question(
            id=uuid.uuid4(),
            title=f"Question {i + 1}",
            asker=f"Asker {i + 1}",
            asker_department=departments[i % len(departments)],
            question=f"Question body {i + 1}",
            answerer=staffs[i % len(staffs)],
            answer=f"Answer {i + 1}",
            input_staff=staffs[(i + 1) % len(staffs)],
        )
        questions.append(q)
    return questions


def main() -> None:
    engine = create_engine(DSN, echo=True)
    session = create_session(engine)

    # 1. Departments
    departments = create_departments()
    session.add_all(departments)

    # 2. Information Sources
    info_sources = create_information_sources()
    session.add_all(info_sources)

    # 3. Jobs
    jobs = create_jobs()
    session.add_all(jobs)

    # 4. Specialties
    specialties = create_specialties()
    session.add_all(specialties)

    # 5. Staffs
    staffs = create_staffs()
    session.add_all(staffs)

    # 6. Questions
    questions = create_questions(departments, staffs)
    session.add_all(questions)

    session.commit()


if __name__ == "__main__":
    main()
