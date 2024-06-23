"""empty message

Revision ID: 842b14a253da
Revises: 94f3bd121d15
Create Date: 2023-11-12 03:00:37.868757

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '842b14a253da'
down_revision = '94f3bd121d15'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('tag', schema=None) as batch_op:
        batch_op.add_column(sa.Column('created', sa.DateTime(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('tag', schema=None) as batch_op:
        batch_op.drop_column('created')

    # ### end Alembic commands ###