"""Add users table

Revision ID: 66bf52ddd27e
Revises: 780658eb5b78
Create Date: 2018-08-09 14:25:26.551141

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '66bf52ddd27e'
down_revision = '780658eb5b78'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'user',
        sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
        sa.Column('name', sa.VARCHAR(length=256), autoincrement=False, nullable=False),
        sa.Column('email_address', sa.VARCHAR(length=256), autoincrement=False, nullable=False),
        sa.PrimaryKeyConstraint('id', name='user_pkey')
    )


def downgrade():
    op.drop_table('user')
