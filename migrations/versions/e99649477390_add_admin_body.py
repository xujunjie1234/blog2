"""add admin body

Revision ID: e99649477390
Revises: ebdbc01ac758
Create Date: 2020-06-07 18:45:30.314609

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e99649477390'
down_revision = 'ebdbc01ac758'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('admin', sa.Column('body', sa.Text(), nullable=True))
    op.add_column('admin', sa.Column('html', sa.Text(), nullable=True))
    op.add_column('admin', sa.Column('timestamp', sa.DateTime(), nullable=True))
    op.create_index(op.f('ix_admin_timestamp'), 'admin', ['timestamp'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_admin_timestamp'), table_name='admin')
    op.drop_column('admin', 'timestamp')
    op.drop_column('admin', 'html')
    op.drop_column('admin', 'body')
    # ### end Alembic commands ###
