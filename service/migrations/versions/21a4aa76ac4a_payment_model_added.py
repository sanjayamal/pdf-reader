"""payment model added

Revision ID: 21a4aa76ac4a
Revises: 084204e6475d
Create Date: 2023-09-03 17:06:49.246343

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '21a4aa76ac4a'
down_revision = '084204e6475d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('feature',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('display_name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('plan',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('price', sa.Float(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('plan_feature',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('plan_id', sa.String(), nullable=True),
    sa.Column('feature_id', sa.String(), nullable=True),
    sa.Column('limit', sa.Float(), nullable=False),
    sa.Column('is_enabled', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['feature_id'], ['feature.id'], ),
    sa.ForeignKeyConstraint(['plan_id'], ['plan.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user_subscription',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('user_id', sa.String(), nullable=True),
    sa.Column('plan_id', sa.String(), nullable=True),
    sa.Column('start_date', sa.DateTime(), nullable=False),
    sa.Column('end_date', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['plan_id'], ['plan.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_subscription')
    op.drop_table('plan_feature')
    op.drop_table('plan')
    op.drop_table('feature')
    # ### end Alembic commands ###
