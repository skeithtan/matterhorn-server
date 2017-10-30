from django.db import models

# Create your models here.
from django.db.models import ForeignKey, CharField, DateField,Model

from institutions.models import Institution


class Mobility(Model):
    linkage = ForeignKey(Institution)
    name = CharField(max_length=64)


class Program(Model):
    mobility = ForeignKey(Mobility)
    start_date = DateField()
    end_date = DateField()