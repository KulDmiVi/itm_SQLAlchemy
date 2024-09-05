"""add note column clients

Revision ID: be26ea653d6c
Revises: 
Create Date: 2024-09-05 15:01:02.072757

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'be26ea653d6c'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('client', sa.Column('note', sa.String(50)))


def downgrade() -> None:
    op.drop_column('client', 'note')
