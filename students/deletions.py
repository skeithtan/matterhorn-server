from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from students.serializers import *
from students.models import *


class DeletedStudentView(ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Student.all_objects.exclude(deleted_at=None)
    serializer_class = StudentSerializer


class DeletedStudentUpdateView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Student.all_objects.exclude(deleted_at=None)
    serializer_class = StudentSerializer

    def get_serializer(self, *args, **kwargs):
        kwargs['partial'] = True
        return super(DeletedStudentUpdateView, self).get_serializer(*args, **kwargs)


class DeletedResidencyAddressHistoryView(ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = ResidencyAddressHistory.all_objects.exclude(deleted_at=None)
    serializer_class = ResidencyAddressHistorySerializer


class DeletedResidencyAddressHistoryUpdateView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = ResidencyAddressHistory.all_objects.exclude(deleted_at=None)
    serializer_class = ResidencyAddressHistorySerializer

    def get_serializer(self, *args, **kwargs):
        kwargs['partial'] = True
        return super(DeletedResidencyAddressHistoryUpdateView, self).get_serializer(*args, **kwargs)


class DeletedStudentProgramView(ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = StudentProgram.all_objects.exclude(deleted_at=None)
    serializer_class = StudentProgramSerializer


class DeletedStudentProgramUpdateView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = StudentProgram.all_objects.exclude(deleted_at=None)
    serializer_class = StudentProgramSerializer

    def get_serializer(self, *args, **kwargs):
        kwargs['partial'] = True
        return super(DeletedStudentProgramUpdateView, self).get_serializer(*args, **kwargs)

