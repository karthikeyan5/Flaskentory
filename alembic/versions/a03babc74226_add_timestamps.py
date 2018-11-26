"""add timestamps

Revision ID: a03babc74226
Revises: 
Create Date: 2018-11-26 12:43:14.682188

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a03babc74226'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('product', sa.Column('time_created', sa.TIMESTAMP, server_default=sa.func.now()))
    op.add_column('product', sa.Column('time_updated', sa.TIMESTAMP, onupdate=sa.func.now()))
    op.add_column('location', sa.Column('time_created', sa.TIMESTAMP, server_default=sa.func.now()))
    op.add_column('location', sa.Column('time_updated', sa.TIMESTAMP, onupdate=sa.func.now()))


def downgrade():
    pass
