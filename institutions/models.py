from django.db.models import (
    Model,
    CharField,
    EmailField,
    DateField,
    ForeignKey,
    ManyToManyField, PositiveIntegerField)

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
    contact_person_name = CharField(max_length=256, blank=True)
    contact_person_number = CharField(max_length=64, blank=True)
    contact_person_email = CharField(max_length=256, blank=True)
    agreement = CharField(max_length=2, choices=AGREEMENT_TYPES)

    def __str__(self):
        return self.name

    @property
    def latest_memorandum(self):
        return self.memorandum_set.all().order_by('-version_date')[0] if self.memorandum_set.count() > 0 else None


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

    def __str__(self):
        return f"{self.institution.name} - {self.date_effective}"


class Term(SoftDeletionModel):
    number = PositiveIntegerField(primary_key=True)
    name = CharField(max_length=8)

    def __str__(self):
        return self.name


class AcademicYear(Model):
    academic_year_start = PositiveIntegerField(primary_key=True)

    def __str__(self):
        return f"{self.academic_year_start} - {self.academic_year_start + 1}"


class Program(SoftDeletionModel):
    memorandum = ForeignKey(Memorandum)
    linkage = ForeignKey(Linkage)
    name = CharField(max_length=64)
    academic_year = ForeignKey(AcademicYear)
    terms = ManyToManyField(Term)

    def __str__(self):
        return self.name


class StudyField(SoftDeletionModel):
    name = CharField(max_length=64)
    program = ForeignKey(Program)
    terms = ManyToManyField(Term)

    def __str__(self):
        return f"{self.program} - {self.name}"
