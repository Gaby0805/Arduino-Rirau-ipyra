"""Add user_id to alarms

Revision ID: 41f5c470453e
Revises: 4228b0866b6a
Create Date: 2025-08-13 11:55:04.773025

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = '41f5c470453e'
down_revision: Union[str, Sequence[str], None] = '4228b0866b6a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # Adiciona a coluna user_id
    op.add_column('alarms', sa.Column('user_id', sa.Integer(), nullable=False))

    # Cria FK usando batch mode (necessário para SQLite)
    with op.batch_alter_table('alarms') as batch_op:
        batch_op.create_foreign_key(
            "fk_alarms_user_id",  # nome da constraint
            "user",               # tabela referenciada
            ["user_id"],          # coluna local
            ["id"],               # coluna da tabela referenciada
            ondelete="CASCADE"
        )

    # Cria índice na tabela alarms_days
    op.create_index(op.f('ix_alarms_days_alarm_id'), 'alarms_days', ['alarm_id'], unique=False)


def downgrade() -> None:
    """Downgrade schema."""
    # Remove índice
    op.drop_index(op.f('ix_alarms_days_alarm_id'), table_name='alarms_days')

    # Remove FK usando batch mode
    with op.batch_alter_table('alarms') as batch_op:
        batch_op.drop_constraint("fk_alarms_user_id", type_='foreignkey')

    # Remove coluna user_id
    op.drop_column('alarms', 'user_id')
