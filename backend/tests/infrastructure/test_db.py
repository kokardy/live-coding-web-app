from app.infrastructure.db import get_sessionmaker
from sqlalchemy import text


class TestDB:
    def test_session(self) -> None:
        session_opener = get_sessionmaker()

        with session_opener() as session:
            session.execute(text("select 1;"))
