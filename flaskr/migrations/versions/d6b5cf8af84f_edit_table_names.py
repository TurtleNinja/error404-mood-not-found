"""edit table names

Revision ID: d6b5cf8af84f
Revises: 58b8488ad67e
Create Date: 2021-01-10 21:14:24.738246

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'd6b5cf8af84f'
down_revision = '58b8488ad67e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=64), nullable=False),
    sa.Column('email', sa.String(length=128), nullable=False),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_index(op.f('ix_Users_username'), 'Users', ['username'], unique=True)
    op.create_table('Entries',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date', sa.DateTime(), nullable=False),
    sa.Column('author_id', sa.Integer(), nullable=False),
    sa.Column('mood_rate', sa.Integer(), nullable=False),
    sa.Column('title', sa.Text(), nullable=True),
    sa.Column('journal', sa.Text(), nullable=True),
    sa.ForeignKeyConstraint(['author_id'], ['Users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_index('ix_user_username', table_name='user')
    op.drop_table('entry')
    op.drop_table('user')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('entry',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('date', postgresql.TIMESTAMP(), autoincrement=False, nullable=False),
    sa.Column('author_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('mood_rate', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('title', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('journal', sa.TEXT(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['author_id'], ['user.id'], name='entry_author_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='entry_pkey')
    )
    op.create_table('user',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('username', sa.VARCHAR(length=64), autoincrement=False, nullable=False),
    sa.Column('email', sa.VARCHAR(length=128), autoincrement=False, nullable=False),
    sa.Column('password_hash', sa.VARCHAR(length=128), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='user_pkey'),
    sa.UniqueConstraint('email', name='user_email_key')
    )
    op.create_index('ix_user_username', 'user', ['username'], unique=True)
    op.drop_table('Entries')
    op.drop_index(op.f('ix_Users_username'), table_name='Users')
    op.drop_table('Users')
    # ### end Alembic commands ###