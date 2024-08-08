import datetime

from sqlalchemy import MetaData, Table, Column, Integer, String, TIMESTAMP, UUID, ForeignKey, JSON

metadata = MetaData()

role = Table(
    "role",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable=False),
    Column("permissions", JSON),
)

user = Table(
    "user",
    metadata,
    Column("UUID", UUID, primary_key=True),
    Column("email", String, nullable=False),
    Column("name", String, nullable=False),
    Column("lastname", String, nullable=False),
    Column("surname", String, nullable=False),
    Column("password", String, nullable=False),
    Column("registered_at", TIMESTAMP, default=datetime.datetime.now(datetime.UTC)),
    Column("role_id", Integer, ForeignKey("role.id")),
)
