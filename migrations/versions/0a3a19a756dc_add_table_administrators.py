"""Add table administrators

Revision ID: 0a3a19a756dc
Revises: d6e92b2cb972
Create Date: 2022-01-09 09:31:21.556816

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0a3a19a756dc'
down_revision = 'd6e92b2cb972'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('administrators',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('user_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('administrators')
    # ### end Alembic commands ###
