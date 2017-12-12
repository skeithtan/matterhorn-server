from django.db.models import Model, BooleanField, OneToOneField
from django.db.models import Q

from core.models import *
from institutions.models import *


class Student(SoftDeletionModel):
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
    is_graduate = BooleanField(default=False)

    @property
    def full_name(self):
        return f"{self.first_name} {self.middle_name} {self.family_name}"

    @property
    def residencies(self):
        return self.residencyaddresshistory_set.filter(archived_at__isnull=True).order_by('-date_effective')

    @property
    def latest_residency(self):
        residencies = self.residencies
        return residencies[0] if residencies.count() > 0 else None

    def __str__(self):
        return self.family_name


class ResidencyAddressHistory(SoftDeletionModel):
    student = ForeignKey(Student)
    date_effective = DateField()
    contact_person_name = CharField(max_length=256)
    contact_person_number = CharField(max_length=64)
    address = CharField(max_length=256)
    residence = CharField(max_length=64)


class InboundCourse(SoftDeletionModel):
    name = CharField(max_length=64)


class InboundStudentProgram(SoftDeletionModel):
    student = OneToOneField(Student)
    terms_duration = ManyToManyField(Term)
    program = ForeignKey(InboundProgram)
    application_requirements = ManyToManyField(InboundRequirement, blank=True)

    def delete(self, using=None, keep_parents=False):
        self.student.delete()

    @staticmethod
    def accepted():
        return [accepted.student_program for accepted in AcceptedStudentProgram.objects.all()]

    @staticmethod
    def applicants():
        return [inbound for inbound in InboundStudentProgram.current.all() if
                inbound not in InboundStudentProgram.accepted() and inbound.student.archived_at is None]

    def __str__(self):
        return f"{self.student.full_name} - {self.program.program.name}"

    @property
    def is_requirements_complete(self):
        requirements = InboundRequirement.objects.all()

        for requirement in requirements:
            if requirement not in self.application_requirements.all():
                print(False)
                return False
        print(True)
        return True


class AcceptedStudentProgram(SoftDeletionModel):
    student_program = ForeignKey(InboundStudentProgram)
    total_units_enrolled = PositiveIntegerField()
    inbound_courses = ManyToManyField(InboundCourse, blank=True)


class OutboundStudentProgram(Model):
    student = OneToOneField(Student)
    terms_duration = ManyToManyField(Term)
    program = ForeignKey(OutboundProgram)
    application_requirements = ManyToManyField(OutboundRequirement, blank=True)

    def delete(self, using=None, keep_parents=False):
        self.student.delete()

    @staticmethod
    def deployed():
        return [deployed.student_program for deployed in DeployedStudentProgram.current.all()]

    @staticmethod
    def applicants():
        return [outbound for outbound in OutboundStudentProgram.objects.all() if
                outbound not in OutboundStudentProgram.deployed() and outbound.student.archived_at is None]

    def __str__(self):
        return f"{self.student.full_name} - {self.program.program.name}"

    @property
    def is_requirements_complete(self):
        requirements = OutboundRequirement.objects.all()
        print([requirement.name for requirement in requirements])
        print(self.application_requirements.all())
        for requirement in requirements:
            if requirement not in self.application_requirements.all():
                print(False)
                return False
        print(True)
        return True


class DeployedStudentProgram(SoftDeletionModel):
    student_program = ForeignKey(OutboundStudentProgram)
    default_units = PositiveIntegerField()
    date_expected_return = DateField(null=True)
    total_units_enrolled = PositiveIntegerField()

    def __str__(self):
        return f"{self.student_program.student.first_name} - {self.student_program.program.program.name}"
