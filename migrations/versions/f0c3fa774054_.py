"""empty message

Revision ID: f0c3fa774054
Revises: b19965451121
Create Date: 2022-01-07 13:54:11.217786

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f0c3fa774054'
down_revision = 'b19965451121'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('candidate', 'first_name',
               existing_type=sa.VARCHAR(length=50),
               nullable=True)
    op.alter_column('candidate', 'last_name',
               existing_type=sa.VARCHAR(length=50),
               nullable=True)
    op.alter_column('candidate', 'resume_file',
               existing_type=sa.VARCHAR(length=50),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('candidate', 'resume_file',
               existing_type=sa.VARCHAR(length=50),
               nullable=False)
    op.alter_column('candidate', 'last_name',
               existing_type=sa.VARCHAR(length=50),
               nullable=False)
    op.alter_column('candidate', 'first_name',
               existing_type=sa.VARCHAR(length=50),
               nullable=False)
    # ### end Alembic commands ###
