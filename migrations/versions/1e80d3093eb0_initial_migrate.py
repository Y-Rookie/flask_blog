"""initial migrate

Revision ID: 1e80d3093eb0
Revises: None
Create Date: 2016-04-07 16:02:43.274189

"""

# revision identifiers, used by Alembic.
revision = '1e80d3093eb0'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('confirmed', sa.Boolean(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'confirmed')
    ### end Alembic commands ###
