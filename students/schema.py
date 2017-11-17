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


class StudentStudyFieldType(DjangoObjectType):
    class Meta:
        model = StudentStudyField


class Query(ObjectType):
    students = List(StudentType, archived=Boolean(), year_archived=Int(), category=String())
    resident_address_histories = List(ResidencyAddressHistoryType, student=Int())
    student_study_fields = List(StudentStudyFieldType)

    student = Field(StudentType, id=Int())
    resident_address_history = Field(ResidencyAddressHistoryType, id=Int())
    student_study_field = Field(StudentStudyFieldType, id=Int())

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

    def resolve_student_study_fields(self, info, **kwargs):
        return StudentStudyField.objects.all()

    def resolve_student(self, info, **kwargs):
        return Student.objects.get(pk=kwargs.get('id'))

    def resolve_resident_address_history(self, info, **kwargs):
        return ResidencyAddressHistory.objects.get(pk=kwargs.get('id'))

    def resolve_student_study_field(self, info, **kwargs):
        return StudentStudyField.objects.get(pk=kwargs.get('id'))
