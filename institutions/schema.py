from graphene_django.types import DjangoObjectType
from .models import *
from graphene import (
    ObjectType,
    List,
    Field,
    Int,
    String, Boolean)


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
    country = String()

    def resolve_country(self, info):
        return self.country.name

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


class CountryType(DjangoObjectType):
    institutions = List(InstitutionType)

    def resolve_institutions(self, info):
        return self.institution_set.filter(archived_at__isnull=True)

    class Meta:
        model = Country


class LinkageType(DjangoObjectType):
    class Meta:
        model = Linkage


class TermType(DjangoObjectType):
    class Meta:
        model = Term


class AcademicYearType(DjangoObjectType):
    class Meta:
        model = AcademicYear


class Program:
    linkage = Field(LinkageType)
    name = String()
    academic_year = Field(AcademicYearType)
    terms_available = List(TermType)
    is_graduate = Boolean()

    def resolve_linkage(self, info):
        return self.program.linkage

    def resolve_name(self, info):
        return self.program.name

    def resolve_academic_year(self, info):
        return self.program.academic_year

    def resolve_terms_available(self, info):
        return self.program.terms_available.all()

    def resolve_is_graduate(self, info):
        return self.program.is_graduate


class InboundRequirementType(DjangoObjectType):
    class Meta:
        model = InboundRequirement


class InboundProgramType(DjangoObjectType, Program):
    requirements = List(InboundRequirementType)

    def resolve_requirements(self, info):
        return self.inboundrequirements_set.all()

    class Meta:
        model = InboundProgram


class OutboundRequirementType(DjangoObjectType):
    class Meta:
        model = OutboundRequirement


class OutboundProgramType(DjangoObjectType, Program):
    requirements = List(OutboundRequirementType)

    def resolve_requirements(self, info):
        return self.outboundrequirement_set.all()

    class Meta:
        model = OutboundProgram


class Query(ObjectType):
    countries = List(CountryType)
    institutions = List(InstitutionType, archived=Boolean(), year_archived=Int())
    memorandums = List(MemorandumType, archived=Boolean(), year_archived=Int())
    academic_years = List(AcademicYearType)
    terms = List(TermType, year=Int())
    outbound_programs = List(OutboundProgramType, institution=Int(), year=Int(), term=Int())
    inbound_programs = List(InboundProgramType, year=Int(), term=Int())
    outbound_requirements = List(OutboundRequirementType)
    inbound_requirements = List(InboundRequirementType)

    institution = Field(InstitutionType, id=Int())
    memorandum = Field(MemorandumType, id=Int())
    outbound_program = Field(OutboundProgramType, id=Int())
    inbound_program = Field(InboundProgramType, id=Int())

    def resolve_academic_years(self, info, **kwargs):
        return AcademicYear.objects.all()

    def resolve_countries(self, info, **kwargs):
        return [country for country in Country.objects.all() if
                country.institution_set.filter(archived_at__isnull=True).count() > 0]

    def resolve_institutions(self, info, **kwargs):
        archived = kwargs.get('archived', False)
        year_archived = kwargs.get('year_archived')

        return Institution.archived.filter(archived_at__year=year_archived) if archived else Institution.current.all()

    def resolve_memorandums(self, info, **kwargs):
        archived = kwargs.get('archived', False)
        year_archived = kwargs.get('year_archived')

        return Memorandum.archived.filter(archived_at__year=year_archived) if archived else Memorandum.current.all()

    def resolve_memorandum(self, info, **kwargs):
        id = kwargs.get('id')
        return Memorandum.current.get(pk=id)

    def resolve_institution(self, info, **kwargs):
        id = kwargs.get('id')
        return Institution.objects.get(pk=id)

    def resolve_terms(self, info, **kwargs):
        terms = Term.current.all()
        year = kwargs.get('year')

        if year:
            terms = terms.filter(academic_year__academic_year_start=year)

        return terms

    def resolve_outbound_programs(self, info, **kwargs):
        institution = kwargs.get('institution', False)
        year = kwargs.get('year', False)
        term = kwargs.get('term', False)

        outbound_programs = OutboundProgram.objects.all()

        if year:
            outbound_programs = outbound_programs.filter(program__academic_year__academic_year_start=year)

        if institution:
            outbound_programs = outbound_programs.filter(institution_id=institution)

        if term:
            outbound_programs = outbound_programs.filter(program__terms_available__number=term)

        return outbound_programs

    def resolve_outbound_program(self, info, **kwargs):
        id = kwargs.get('id')
        return OutboundProgram.objects.get(pk=id)

    def resolve_inbound_programs(self, info, **kwargs):
        year = kwargs.get('year', False)
        term = kwargs.get('term', False)

        inbound_programs = InboundProgram.objects.all()

        if year:
            inbound_programs = inbound_programs.filter(program__academic_year__academic_year_start=year)

        if term:
            inbound_programs = inbound_programs.filter(program__terms_available__number=term)

        return inbound_programs

    def resolve_inbound_program(self, info, **kwargs):
        id = kwargs.get('id')
        return InboundProgram.objects.get(pk=id)

    def resolve_inbound_requirements(self, info, **kwargs):
        return InboundRequirement.objects.all()

    def resolve_outbound_requirements(self, info, **kwargs):
        return OutboundRequirement.objects.all()
