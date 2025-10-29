"""create user_type table

Revision ID: 7509435b1015
Revises: 
Create Date: 2025-10-28 22:59:00.733707

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7509435b1015'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'user_type',
        sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column('user_type', sa.String(length=8), nullable=False)
    )


def downgrade() -> None:
    op.drop_table('user_type')
