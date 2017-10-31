from graphene import AbstractType, List
from graphene_django.types import DjangoObjectType
from .models import *


class CountryType(DjangoObjectType):
    class Meta:
        model = Country

class InstitutionType(DjangoObjectType):
    class Meta:
        model = Institution


class Query(AbstractType):
    countries = List(CountryType)
    institutions = List(InstitutionType)

    def resolve_countries(self, info, **kwargs):
        return [country for country in Country.objects.all() if country.institution_set.count() > 0]

    def resolve_institutions(self, info, **kwargs):
        return Institution.objects.all()
