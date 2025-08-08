from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey

from typing import Optional

from src.database import Base

import datetime


class Sources(Base):
    __tablename__ = 'sources'

    source_id: Mapped[int] = mapped_column(primary_key=True)

    name: Mapped[str]
    link: Mapped[str]

    created_at: Mapped[datetime.datetime]
    updated_at: Mapped[datetime.datetime]


class RawVacancies(Base):
    __tablename__ = "raw_vacancies"

    raw_vacancy_id:Mapped[int] = mapped_column(primary_key=True)

    source_id:Mapped[int] = mapped_column(ForeignKey("sources.source_id", ondelete="SET NULL"))

    link: Mapped[str]
    name: Mapped[str]
    data: Mapped[str]
    
    published_at: Mapped[Optional[datetime.datetime]]
    unpublished_at: Mapped[Optional[datetime.datetime]]

    created_at: Mapped[datetime.datetime]
    updated_at: Mapped[datetime.datetime]