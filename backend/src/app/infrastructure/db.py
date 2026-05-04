from app.core.env import Environment
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Engine, create_engine

env = Environment.load()


def get_engine(
    schema="postgresql+psycopg://",
    host=env.DB_HOST,
    port=env.DB_PORT,
    user=env.DB_USER,
    password=env.DB_PASSWORD,
    name=env.DB_NAME,
    echo=False,
) -> Engine:
    dsn = f"{schema}{user}:{password}@{host}:{port}/{name}"
    return create_engine(url=dsn, echo=echo)


def get_sessionmaker(echo=False) -> sessionmaker:
    engine = get_engine(echo=echo)
    return sessionmaker(bind=engine)
