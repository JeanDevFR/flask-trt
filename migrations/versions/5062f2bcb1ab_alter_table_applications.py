"""alter table applications

Revision ID: 5062f2bcb1ab
Revises: da9f9ccde3b3
Create Date: 2022-01-11 22:06:26.322334

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5062f2bcb1ab'
down_revision = 'da9f9ccde3b3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('applications', 'job_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('applications', 'user_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.drop_column('applications', 'id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('applications', sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False))
    op.alter_column('applications', 'user_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('applications', 'job_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###
