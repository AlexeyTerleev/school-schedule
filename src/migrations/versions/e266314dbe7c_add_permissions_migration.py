"""add permissions migration

Revision ID: e266314dbe7c
Revises: 33cc94c0f158
Create Date: 2023-07-28 07:59:51.119075

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e266314dbe7c'
down_revision = '33cc94c0f158'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('admins', sa.Column('permission', sa.Integer(), nullable=False))
    op.add_column('admins', sa.Column('school_id', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'admins', 'schools', ['school_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'admins', type_='foreignkey')
    op.drop_column('admins', 'school_id')
    op.drop_column('admins', 'permission')
    # ### end Alembic commands ###