"""create address_id to users

Revision ID: 423d22a1204b
Revises: e5ed30b9b057
Create Date: 2023-07-30 20:59:18.985402

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '423d22a1204b'
down_revision = 'e5ed30b9b057'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('users', sa.Column('address_id', sa.Integer, nullable=True))
    op.create_foreign_key(
        'address_users_fk',
        source_table="users",
        referent_table="address",
        local_cols=['address_id'],
        remote_cols=['id'],
        ondelete="CASCADE"
    )


def downgrade() -> None:
    op.drop_constraint('address_users_fk', table_name="users")
    op.drop_column("users", 'address_id')
