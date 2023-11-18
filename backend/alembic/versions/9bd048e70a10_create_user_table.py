"""create user table

Revision ID: 9bd048e70a10
Revises: 
Create Date: 2023-11-19 05:47:22.099363

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9bd048e70a10'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "users",
        sa.Column("id", sa.Integer, primary_key=True, index=True),
        sa.Column("username", sa.String, unique=True, index=True),
        sa.Column("email", sa.String, unique=True, index=True),
        sa.Column("full_name", sa.String, nullable=True),
        sa.Column("hashed_password", sa.String),
        sa.Column("disabled", sa.Boolean, nullable=True)
    )


def downgrade() -> None:
    op.drop_table("users")
