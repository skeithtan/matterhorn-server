from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated

from core.mixins import MasterGenericAPIViewMixin
from students.serializers import *
from students.models import *


class StudentListCreateView(MasterGenericAPIViewMixin):
    permission_classes = (IsAuthenticated,)
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    codename = 'crud_student'


class StudentRetrieveUpdateDestroyView(MasterGenericAPIViewMixin):
    permission_classes = (IsAuthenticated,)
    queryset = Student.all_objects
    serializer_class = StudentSerializer
    codename = 'crud_student'

    def get_queryset(self):
        student = self.kwargs['pk']
        return Student.objects.filter(pk=student)


class ResidencyAddressHistoryListCreateView(MasterGenericAPIViewMixin):
    permission_classes = (IsAuthenticated,)
    queryset = ResidencyAddressHistory.objects.all()
    serializer_class = ResidencyAddressHistorySerializer
    lookup_field = 'student_id'
    codename = 'crud_student'

    def get_queryset(self):
        student = self.kwargs['student_id']
        return ResidencyAddressHistory.objects.filter(student=student)


class ResidencyAddressHistoryRetrieveUpdateDestroyView(MasterGenericAPIViewMixin):
    permission_classes = (IsAuthenticated,)
    queryset = ResidencyAddressHistory.all_objects
    serializer_class = ResidencyAddressHistorySerializer
    lookup_field = 'student_id'
    codename = 'crud_student'

    def get_queryset(self):
        student = self.kwargs['student_id']
        residency = self.kwargs['residencyaddresshistory_id']
        return ResidencyAddressHistory.objects.filter(student=student, id=residency)


class StudentProgramListCreateView(MasterGenericAPIViewMixin):
    permission_classes = (IsAuthenticated,)
    queryset = StudentProgram.objects.all()
    serializer_class = StudentProgramSerializer
    lookup_field = 'student_id'
    codename = 'crud_student'

    def get_queryset(self):
        student = self.kwargs['student_id']
        return StudentProgram.objects.filter(student=student)

    def perform_create(self, serializer):
        student = Student.objects.get(self.kwargs['student_id'])
        serializer.save(student=student)


class StudentProgramRetrieveUpdateDestroyView(MasterGenericAPIViewMixin):
    permission_classes = (IsAuthenticated,)
    queryset = StudentProgram.all_objects
    serializer_class = StudentProgramSerializer
    lookup_field = 'student_id'
    codename = 'crud_student'

    def get_queryset(self):
        student = self.kwargs['student_id']
        program_offering = self.kwargs['program_offering_id']
        return StudentProgram.objects.filter(student=student, program_offering=program_offering)
