"""Create address table

Revision ID: e5ed30b9b057
Revises: ab77840d9f24
Create Date: 2023-07-30 20:42:58.004830

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e5ed30b9b057'
down_revision = 'ab77840d9f24'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'address',
        sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
        sa.Column('address_1', sa.String(), nullable=False),
        sa.Column('address_2', sa.String(), nullable=False),
        sa.Column('city', sa.String(), nullable=False),
        sa.Column('state', sa.String(), nullable=False),
        sa.Column('country', sa.String(), nullable=False),
        sa.Column('postal_code', sa.String(), nullable=False)
    )


def downgrade() -> None:
    op.drop_column('address')
