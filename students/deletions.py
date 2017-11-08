from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from students.serializers import *
from students.models import *


class StudentBinView(ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Student.all_objects.exclude(deleted_at=None)
    serializer_class = StudentSerializer


class ResidencyAddressHistoryBinView(ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = ResidencyAddressHistory.all_objects.exclude(deleted_at=None)
    serializer_class = ResidencyAddressHistorySerializer


class StudentProgramBinView(ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = StudentProgram.all_objects.exclude(deleted_at=None)
    serializer_class = StudentProgramSerializer
