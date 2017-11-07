from django.db.models import ForeignKey, CharField, DateField, PositiveIntegerField, Model
from core.models import COLLEGES
from institutions.models import *


class Student(Model):
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

    STUDENT_CATEGORIES = (
        ('IN', 'Inbound'),
        ('OUT', 'Outbound')
    )

    category = CharField(max_length=3, choices=STUDENT_CATEGORIES)
    id_number = CharField(max_length=8, unique=True)
    college = CharField(max_length=6, choices=COLLEGES)
    family_name = CharField(max_length=64)
    first_name = CharField(max_length=64)
    middle_name = CharField(max_length=64, blank=True)
    nickname = CharField(max_length=64, blank=True)
    nationality = CharField(max_length=64, blank=True)
    home_address = CharField(max_length=256)
    phone_number = CharField(max_length=64)
    birth_date = DateField()
    sex = CharField(max_length=2, choices=GENDER_TYPES)
    emergency_contact_name = CharField(max_length=64)
    emergency_contact_relationship = CharField(max_length=32)
    emergency_contact_number = CharField(max_length=64)
    email = CharField(max_length=256)
    civil_status = CharField(max_length=2, choices=CIVIL_STATUS_TYPES)
    institution = ForeignKey(Institution, null=True)

    def __str__(self):
        return self.family_name


class ResidencyAddressHistory(Model):
    student = ForeignKey(Student)
    effective_from = DateField()
    contact_person_name = CharField(max_length=256)
    contact_person_number = CharField(max_length=64)
    address = CharField(max_length=256)
    residence = CharField(max_length=64)


class StudentProgram(Model):
    student = ForeignKey(Student)
    program_offering = ForeignKey(Program)
    total_units_enrolled = PositiveIntegerField()
    date_expected_return = DateField(null=True)
