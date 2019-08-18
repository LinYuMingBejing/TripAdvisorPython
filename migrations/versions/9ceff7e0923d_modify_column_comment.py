"""modify column comment 

Revision ID: 9ceff7e0923d
Revises: c49901cfeec3
Create Date: 2019-08-12 16:12:53.639052

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '9ceff7e0923d'
down_revision = 'c49901cfeec3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('hotel', sa.Column('comment1', sa.Text(), nullable=True))
    op.drop_column('hotel', 'comment')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('hotel', sa.Column('comment', mysql.VARCHAR(length=1024), nullable=True))
    op.drop_column('hotel', 'comment1')
    # ### end Alembic commands ###
