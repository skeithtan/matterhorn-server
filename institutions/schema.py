from graphene_django.types import DjangoObjectType
from .models import *

from graphene import (
    AbstractType,
    List,
    Field,
    Int
)


class CountryType(DjangoObjectType):
    class Meta:
        model = Country


class InstitutionType(DjangoObjectType):
    class Meta:
        model = Institution


class Query(AbstractType):
    countries = List(CountryType)
    institutions = List(InstitutionType)

    institution = Field(InstitutionType, id=Int())

    def resolve_countries(self, info, **kwargs):
        return [country for country in Country.objects.all() if country.institution_set.count() > 0]

    def resolve_institutions(self, info, **kwargs):
        return Institution.objects.all()

    def resolve_institution(self, info, **kwargs):
        id = kwargs.get('id')
        return Institution.objects.get(pk=id)
