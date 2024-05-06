"""add fk to posts table

Revision ID: c97a5392c999
Revises: 90b42a37aadc
Create Date: 2024-05-05 21:34:48.778999

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c97a5392c999'
down_revision: Union[str, None] = '90b42a37aadc'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("posts", sa.Column("owner_id", sa.Integer(), nullable=False))
    op.create_foreign_key("posts_users_fk", 
                          source_table="posts", 
                          referent_table="users", 
                          local_cols=["owner_id"], 
                          remote_cols=["id"], 
                          ondelete="CASCADE"
                          )
    pass


def downgrade() -> None:
    op.drop_constraint("posts_users_fk", table_name="posts")
    op.drop_column("posts", "owner_id")
    pass
