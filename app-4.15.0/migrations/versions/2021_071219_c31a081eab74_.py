"""empty message

Revision ID: c31a081eab74
Revises: f3f19998b755
Create Date: 2021-07-12 19:25:44.745045

"""
import sqlalchemy_utils
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c31a081eab74'
down_revision = 'f3f19998b755'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('coupon',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('created_at', sqlalchemy_utils.types.arrow.ArrowType(), nullable=False),
    sa.Column('updated_at', sqlalchemy_utils.types.arrow.ArrowType(), nullable=True),
    sa.Column('code', sa.String(length=128), nullable=False),
    sa.Column('nb_year', sa.Integer(), server_default='1', nullable=False),
    sa.Column('used', sa.Boolean(), server_default='0', nullable=False),
    sa.Column('used_by_user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['used_by_user_id'], ['users.id'], ondelete='cascade'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('code')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('coupon')
    # ### end Alembic commands ###
