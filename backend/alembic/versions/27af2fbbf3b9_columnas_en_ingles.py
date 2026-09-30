"""columnas en ingles

Revision ID: 27af2fbbf3b9
Revises: a5111ffa4082
Create Date: 2026-09-30 17:23:28.367035

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '27af2fbbf3b9'
down_revision: Union[str, Sequence[str], None] = 'a5111ffa4082'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Rename columns to English and adjust the schema."""
    op.alter_column(
        'plants',
        'nombre_comun',
        new_column_name='common_name',
        existing_type=sa.String(length=120),
    )
    op.alter_column(
        'plants',
        'common_name',
        existing_type=sa.String(length=120),
        nullable=True,
    )
    op.alter_column(
        'plants',
        'especie_cientifica',
        new_column_name='scientific_name',
        existing_type=sa.String(length=160),
    )
    op.drop_column('plants', 'descripcion')
    op.add_column('plants', sa.Column('origin', sa.String(length=120), nullable=True))
    op.add_column('plants', sa.Column('height', sa.Float(), nullable=True))


def downgrade() -> None:
    """Revert columns to the previous Spanish names."""
    op.drop_column('plants', 'height')
    op.drop_column('plants', 'origin')
    op.add_column('plants', sa.Column('descripcion', sa.Text(), nullable=True))
    op.alter_column(
        'plants',
        'scientific_name',
        new_column_name='especie_cientifica',
        existing_type=sa.String(length=160),
    )
    op.alter_column(
        'plants',
        'common_name',
        new_column_name='nombre_comun',
        existing_type=sa.String(length=120),
    )
    op.alter_column(
        'plants',
        'nombre_comun',
        existing_type=sa.String(length=120),
        nullable=False,
    )
