"""created db

Revision ID: 71eea195f799
Revises: 
Create Date: 2024-02-06 20:34:02.543730

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '71eea195f799'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('doctors',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('departmentID', sa.Integer(), nullable=True),
    sa.Column('schedule', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('patients',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('gender', sa.String(), nullable=True),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('medical_history', sa.String(), nullable=True),
    sa.Column('address', sa.String(), nullable=True),
    sa.Column('phone', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('appointments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('patients_id', sa.Integer(), nullable=True),
    sa.Column('doctors_id', sa.Integer(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['doctors_id'], ['doctors.id'], name=op.f('fk_appointments_doctors_id_doctors')),
    sa.ForeignKeyConstraint(['patients_id'], ['patients.id'], name=op.f('fk_appointments_patients_id_patients')),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('treatments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('appointment_id', sa.Integer(), nullable=True),
    sa.Column('doctors_id', sa.Integer(), nullable=True),
    sa.Column('patients_id', sa.Integer(), nullable=True),
    sa.Column('diagnosis', sa.String(), nullable=True),
    sa.Column('prescription', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['appointment_id'], ['appointments.id'], name=op.f('fk_treatments_appointment_id_appointments')),
    sa.ForeignKeyConstraint(['doctors_id'], ['doctors.id'], name=op.f('fk_treatments_doctors_id_doctors')),
    sa.ForeignKeyConstraint(['patients_id'], ['patients.id'], name=op.f('fk_treatments_patients_id_patients')),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('treatments')
    op.drop_table('appointments')
    op.drop_table('patients')
    op.drop_table('doctors')
    # ### end Alembic commands ###
