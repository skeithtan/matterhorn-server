from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from institutions.serializers import *
from institutions.models import *


class InstitutionBinView(ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Institution.all_objects.exclude(deleted_at=None)
    serializer_class = InstitutionSerializer


class InstitutionUpdateBinView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Institution.all_objects.exclude(deleted_at=None)
    serializer_class = InstitutionSerializer

    def get_serializer(self, *args, **kwargs):
        kwargs['partial'] = True
        return super(InstitutionUpdateBinView, self).get_serializer(*args, **kwargs)


class MemorandumBinView(ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Memorandum.all_objects.exclude(deleted_at=None)
    serializer_class = MemorandumSerializer


class MemorandumUpdateBinView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Memorandum.all_objects.exclude(deleted_at=None)
    serializer_class = MemorandumSerializer

    def get_serializer(self, *args, **kwargs):
        kwargs['partial'] = True
        return super(MemorandumUpdateBinView, self).get_serializer(*args, **kwargs)


class ProgramBinView(ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Program.all_objects.exclude(deleted_at=None)
    serializer_class = ProgramSerializer


class ProgramUpdateBinView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Program.all_objects.exclude(deleted_at=None)
    serializer_class = ProgramSerializer

    def get_serializer(self, *args, **kwargs):
        kwargs['partial'] = True
        return super(ProgramUpdateBinView, self).get_serializer(*args, **kwargs)