from asyncio import current_task
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, async_scoped_session, AsyncSession
from .config import db_settings


class DataBase:

    def __init__(self):
        self.engine = create_async_engine(
            url=db_settings.dsn,
            echo=db_settings.echo
        )
        self.session_factory = async_sessionmaker(
            bind=self.engine,
            autoflush=db_settings.autoflush,
            autocommit=db_settings.autocommit,
            expire_on_commit=db_settings.expire_on_commit
        )

    def get_scoped_session(self):
        session = async_scoped_session(
            session_factory=self.session_factory,
            scopefunc=current_task
        )
        return session

    async def session_dependency(self) -> AsyncSession:
        session = self.get_scoped_session()
        yield session
        await session.close()


database = DataBase()
