"""EnableUuid

Revision ID: 014dec5bfbe8
Revises: 
Create Date: 2023-03-12 10:51:18.195022

"""

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.

revision = '014dec5bfbe8'
down_revision = None
branch_labels = None
depends_on = None

def upgrade() -> None:
  # ### commands auto generated by Alembic - please adjust! ###
  op.execute(sa.text('CREATE EXTENSION IF NOT EXISTS "uuid-ossp";'))
  # ### end Alembic commands ###

def downgrade() -> None:
  # ### commands auto generated by Alembic - please adjust! ###
  op.execute(sa.text('DROP EXTENSION IF EXISTS "uuid-ossp";'))
  # ### end Alembic commands ###
