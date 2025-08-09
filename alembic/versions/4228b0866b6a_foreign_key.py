"""foreign key

Revision ID: 4228b0866b6a
Revises: b8e2abf39fdc
Create Date: 2025-08-08 20:56:16.946533

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4228b0866b6a'
down_revision: Union[str, Sequence[str], None] = 'b8e2abf39fdc'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
