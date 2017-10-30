from django.db import models

# Create your models here.
from django.db.models import (
    Model,
    CASCADE,
    CharField,
    ForeignKey,
    DateTimeField,
    PositiveIntegerField,
)

class Country(Model):
    name = CharField(max_length=64,null=False)
    continent = CharField(max_length=64, null=False)

class Continent(Model):
    name = CharField(max_length=64,null=False)

    def __str__(self):
        return f"Continent {self.name} "