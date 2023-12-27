"""empty message

Revision ID: dfe743849802
Revises: 89bd8a261dc5
Create Date: 2023-11-27 13:22:03.229524

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dfe743849802'
down_revision = '89bd8a261dc5'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('depositrecords', sa.Column('lastchanged_at', sa.DateTime(timezone=True), nullable=True))
    op.add_column('usedtoken', sa.Column('lastchanged_at', sa.DateTime(timezone=True), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('usedtoken', 'lastchanged_at')
    op.drop_column('depositrecords', 'lastchanged_at')
    # ### end Alembic commands ###