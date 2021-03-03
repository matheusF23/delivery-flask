"""added name to user

Revision ID: 7833067e5e8c
Revises: 
Create Date: 2021-03-03 12:20:50.785846

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7833067e5e8c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'name')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###
