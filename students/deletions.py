from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from students.serializers import *
from students.models import *


class StudentBinView(ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Student.all_objects.exclude(deleted_at=None)
    serializer_class = StudentSerializer


class StudentUpdateBinView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Student.all_objects.exclude(deleted_at=None)
    serializer_class = StudentSerializer

    def get_serializer(self, *args, **kwargs):
        kwargs['partial'] = True
        return super(StudentUpdateBinView, self).get_serializer(*args, **kwargs)


class ResidencyAddressHistoryBinView(ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = ResidencyAddressHistory.all_objects.exclude(deleted_at=None)
    serializer_class = ResidencyAddressHistorySerializer


class ResidencyAddressHistoryUpdateBinView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = ResidencyAddressHistory.all_objects.exclude(deleted_at=None)
    serializer_class = ResidencyAddressHistorySerializer

    def get_serializer(self, *args, **kwargs):
        kwargs['partial'] = True
        return super(ResidencyAddressHistoryUpdateBinView, self).get_serializer(*args, **kwargs)


class StudentProgramBinView(ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = StudentProgram.all_objects.exclude(deleted_at=None)
    serializer_class = StudentProgramSerializer


class StudentProgramUpdateBinView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = StudentProgram.all_objects.exclude(deleted_at=None)
    serializer_class = StudentProgramSerializer

    def get_serializer(self, *args, **kwargs):
        kwargs['partial'] = True
        return super(StudentProgramUpdateBinView, self).get_serializer(*args, **kwargs)

