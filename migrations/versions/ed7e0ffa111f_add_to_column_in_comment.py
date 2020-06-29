"""add to column in comment

Revision ID: ed7e0ffa111f
Revises: 6a2412bbaf78
Create Date: 2020-05-24 11:30:27.337084

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ed7e0ffa111f'
down_revision = '6a2412bbaf78'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comment', sa.Column('to', sa.String(length=100), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('comment', 'to')
    # ### end Alembic commands ###