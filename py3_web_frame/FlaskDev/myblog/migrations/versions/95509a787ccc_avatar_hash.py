"""'avatar_hash'

Revision ID: 95509a787ccc
Revises: 741647815d25
Create Date: 2018-02-05 18:00:33.881547

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '95509a787ccc'
down_revision = '741647815d25'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('avatar_hash', sa.String(length=32), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'avatar_hash')
    # ### end Alembic commands ###