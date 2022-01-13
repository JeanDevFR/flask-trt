"""alter table jobs add column salary

Revision ID: da9f9ccde3b3
Revises: a07142aa5b6a
Create Date: 2022-01-11 16:31:08.505782

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'da9f9ccde3b3'
down_revision = 'a07142aa5b6a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('jobs', sa.Column('salary', sa.Integer(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('jobs', 'salary')
    # ### end Alembic commands ###