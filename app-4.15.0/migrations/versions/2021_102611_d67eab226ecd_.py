"""empty message

Revision ID: d67eab226ecd
Revises: a06066e3fbeb
Create Date: 2021-10-26 11:35:13.448796

"""
import sqlalchemy_utils
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd67eab226ecd'
down_revision = 'a06066e3fbeb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('client', sa.Column('referral_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'client', 'referral', ['referral_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'client', type_='foreignkey')
    op.drop_column('client', 'referral_id')
    # ### end Alembic commands ###
