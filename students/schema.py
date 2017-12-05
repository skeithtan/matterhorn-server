from graphene_django.types import DjangoObjectType
from .models import *

from graphene import (
    ObjectType,
    List,
    Field,
    Int,
    Boolean, String)


class ResidencyAddressHistoryType(DjangoObjectType):
    class Meta:
        model = ResidencyAddressHistory


class StudentType(DjangoObjectType):
    residencies = List(ResidencyAddressHistoryType)
    latest_residency = Field(ResidencyAddressHistoryType)

    def resolve_residencies(self, info, **kwargs):
        return self.residencies

    def resolve_latest_residency(self, info, **kwargs):
        return self.latest_residency

    class Meta:
        model = Student


class OutboundStudentProgramType(DjangoObjectType):
    is_requirements_complete = Boolean()

    def resolve_is_requirements_complete(self, info):
        return self.is_requirements_complete

    class Meta:
        model = OutboundStudentProgram


class InboundStudentProgramType(DjangoObjectType):
    is_requirements_complete = Boolean()

    def resolve_is_requirements_complete(self, info):
        return self.is_requirements_complete

    class Meta:
        model = InboundStudentProgram


class Query(ObjectType):
    students = List(StudentType, archived=Boolean(), year_archived=Int(), category=String())
    resident_address_histories = List(ResidencyAddressHistoryType, student=Int())
    outbound_student_programs = List(OutboundStudentProgramType, deployed=Boolean())
    inbound_student_programs = List(InboundStudentProgramType, accepted=Boolean())

    student = Field(StudentType, id=Int())
    resident_address_history = Field(ResidencyAddressHistoryType, id=Int())

    def resolve_students(self, info, **kwargs):
        archived = kwargs.get('archived', False)
        year_archived = kwargs.get('year_archived')
        category = kwargs.get('category', 'all')

        students = Student.archived.filter(archived_at__year=year_archived) if archived else Student.current.all()

        if category == 'all':
            return students

        return students.filter(category=category)

    def resolve_resident_address_histories(self, info, **kwargs):
        student = kwargs.get('student')
        return ResidencyAddressHistory.objects.filter(student=student)

    def resolve_student(self, info, **kwargs):
        return Student.objects.get(pk=kwargs.get('id'))

    def resolve_resident_address_history(self, info, **kwargs):
        return ResidencyAddressHistory.objects.get(pk=kwargs.get('id'))

    def resolve_outbound_student_programs(self, info, **kwargs):
        deployed = kwargs.get('deployed', False)
        return OutboundStudentProgram.deployed() if deployed else OutboundStudentProgram.applicants()

    def resolve_inbound_student_programs(self, info, **kwargs):
        accepted = kwargs.get('accepted', False)
        return InboundStudentProgram.accepted() if accepted else InboundStudentProgram.applicants()
