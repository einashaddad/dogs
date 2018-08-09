"""Create dog table

Revision ID: 780658eb5b78
Revises:
Create Date: 2018-08-05 15:35:19.729386

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '780658eb5b78'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'dog',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(256), nullable=False),
        sa.Column('link', sa.String(256)),
        sa.Column('image', sa.String(256)),
        sa.Column('age', sa.String(256)),
        sa.Column('weight', sa.String(256)),
        sa.Column('breed', sa.String(256)),
        sa.Column('gender', sa.String(256)),
    )


def downgrade():
    op.drop_table('dog')
