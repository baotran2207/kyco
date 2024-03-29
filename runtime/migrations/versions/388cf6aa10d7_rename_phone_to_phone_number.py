"""rename phone to phone_number

Revision ID: 388cf6aa10d7
Revises: 518fbbd3f95d
Create Date: 2023-01-19 14:38:38.442530

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '388cf6aa10d7'
down_revision = '518fbbd3f95d'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('phone_number', sa.String(), nullable=True))
    op.drop_index('ix_user_phone', table_name='user')
    op.create_index(op.f('ix_user_phone_number'), 'user', ['phone_number'], unique=False)
    op.drop_column('user', 'phone')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('phone', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.drop_index(op.f('ix_user_phone_number'), table_name='user')
    op.create_index('ix_user_phone', 'user', ['phone'], unique=False)
    op.drop_column('user', 'phone_number')
    # ### end Alembic commands ###
