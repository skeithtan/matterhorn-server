from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from students.serializers import *
from students.models import *


class ArchivedStudentView(ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Student.all_objects.exclude(archived_at=None)
    serializer_class = StudentSerializer


class ArchivedStudentUpdateView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Student.all_objects.exclude(archived_at=None)
    serializer_class = StudentSerializer

    def get_serializer(self, *args, **kwargs):
        kwargs['partial'] = True
        return super(ArchivedStudentUpdateView, self).get_serializer(*args, **kwargs)


class ArchivedResidencyAddressHistoryView(ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = ResidencyAddressHistory.all_objects.exclude(archived_at=None)
    serializer_class = ResidencyAddressHistorySerializer


class ArchivedResidencyAddressHistoryUpdateView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = ResidencyAddressHistory.all_objects.exclude(archived_at=None)
    serializer_class = ResidencyAddressHistorySerializer

    def get_serializer(self, *args, **kwargs):
        kwargs['partial'] = True
        return super(ArchivedResidencyAddressHistoryUpdateView, self).get_serializer(*args, **kwargs)


class ArchivedStudentProgramView(ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = StudentProgram.all_objects.exclude(archived_at=None)
    serializer_class = StudentProgramSerializer


class ArchivedStudentProgramUpdateView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = StudentProgram.all_objects.exclude(archived_at=None)
    serializer_class = StudentProgramSerializer

    def get_serializer(self, *args, **kwargs):
        kwargs['partial'] = True
        return super(ArchivedStudentProgramUpdateView, self).get_serializer(*args, **kwargs)

