from pathlib import Path
from pydantic_settings import BaseSettings


BASE_DIR = Path(__file__).parent.parent


class SettingsDB(BaseSettings):
    dsn: str = f"sqlite+aiosqlite:///{BASE_DIR}/database.sqlite3"
    echo: bool = True
    autoflush: bool = False,
    autocommit: bool = False,
    expire_on_commit: bool = False


db_settings = SettingsDB()
