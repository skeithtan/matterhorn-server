from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from institutions.serializers import *
from institutions.models import *


class InstitutionBinView(ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Institution.all_objects.exclude(deleted_at=None)
    serializer_class = InstitutionSerializer


class MemorandumBinView(ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Memorandum.all_objects.exclude(deleted_at=None)
    serializer_class = MemorandumSerializer


class ProgramBinView(ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Program.all_objects.exclude(deleted_at=None)
    serializer_class = ProgramSerializer
