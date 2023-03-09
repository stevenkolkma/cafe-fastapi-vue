"""First revision

Revision ID: 29a20b5a01e1
Revises: 0eb78c950237
Create Date: 2023-03-09 12:23:09.305600

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '29a20b5a01e1'
down_revision = '0eb78c950237'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cafes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('address', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_cafes_address'), 'cafes', ['address'], unique=False)
    op.create_index(op.f('ix_cafes_id'), 'cafes', ['id'], unique=False)
    op.create_index(op.f('ix_cafes_name'), 'cafes', ['name'], unique=False)
    op.create_table('drinks',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('price', sa.String(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_drinks_description'), 'drinks', ['description'], unique=False)
    op.create_index(op.f('ix_drinks_id'), 'drinks', ['id'], unique=False)
    op.create_index(op.f('ix_drinks_name'), 'drinks', ['name'], unique=False)
    op.create_index(op.f('ix_drinks_price'), 'drinks', ['price'], unique=False)
    op.drop_index('ix_users_email', table_name='users')
    op.drop_index('ix_users_name', table_name='users')
    op.drop_table('users')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('email', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('name', name='users_pkey')
    )
    op.create_index('ix_users_name', 'users', ['name'], unique=False)
    op.create_index('ix_users_email', 'users', ['email'], unique=False)
    op.drop_index(op.f('ix_drinks_price'), table_name='drinks')
    op.drop_index(op.f('ix_drinks_name'), table_name='drinks')
    op.drop_index(op.f('ix_drinks_id'), table_name='drinks')
    op.drop_index(op.f('ix_drinks_description'), table_name='drinks')
    op.drop_table('drinks')
    op.drop_index(op.f('ix_cafes_name'), table_name='cafes')
    op.drop_index(op.f('ix_cafes_id'), table_name='cafes')
    op.drop_index(op.f('ix_cafes_address'), table_name='cafes')
    op.drop_table('cafes')
    # ### end Alembic commands ###
