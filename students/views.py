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
    queryset = Student.current.all()
    serializer_class = StudentSerializer
    codename = 'crud_student'

    def get_serializer(self, *args, **kwargs):
        kwargs['partial'] = True
        return super(StudentRetrieveUpdateDestroyView, self).get_serializer(*args, **kwargs)

    def get_queryset(self):
        student = self.kwargs['pk']
        return super().get_queryset().filter(pk=student)


class ResidencyAddressHistoryListCreateView(MasterGenericAPIViewMixin):
    permission_classes = (IsAuthenticated,)
    queryset = ResidencyAddressHistory.objects.all()
    serializer_class = ResidencyAddressHistorySerializer
    lookup_field = 'student_id'
    codename = 'crud_student'

    def get_queryset(self):
        student = self.kwargs['student_id']
        return super().get_queryset().filter(student=student)


class ResidencyAddressHistoryRetrieveUpdateDestroyView(MasterGenericAPIViewMixin):
    permission_classes = (IsAuthenticated,)
    queryset = ResidencyAddressHistory.current
    serializer_class = ResidencyAddressHistorySerializer
    lookup_field = 'student_id'
    codename = 'crud_student'

    def get_serializer(self, *args, **kwargs):
        kwargs['partial'] = True
        return super(ResidencyAddressHistoryRetrieveUpdateDestroyView, self).get_serializer(*args, **kwargs)

    def get_queryset(self):
        student = self.kwargs['student_id']
        residency = self.kwargs['residencyaddresshistory_id']
        return super().get_queryset().filter(student=student, id=residency)
