"""create user table

Revision ID: 4abb9c203bdf
Revises: 7509435b1015
Create Date: 2025-10-28 22:59:51.013734

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from datetime import datetime, timezone


# revision identifiers, used by Alembic.
revision: str = '4abb9c203bdf'
down_revision: Union[str, Sequence[str], None] = '7509435b1015'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'user',
        sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column('email', sa.String(length=255), nullable=False),
        sa.Column('password', sa.String(length=255), nullable=False),
        sa.Column('username', sa.String(length=255), nullable=True),
        sa.Column('user_type', sa.Integer(), sa.ForeignKey('user_type.id')),
        sa.Column('created_at', sa.DateTime(), nullable=False, default=datetime.now(timezone.utc)),
        sa.Column('updated_at', sa.DateTime(), nullable=True),
    )


def downgrade() -> None:
    op.drop_table('user')
