"""add blacklist table

Revision ID: 944ef8e7c4a7
Revises: 938cd55ee58e
Create Date: 2021-03-25 11:32:18.827593

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '944ef8e7c4a7'
down_revision = '938cd55ee58e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('blacklist_tokens',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('token', sa.String(length=500), nullable=False),
    sa.Column('blacklisted_on', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('token')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('blacklist_tokens')
    # ### end Alembic commands ###
