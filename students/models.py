from django.db.models import ForeignKey, CharField, DateField, EmailField, PositiveIntegerField
from core.models import COLLEGES
from programs.models import Program

# Create your models here.



class Student:
    GENDER_TYPES = (
        ('F', 'Female'),
        ('M', 'Male')
    )

    CIVIL_STATUS_TYPES = (
        ('S', 'Single'),
        ('M', 'Married'),
        ('D', 'Divorced'),
        ('W', 'Widowed')
    )

    STUDENT_TYPE = (
        ('IN', 'Inbound'),
        ('OUT', 'Outbound')
    )

    type =  CharField(max_length=4, choices=STUDENT_TYPE)
    id_number = CharField(max_length=8)
    college = CharField(max_length=5, choices=COLLEGES)
    family_name = CharField(max_length=64)
    first_name = CharField(max_length=64)
    middle_name = CharField(max_length=64, null=True)
    nickname = CharField(max_length=64, null=True)
    nationality = CharField(max_length=64, null=True)
    home_address = CharField(max_length=256)
    phone_number = CharField(max_length=64)
    birth_date = DateField()
    gender = CharField(max_length=2, choices=GENDER_TYPES)
    emergency_contact_name = CharField(max_length=64)
    emergency_contact_relationship = CharField(max_length=32)
    emergency_contact_number = CharField(max_length=64)
    email = EmailField(max_length=256)
    civil_status = CharField(max_length=2, choices=CIVIL_STATUS_TYPES)

class ResidencyAddressHistory:
    student = ForeignKey(Student)
    effective_from = DateField()
    contact_person_name = CharField(max_length=256)
    contact_person_number = CharField(max_length=64)
    address = CharField(max_length=256)
    residence_type = CharField(max_length=64)

class StudentProgram:
    student = ForeignKey(Student)
    program = ForeignKey(Program)
    total_units_enrolled = PositiveIntegerField()
    date_expected_return = DateField()
