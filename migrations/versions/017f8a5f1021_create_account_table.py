"""create account table

Revision ID: 017f8a5f1021
Revises: 
Create Date: 2022-09-11 17:50:30.723307

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '017f8a5f1021'
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
