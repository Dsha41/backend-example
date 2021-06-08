"""empty message

Revision ID: 88574fe20324
Revises: 9122a99b94a0
Create Date: 2021-06-08 21:32:09.076697

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '88574fe20324'
down_revision = '9122a99b94a0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('sal', sa.String(length=40), nullable=False))
    op.add_column('user', sa.Column('hashed_password', sa.String(length=240), nullable=False))
    op.drop_column('user', 'password')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('password', mysql.VARCHAR(length=80), nullable=False))
    op.drop_column('user', 'hashed_password')
    op.drop_column('user', 'sal')
    # ### end Alembic commands ###