"""newrelationshipUserid_added

Revision ID: 0c09c032ad54
Revises: 2b7cf4be2e5a
Create Date: 2023-11-20 11:30:05.660244

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0c09c032ad54'
down_revision = '2b7cf4be2e5a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('post', schema=None) as batch_op:
        batch_op.drop_constraint('fk_post_user_id', type_='foreignkey')
        batch_op.create_foreign_key('userid', 'user', ['user_id'], ['userid'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('post', schema=None) as batch_op:
        batch_op.drop_constraint('userid', type_='foreignkey')
        batch_op.create_foreign_key('fk_post_user_id', 'user', ['user_id'], ['id'])

    # ### end Alembic commands ###