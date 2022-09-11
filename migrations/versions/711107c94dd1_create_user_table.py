"""create user table

Revision ID: 711107c94dd1
Revises: 
Create Date: 2022-09-11 18:19:21.175011

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '711107c94dd1'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
        op.create_table(
        'user',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('email', sa.String(50), nullable=False),
        sa.Column('password', sa.String(50), nullable=False),
        sa.Column('is_active', sa.Boolean),
        sa.Column('is_superuser', sa.Boolean),
        sa.Column('activation_code', sa.String(100), nullable=True),
    )


def downgrade() -> None:
    pass
