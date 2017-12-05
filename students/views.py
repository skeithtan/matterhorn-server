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

    def perform_create(self, serializer):
        student = Student.objects.get(pk=self.kwargs['student_id'])
        serializer.save(student=student)

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
        residency = self.kwargs['pk']
        return super().get_queryset().filter(student=student, id=residency)


class InboundStudentProgramListCreateView(MasterGenericAPIViewMixin):
    permission_classes = (IsAuthenticated, )
    queryset = InboundStudentProgram.objects.all()
    serializer_class = InboundStudentProgramSerializer
    codename = 'crud_student'


class InboundStudentProgramRetrieveUpdateDestroyView(MasterGenericAPIViewMixin):
    permission_classes = (IsAuthenticated, )
    queryset = InboundStudentProgram.current.all()
    serializer_class = InboundStudentProgramSerializer
    codename = 'crud_student'
    lookup_url_kwargs = 'inbound_program_id'

    def get_serializer(self, *args, **kwargs):
        kwargs['partial'] = True
        return super(InboundStudentProgramRetrieveUpdateDestroyView, self).get_serializer(*args, **kwargs)

    def get_queryset(self):
        student = self.kwargs['pk']
        return super().get_queryset().filter(id=student)


class OutboundStudentProgramListCreateView(MasterGenericAPIViewMixin):
    permission_classes = (IsAuthenticated, )
    queryset = OutboundStudentProgram.objects.all()
    serializer_class = OutboundStudentProgramSerializer
    codename = 'crud_student'


class OutboundStudentProgramRetrieveUpdateDestroyView(MasterGenericAPIViewMixin):
    permission_classes = (IsAuthenticated, )
    queryset = OutboundStudentProgram.objects.all()
    serializer_class = OutboundStudentProgramSerializer
    lookup_url_kwargs = 'outbound_program_id'
    codename = 'crud_student'

    def get_serializer(self, *args, **kwargs):
        kwargs['partial'] = True
        return super(OutboundStudentProgramRetrieveUpdateDestroyView, self).get_serializer(*args, **kwargs)

    def get_queryset(self):
        student = self.kwargs['pk']
        return super().get_queryset().filter(id=student)


class DeployedStudentProgramListCreateView(MasterGenericAPIViewMixin):
    permission_classes = (IsAuthenticated, )
    queryset = DeployedStudentProgram.objects.all()
    serializer_class = DeployedStudentProgramSerializer
    codename = 'crud_student'

    def get_serializer(self, *args, **kwargs):
        kwargs['partial'] = True
        return super(DeployedStudentProgramListCreateView, self).get_serializer(*args, **kwargs)

    def get_serializer_context(self):
        return {'student': self.kwargs['pk']}


class AcceptedStudentProgramListCreateView(MasterGenericAPIViewMixin):
    permission_classes = (IsAuthenticated,)
    queryset = AcceptedStudentProgram.objects.all()
    serializer_class = AcceptedStudentProgramSerializer
    codename = 'crud_student'

    def get_serializer(self, *args, **kwargs):
        kwargs['partial'] = True
        return super(AcceptedStudentProgramListCreateView, self).get_serializer(*args, **kwargs)

    def get_serializer_context(self):
        return {'student': self.kwargs['pk']}






