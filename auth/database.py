import uuid
from datetime import datetime
from typing import AsyncGenerator, TYPE_CHECKING

from fastapi import Depends
from fastapi_users.db import SQLAlchemyBaseUserTableUUID, SQLAlchemyUserDatabase
from fastapi_users_db_sqlalchemy import GUID
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.dialects.postgresql import TIMESTAMP
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase, DeclarativeMeta, declarative_base, Mapped, mapped_column

from config import DB_USER, DB_PASS, DB_HOST, DB_PORT, DB_NAME

DATABASE_URL = f"postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
# Base: DeclarativeMeta = declarative_base()

UUID_ID = uuid.UUID


class Base(DeclarativeBase):
    pass


class User(SQLAlchemyBaseUserTableUUID, Base):
    if TYPE_CHECKING:  # pragma: no cover
        id: UUID_ID
    else:
        id: Mapped[UUID_ID] = mapped_column(GUID, primary_key=True, default=uuid.uuid4)
    email = Column(String(length=1024), nullable=False)
    name = Column(String, nullable=False)
    lastname = Column(String, nullable=False)
    surname = Column(String, nullable=False)
    password = Column(String(length=1024), nullable=False)
    registered_at = Column(TIMESTAMP, default=datetime.now(datetime.UTC))
    role_id = Column(Integer, ForeignKey("role.c.id"))


engine = create_async_engine(DATABASE_URL)
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)


async def create_db_and_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session


async def get_user_db(session: AsyncSession = Depends(get_async_session)):
    yield SQLAlchemyUserDatabase(session, User)