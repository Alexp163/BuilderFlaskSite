"""empty message

Revision ID: dfa2cf2861d6
Revises: 
Create Date: 2023-11-20 22:13:42.122884

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dfa2cf2861d6'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('object',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name_object', sa.String(length=50), nullable=True),
    sa.Column('type_object', sa.String(length=50), nullable=True),
    sa.Column('material', sa.String(length=50), nullable=True),
    sa.Column('date_manufacture', sa.String(length=10), nullable=True),
    sa.Column('price', sa.Float(), nullable=True),
    sa.Column('location', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('service_group',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('service',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name_service', sa.String(length=100), nullable=True),
    sa.Column('department_name', sa.String(length=50), nullable=True),
    sa.Column('deadlines_implementation', sa.String(length=50), nullable=True),
    sa.Column('price', sa.Float(), nullable=True),
    sa.Column('department_contact_information', sa.Text(), nullable=True),
    sa.Column('service_group_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['service_group_id'], ['service_group.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('service')
    op.drop_table('service_group')
    op.drop_table('object')
    # ### end Alembic commands ###
