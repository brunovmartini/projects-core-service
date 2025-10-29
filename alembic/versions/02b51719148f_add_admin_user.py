"""add admin user


Revision ID: 02b51719148f
Revises: 8cf852a88dfc
Create Date: 2025-10-28 23:27:45.103559

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql
from datetime import datetime, timezone

# revision identifiers, used by Alembic.
revision: str = '02b51719148f'
down_revision: Union[str, Sequence[str], None] = '8cf852a88dfc'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    user_table = sa.table(
        'user',
        sa.column('email', sa.String),
        sa.column('password', sa.String),
        sa.column('username', sa.String),
        sa.column('user_type', sa.Integer),
        sa.column('created_at', sa.DateTime),
    )

    op.bulk_insert(
        user_table,
        [
            {
                'email': 'admin@projects.com',
                'password': 'admin',
                'username': 'admin',
                'user_type': 2,
                'created_at': datetime.now(timezone.utc),
            }
        ]
    )


def downgrade() -> None:
    op.execute(
        sa.text("DELETE FROM \"user\" WHERE username = 'admin'")
    )
