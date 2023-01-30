"""rename phone to created_time

Revision ID: 947546b7842b
Revises: 388cf6aa10d7
Create Date: 2023-01-30 13:45:08.033902

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '947546b7842b'
down_revision = '388cf6aa10d7'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('depositrecords', sa.Column('created_time', sa.DateTime(timezone=True), nullable=True))
    op.drop_column('depositrecords', 'order_created_time')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('depositrecords', sa.Column('order_created_time', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=True))
    op.drop_column('depositrecords', 'created_time')
    # ### end Alembic commands ###