from app.infrastructure.models import Staff, Job, Department, Specialty, Tag

from collections.abc import Iterable
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DSN = "postgresql+psycopg://postgres:password@localhost:5432/app"


def seed_staff() -> Iterable[Staff]:
    return (
        Staff(
            id=i,
            code=f"STAFF{i:03d}",
            name=f"Staff {i}",
        )
        for i in range(1, 100)
    )


def seed_job() -> Iterable[Job]:
    return [Job(id=i, name=f"Job {i}") for i in range(1, 10)]


def seed_department() -> Iterable[Department]:
    return (
        Department(
            id=i,
            code=f"Dep{i:03d}",
            name=f"Department {i}",
        )
        for i in range(1, 10)
    )


def seed_specialty() -> Iterable[Specialty]:
    return (
        Specialty(
            id=i,
            code=f"Sp{i:03d}",
            name=f"Specialty {i}",
        )
        for i in range(1, 10)
    )


def seed_tag() -> Iterable[Tag]:
    return (
        Tag(
            id=i,
            name=f"Tag {i}",
        )
        for i in range(1, 10)
    )


def main() -> None:
    engine = create_engine(DSN)
    Session = sessionmaker(bind=engine)
    session = Session()

    staff_list = seed_staff()
    job_list = seed_job()
    department_list = seed_department()
    specialty_list = seed_specialty()
    tag_list = seed_tag()

    session.add_all(staff_list)
    session.add_all(job_list)
    session.add_all(department_list)
    session.add_all(specialty_list)
    session.add_all(tag_list)

    session.commit()


if __name__ == "__main__":
    main()
