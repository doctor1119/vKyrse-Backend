"""Change text column type to text

Revision ID: 3a54cde9c1ab
Revises: b4f045c6dd40
Create Date: 2024-06-11 19:37:47.563081

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3a54cde9c1ab'
down_revision: Union[str, None] = 'b4f045c6dd40'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('article', 'text',
               existing_type=sa.String(),
               type_=sa.Text(),
               existing_nullable=True)
    # ### end Alembic commands ###

def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('article', 'text',
               existing_type=sa.Text(),
               type_=sa.String(),
               existing_nullable=True)
    # ### end Alembic commands ###