"""empty message

Revision ID: 4dc5f344e4ab
Revises: ed28f22667dd
Create Date: 2016-12-19 14:52:13.509000

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '4dc5f344e4ab'
down_revision = 'ed28f22667dd'
branch_labels = None
depends_on = None


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('comment_snippet', 'id_snippet',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=False)
    op.alter_column('tag_snippet', 'id_snippet',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=False)
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('tag_snippet', 'id_snippet',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=True)
    op.alter_column('comment_snippet', 'id_snippet',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=True)
    ### end Alembic commands ###