from django.db.models import (
    Model,
    CharField,
    EmailField,
    DateField,
    ForeignKey
)

from core.models import COLLEGES


class Continent(Model):
    name = CharField(max_length=64, null=False, primary_key=True)

    def __str__(self):
        return self.name


class Country(Model):
    name = CharField(max_length=64, null=False, primary_key=True)
    continent = ForeignKey(Continent)

    def __str__(self):
        return f"{self.name} - {self.continent.name} "


class Institution(Model):
    AGREEMENT_TYPES = (
        ('B', 'Bilateral'),
        ('M', 'Multilateral')
    )

    name = CharField(max_length=64)
    country = ForeignKey(Country)
    address = CharField(max_length=256)
    website = CharField(max_length=256)
    contact_person_name = CharField(max_length=256, null=True)
    contact_person_number = CharField(max_length=64, null=True)
    contact_person_email = EmailField(max_length=256, null=True)
    agreement = CharField(max_length=2, choices=AGREEMENT_TYPES)

    def __str__(self):
        return self.name

    @property
    def latest_memorandum(self):
        return self.memorandum_set.all().order_by('-version_date')[0] if self.memorandum_set.count() > 0 else None


class Memorandum(Model):
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


class MemorandumLinkage(Model):
    LINKAGE_CATEGORIES = (
        ('S', 'Scholarship'),
        ('OI', 'OJT/Internship'),
        ('FE', 'Faculty Exchange'),
        ('SE', 'Student Exchange'),
        ('RE', 'Researcher / Expert Exchange'),
        ('SP', 'Support for Projects Exchange'),
        ('RP', 'Research and Publication'),
        ('AP', 'Academic Program'),
        ('PF', 'Project Funding'),
        ('EMPI', 'Exchange of Materials, Publications and Information'),
        ('CE', 'Cultural Exchange'),
        ('SAMC', 'Seminars and Academic Meetings / Conferences'),
        ('TAP', 'Technical or Administrative Programs'),
        ('O', 'Established Office'),
        ('ASE', 'Administrative and Staff Exchange'),
        ('EM', 'Executive Meetings')
    )

    linkage = CharField(max_length=4, choices=LINKAGE_CATEGORIES)
    memorandum = ForeignKey(Memorandum)


class Program(Model):
    memorandum_linkage = ForeignKey(MemorandumLinkage, null=True)
    name = CharField(max_length=64)

    def __str__(self):
        return self.name


class ProgramOffering(Model):
    program = ForeignKey(Program)
    start_date = DateField()
    end_date = DateField()
