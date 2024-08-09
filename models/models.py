import datetime

from sqlalchemy import MetaData, Table, Column, Integer, String, TIMESTAMP, UUID, ForeignKey, JSON, Boolean

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
    Column("id", UUID, primary_key=True),
    Column("email", String, nullable=False),
    Column("name", String, nullable=False),
    Column("lastname", String, nullable=False),
    Column("surname", String, nullable=False),
    Column("hashed_password", String, nullable=False),
    Column("registered_at", TIMESTAMP, default=datetime.datetime.now(datetime.UTC)),
    Column("role_id", Integer, ForeignKey("role.id")),
    Column("is_active", Boolean, default=True, nullable=False),
    Column("is_superuser", Boolean, default=False, nullable=False),
    Column("is_verified", Boolean, default=False, nullable=False),
    Column("ed_organization_inn", Integer, ForeignKey("education_organisation.INN")),
)

education_organisation = Table(
    "education_organisation",
    metadata,
    Column("INN", Integer, primary_key=True),
    Column("full_name", String, nullable=False),
    Column("name", String, nullable=False),
    Column("site", String, nullable=True),
    Column("phone", String, nullable=True),
    Column("email", String, nullable=True),

)
