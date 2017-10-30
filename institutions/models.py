from django.db.models import (
    Model,
    CharField,
    EmailField,
    DateField,
    ForeignKey,
)

from core.models import COLLEGES

class Continent(Model):
    name = CharField(max_length=64, null=False)

    def __str__(self):
        return self.name


class Country(Model):
    name = CharField(max_length=64, null=False)
    continent = ForeignKey(Continent)

    def __str__(self):
        return f"{self.name} - {self.continent.name} "


class Institution(Model):
    name = CharField(max_length=64)
    country = ForeignKey(Country)
    email = EmailField(max_length=256, null=True)
    address = CharField(max_length=256)
    website = CharField(max_length=256)
    contact_person_name = CharField(max_length=256, null=True)
    contact_person_number = CharField(max_length=64, null=True)

    def __str__(self):
        return self.name


class Memorandum(Model):
    MEMORANDUM_TYPES = (
        ('MOA', 'Memorandum of Agreement'),
        ('MOU', 'Memorandum of Understanding')
    )

    AGREEMENT_TYPES = (
        ('B', 'Bilateral'),
        ('M', 'Multilateral')
    )

    institution = ForeignKey(Institution)
    type = CharField(max_length=3, choices=MEMORANDUM_TYPES)
    date_effective = DateField()
    date_expiration = DateField(null=True)
    college_initiator = CharField(max_length=5, choices=COLLEGES, null=True)
    agreement_type = CharField(max_length=64, choices=AGREEMENT_TYPES)


class MemorandumVersion:
    memorandum = ForeignKey(Memorandum)
    initial_review_file =  CharField(max_length=512)
    final_revision_file = CharField(max_length=512, null=True)
    memorandum_file = CharField(max_length=512)
    version_date = DateField()

class Linkage:

    LINKAGE_TYPES = (
        ('S', 'Scholarship'),
        ('OI', 'OJT/Internship'),
        ('FE', 'Faculty Exchange'),
        ('SE','Student Exchange'),
        ('RE', 'Researcher / Expert Exchange'),
        ('SP', 'Support for Projects Exchange'),
        ('RP', 'Research and Publication'),
        ('AP', 'Academic Program'),
        ('PF', 'Project Funding'),
        ('EMPI', 'Exchange of Materials, Publications and Information'),
        ('CE', 'Cultural Exchange'),
        ('SAMC', 'Seminars and Academic Meetings / Conferences'),
        ('TAP', 'Technical or Adminstrative Programs'),
        ('O', 'Established Office'),
        ('ASE', 'Administrative and Staff Exchange'),
        ('EM', 'Executive Meetings')
    )

    memorandum = ForeignKey(Memorandum)
    type = CharField(max_length=4, choices=LINKAGE_TYPES)

