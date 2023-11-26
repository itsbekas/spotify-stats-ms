from sqlalchemy import Integer, String, DateTime
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import Mapped

from .base import Base


class Play(Base):
    __tablename__ = "plays"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    track: Mapped[int] = mapped_column(String)
    played_at: Mapped[str] = mapped_column(DateTime)
