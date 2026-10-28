from geoalchemy2 import Geometry
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from app.database.base import Base

class Cadastre(Base):
  __tablename__ = "cadastre_netherlands"
  __table_args__= {"schema": "iris_staging"}

  source_id: Mapped[str] = mapped_column(String, primary_key=True)
  country_code: Mapped[str] = mapped_column(String(2), default="NL")
  geometry = mapped_column(Geometry("MULTIPOLYGON", srid=4326))