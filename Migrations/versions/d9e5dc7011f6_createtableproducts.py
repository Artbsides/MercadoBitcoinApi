"""CreateTableProducts

Revision ID: d9e5dc7011f6
Revises: 014dec5bfbe8
Create Date: 2023-03-12 11:36:34.209013

"""

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.

revision = 'd9e5dc7011f6'
down_revision = '014dec5bfbe8'
branch_labels = None
depends_on = None


def upgrade() -> None:
  # ### commands auto generated by Alembic - please adjust! ###
  op.create_table('Products',
  sa.Column('id', sa.Uuid(), server_default=sa.text('uuid_generate_v4()'), nullable=False),
  sa.Column('name', sa.String(), nullable=False),
  sa.PrimaryKeyConstraint('id'),
  sa.UniqueConstraint('name')
  )
  # ### end Alembic commands ###

def downgrade() -> None:
  # ### commands auto generated by Alembic - please adjust! ###
  op.drop_table('Products')
  # ### end Alembic commands ###
