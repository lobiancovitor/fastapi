"""add content column to posts table

Revision ID: 0c8ff6d4c54b
Revises: 013b994e68fc
Create Date: 2024-05-05 21:17:12.548926

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0c8ff6d4c54b'
down_revision: Union[str, None] = '013b994e68fc'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("posts", 
                  sa.Column("content", sa.String(), nullable=False)
                  )
    pass


def downgrade() -> None:
    op.drop_column("posts", "content")
    pass
