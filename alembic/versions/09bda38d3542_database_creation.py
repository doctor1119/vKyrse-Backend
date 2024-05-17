"""DataBase creation

Revision ID: 09bda38d3542
Revises: 19a4f394a8a8
Create Date: 2024-05-17 17:01:47.242703

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '09bda38d3542'
down_revision: Union[str, None] = '19a4f394a8a8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('article',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('article_id', sa.VARCHAR(length=128), nullable=True),
    sa.Column('title', sa.VARCHAR(length=256), nullable=True),
    sa.Column('url', sa.VARCHAR(length=128), nullable=True),
    sa.Column('published_dt', sa.VARCHAR(length=128), nullable=True),
    sa.Column('meta_description', sa.VARCHAR(length=256), nullable=True),
    sa.Column('currency_curs', sa.FLOAT(), nullable=True),
    sa.Column('text', sa.String(), nullable=True),
    sa.Column('tags', sa.VARCHAR(length=256), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('article')
    # ### end Alembic commands ###
