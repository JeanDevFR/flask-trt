"""Add Recruiter table

Revision ID: 0976f2570bcb
Revises: 6aee0c45d28a
Create Date: 2022-01-07 22:20:13.708554

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0976f2570bcb'
down_revision = '6aee0c45d28a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('recruiters',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('company', sa.String(length=50), nullable=True),
    sa.Column('address', sa.String(length=255), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('user_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('recruiters')
    # ### end Alembic commands ###
