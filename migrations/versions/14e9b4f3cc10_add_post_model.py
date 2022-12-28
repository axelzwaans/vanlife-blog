"""Add post model

Revision ID: 14e9b4f3cc10
Revises: 6e21fdaa06f7
Create Date: 2022-12-23 08:31:48.104868

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '14e9b4f3cc10'
down_revision = '6e21fdaa06f7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('post', schema=None) as batch_op:
        batch_op.alter_column('author',
               existing_type=sa.INTEGER(),
               nullable=False)

    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('firstName',
               existing_type=sa.VARCHAR(length=1000),
               type_=sa.String(length=150),
               existing_nullable=True)
        batch_op.alter_column('lastName',
               existing_type=sa.VARCHAR(length=1000),
               type_=sa.String(length=150),
               existing_nullable=True)
        batch_op.alter_column('email',
               existing_type=sa.VARCHAR(length=1000),
               type_=sa.String(length=150),
               existing_nullable=True)
        batch_op.alter_column('password',
               existing_type=sa.VARCHAR(length=1000),
               type_=sa.String(length=150),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('password',
               existing_type=sa.String(length=150),
               type_=sa.VARCHAR(length=1000),
               existing_nullable=True)
        batch_op.alter_column('email',
               existing_type=sa.String(length=150),
               type_=sa.VARCHAR(length=1000),
               existing_nullable=True)
        batch_op.alter_column('lastName',
               existing_type=sa.String(length=150),
               type_=sa.VARCHAR(length=1000),
               existing_nullable=True)
        batch_op.alter_column('firstName',
               existing_type=sa.String(length=150),
               type_=sa.VARCHAR(length=1000),
               existing_nullable=True)

    with op.batch_alter_table('post', schema=None) as batch_op:
        batch_op.alter_column('author',
               existing_type=sa.INTEGER(),
               nullable=True)

    # ### end Alembic commands ###