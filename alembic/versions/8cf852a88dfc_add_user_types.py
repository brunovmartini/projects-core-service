"""add user types

Revision ID: 8cf852a88dfc
Revises: 4abb9c203bdf
Create Date: 2025-10-28 23:05:41.362003

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '8cf852a88dfc'
down_revision: Union[str, Sequence[str], None] = '4abb9c203bdf'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    user_type_table = sa.table(
        'user_type',
        sa.column('id', sa.Integer),
        sa.column('user_type', sa.String),
    )
    op.bulk_insert(
        user_type_table,
        [
            {'user_type': 'employee'},
            {'user_type': 'manager'},
        ]
    )


def downgrade() -> None:
    op.execute(
        sa.text("DELETE FROM user_type WHERE user_type IN ('employee', 'manager')")
    )
