from graphene_django.types import DjangoObjectType
from .models import *

from graphene import (
    ObjectType,
    List,
    Field,
    Int,
    String)


class CountryType(DjangoObjectType):
    class Meta:
        model = Country


class MemorandumType(DjangoObjectType):
    linkages = List(String)

    def resolve_linkages(self, info):
        return [linkage.code for linkage in self.linkages.all()]

    class Meta:
        model = Memorandum


class InstitutionType(DjangoObjectType):
    mous = List(MemorandumType)
    moas = List(MemorandumType)
    latest_moa = Field(MemorandumType)
    latest_mou = Field(MemorandumType)

    def resolve_moas(self, info):
        return self.mous

    def resolve_moas(self, info):
        return self.moas

    def resolve_latest_moa(self, info):
        return self.latest_moa

    def resolve_latest_mou(self, info):
        return self.latest_mou

    class Meta:
        model = Institution


class LinkageType(DjangoObjectType):
    class Meta:
        model = Linkage


class ProgramType(DjangoObjectType):
    class Meta:
        model = Program


class TermType(DjangoObjectType):
    class Meta:
        model = Term


class AcademicYearType(DjangoObjectType):
    class Meta:
        model = AcademicYear


class Query(ObjectType):
    countries = List(CountryType)
    institutions = List(InstitutionType)
    memorandums = List(MemorandumType)
    programs = List(ProgramType, year=Int(), term=Int(), institution=Int())
    academic_years = List(AcademicYearType)

    institution = Field(InstitutionType, id=Int())
    memorandum = Field(MemorandumType, id=Int())
    program = Field(ProgramType, id=Int())

    def resolve_academic_years(self, info, **kwargs):
        return AcademicYear.objects.all()

    def resolve_countries(self, info, **kwargs):
        return [country for country in Country.objects.all() if country.institution_set.count() > 0]

    def resolve_institutions(self, info, **kwargs):
        return Institution.objects.all()

    def resolve_memorandums(self, info, **kwargs):
        return Memorandum.objects.all()

    def resolve_memorandum(self, info, **kwargs):
        id = kwargs.get('id')
        return Memorandum.objects.get(pk=id)

    def resolve_institution(self, info, **kwargs):
        id = kwargs.get('id')
        return Institution.objects.get(pk=id)

    def resolve_programs(self, info, **kwargs):
        year = kwargs.get('year')
        term = kwargs.get('term')
        institution = kwargs.get('institution')

        programs = Program.objects.all()

        if institution:
            programs = programs.filter(memorandum__institution_id=institution)

        if year:
            programs = programs.filter(academic_year__academic_year_start=year)

        if term:
            programs.filter(terms__number=term)

        return programs

    def resolve_program(self, info, **kwargs):
        id = kwargs.get('id')
        return Program.objects.get(pk=id)
