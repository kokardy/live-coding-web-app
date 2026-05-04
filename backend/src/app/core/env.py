from pydantic import BaseModel
import os


class Environment(BaseModel):
    DB_USER: str
    DB_PASSWORD: str
    DB_NAME: str
    DB_HOST: str
    DB_PORT: int

    @classmethod
    def load(cls) -> Environment:
        return cls.reload()

    @classmethod
    def reload(cls) -> Environment:
        return Environment(**os.environ)  # type: ignore
