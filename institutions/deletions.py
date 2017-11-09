from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from institutions.serializers import *
from institutions.models import *


class DeletedInstitutionsView(ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Institution.all_objects.exclude(deleted_at=None)
    serializer_class = InstitutionSerializer


class DeletedInstitutionUpdateDeletedView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Institution.all_objects.exclude(deleted_at=None)
    serializer_class = InstitutionSerializer

    def get_serializer(self, *args, **kwargs):
        kwargs['partial'] = True
        return super(DeletedInstitutionUpdateDeletedView, self).get_serializer(*args, **kwargs)


class DeletedMemorandumsView(ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Memorandum.all_objects.exclude(deleted_at=None)
    serializer_class = MemorandumSerializer


class DeletedMemorandumUpdateDeletedView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Memorandum.all_objects.exclude(deleted_at=None)
    serializer_class = MemorandumSerializer

    def get_serializer(self, *args, **kwargs):
        kwargs['partial'] = True
        return super(DeletedMemorandumUpdateDeletedView, self).get_serializer(*args, **kwargs)


class DeletedProgramsView(ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Program.all_objects.exclude(deleted_at=None)
    serializer_class = ProgramSerializer


class DeletedProgramUpdateView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Program.all_objects.exclude(deleted_at=None)
    serializer_class = ProgramSerializer

    def get_serializer(self, *args, **kwargs):
        kwargs['partial'] = True
        return super(DeletedProgramUpdateView, self).get_serializer(*args, **kwargs)
