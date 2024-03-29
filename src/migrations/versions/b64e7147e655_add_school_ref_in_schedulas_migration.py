"""add school ref in schedulas migration

Revision ID: b64e7147e655
Revises: 4df6a2c76f98
Create Date: 2023-07-24 12:50:01.894152

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b64e7147e655'
down_revision = '4df6a2c76f98'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('schedules', sa.Column('school_id', sa.Integer(), nullable=False, server_default="1"))
    op.create_foreign_key(None, 'schedules', 'schools', ['school_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'schedules', type_='foreignkey')
    op.drop_column('schedules', 'school_id')
    # ### end Alembic commands ###
