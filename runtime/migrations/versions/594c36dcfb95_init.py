"""init

Revision ID: 594c36dcfb95
Revises: dd80316b63ab
Create Date: 2022-12-26 12:10:51.727009

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '594c36dcfb95'
down_revision = 'dd80316b63ab'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('cognito_id', sa.String(), nullable=True))
    op.create_index(op.f('ix_user_cognito_id'), 'user', ['cognito_id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_user_cognito_id'), table_name='user')
    op.drop_column('user', 'cognito_id')
    # ### end Alembic commands ###
