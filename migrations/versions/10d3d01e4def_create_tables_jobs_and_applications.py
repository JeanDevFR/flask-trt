"""Create tables jobs and applications

Revision ID: 10d3d01e4def
Revises: 0a3a19a756dc
Create Date: 2022-01-09 13:50:55.748265

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '10d3d01e4def'
down_revision = '0a3a19a756dc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('jobs',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=255), nullable=False),
    sa.Column('place', sa.String(length=50), nullable=False),
    sa.Column('description', sa.Text(), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('applications',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('job_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['job_id'], ['jobs.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('applications')
    op.drop_table('jobs')
    # ### end Alembic commands ###