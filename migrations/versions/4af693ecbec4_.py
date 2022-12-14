"""empty message

Revision ID: 4af693ecbec4
Revises: e10bd8facd0e
Create Date: 2022-08-29 16:09:42.757575

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4af693ecbec4'
down_revision = 'e10bd8facd0e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('posts', sa.Column('body_html', sa.Text(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('posts', 'body_html')
    # ### end Alembic commands ###
