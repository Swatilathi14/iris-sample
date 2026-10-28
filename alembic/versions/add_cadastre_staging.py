from alembic import op
import geoalchemy2
import sqlalchemy as sa

revision = "add_cadastre_staging"
down_revision = "b18ad888465f"
branch_labels = None
depends_on = None

def upgrade():
  op.execute("CREATE SCHEMA IF NOT EXISTS iris_staging")
  
  op.create_table(
    "cadastre_netherlands",
    sa.Column("source_id", sa.String(), primary_key=True),
    sa.Column("country_code", sa.String(2), nullable=False),
    sa.Columns("geometry", geoalchemy2.Geometry("MULTIPOLYGON", srid=4326), nullable=False,
    ),
    schema="iris_staging",
  )

def downgrade():
  op.drop_table("cadastre_netherlands", schema="iris_staging")