"""add last columns to posts table

Revision ID: d48829fd5286
Revises: c97a5392c999
Create Date: 2024-05-05 22:13:11.335196

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd48829fd5286'
down_revision: Union[str, None] = 'c97a5392c999'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("posts", 
                  sa.Column("published", sa.Boolean(), 
                            nullable=False, server_default="TRUE")
                  )
    op.add_column("posts", 
                  sa.Column("created_at", sa.TIMESTAMP(timezone=True), 
                            nullable=False, server_default=sa.text('NOW()')
                            )
                  )
    pass


def downgrade() -> None:
    op.drop_column("posts", "published")
    op.drop_column("posts", "created_at")
    pass
