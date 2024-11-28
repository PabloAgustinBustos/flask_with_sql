"""empty message

Revision ID: a16650e016ce
Revises: 34765d6575fd
Create Date: 2024-11-28 13:40:45.101134

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a16650e016ce'
down_revision = '34765d6575fd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.alter_column('password',
               existing_type=sa.VARCHAR(length=15),
               type_=sa.String(length=60),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.alter_column('password',
               existing_type=sa.String(length=60),
               type_=sa.VARCHAR(length=15),
               existing_nullable=False)

    # ### end Alembic commands ###
