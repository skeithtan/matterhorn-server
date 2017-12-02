from django.db.models import (
    Model,
    ForeignKey,
    DateField,
    ManyToManyField, PositiveIntegerField, BooleanField)

from core.models import *


class Continent(Model):
    name = CharField(max_length=64, primary_key=True)

    def __str__(self):
        return self.name



class Country(Model):
    name = CharField(max_length=64, primary_key=True)
    continent = ForeignKey(Continent)

    def __str__(self):
        return f"{self.name} - {self.continent.name} "


class Institution(SoftDeletionModel):
    AGREEMENT_TYPES = (
        ('B', 'Bilateral'),
        ('M', 'Multilateral')
    )

    name = CharField(max_length=64)
    country = ForeignKey(Country)
    address = CharField(max_length=256)
    website = CharField(max_length=256)
    contact_person_name = CharField(max_length=256)
    contact_person_number = CharField(max_length=64)
    contact_person_email = CharField(max_length=256)
    agreement = CharField(max_length=2, choices=AGREEMENT_TYPES)

    def __str__(self):
        return self.name

    @property
    def moas(self):
        return self.memorandum_set.filter(category='MOA', archived_at__isnull=True).order_by('-date_effective')

    @property
    def mous(self):
        return self.memorandum_set.filter(category='MOU', archived_at__isnull=True).order_by('-date_effective')

    @property
    def latest_moa(self):
        moas = self.moas
        return moas[0] if moas.count() > 0 else None

    @property
    def latest_mou(self):
        mous = self.mous
        return mous[0] if mous.count() > 0 else None


class Linkage(Model):
    code = CharField(max_length=4, primary_key=True)
    name = CharField(max_length=64)

    def __str__(self):
        return self.name


class Memorandum(SoftDeletionModel):
    MEMORANDUM_CATEGORIES = (
        ('MOA', 'Memorandum of Agreement'),
        ('MOU', 'Memorandum of Understanding')
    )

    institution = ForeignKey(Institution)
    category = CharField(max_length=3, choices=MEMORANDUM_CATEGORIES)
    memorandum_file = CharField(max_length=512)
    date_effective = DateField()
    date_expiration = DateField(null=True)
    college_initiator = CharField(max_length=5, choices=COLLEGES, null=True)
    linkages = ManyToManyField(Linkage)

    @property
    def is_latest(self):
        return self.institution.latest_memorandum.id == self.id

    def __str__(self):
        return f"{self.institution.name} - {self.date_effective}"


class AcademicYear(Model):
    academic_year_start = PositiveIntegerField(primary_key=True)

    def __str__(self):
        return f"{self.academic_year_start} - {self.academic_year_start + 1}"


class Term(SoftDeletionModel):
    number = PositiveIntegerField()
    start_date = DateField()
    end_date = DateField()
    academic_year = ForeignKey(AcademicYear, related_name='terms')

    def __str__(self):
        return f"Term {self.number} - {self.academic_year.academic_year_start}"


class Program(SoftDeletionModel):
    linkage = ForeignKey(Linkage)
    name = CharField(max_length=64)
    academic_year = ForeignKey(AcademicYear)
    terms_available = ManyToManyField(Term)
    is_graduate = BooleanField()

    def __str__(self):
        return self.name


class OutboundProgram(SoftDeletionModel):
    program = ForeignKey(Program)
    requirement_deadline = DateField()
    institution = ForeignKey(Institution)

    def __str__(self):
        return f"{self.institution.name} - {self.program.name}"


class InboundProgram(SoftDeletionModel):
    program = ForeignKey(Program)

    def __str__(self):
        return f"{self.program.name}"


class Requirement(SoftDeletionModel):
    name = CharField(max_length=64)
    program = ForeignKey(OutboundProgram, null=True)


