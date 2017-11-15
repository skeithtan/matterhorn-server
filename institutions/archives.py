from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from institutions.serializers import *
from institutions.models import *


class ArchivedInstitutionsView(ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Institution.archived.all()
    serializer_class = InstitutionSerializer


class ArchivedInstitutionUpdateDeletedView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Institution.archived.all()
    serializer_class = InstitutionSerializer

    def get_serializer(self, *args, **kwargs):
        kwargs['partial'] = True
        return super(ArchivedInstitutionUpdateDeletedView, self).get_serializer(*args, **kwargs)


class ArchivedMemorandumsView(ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Memorandum.archived.all()
    serializer_class = MemorandumSerializer


class ArchivedMemorandumUpdateDeletedView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Memorandum.archived.all()
    serializer_class = MemorandumSerializer

    def get_serializer(self, *args, **kwargs):
        kwargs['partial'] = True
        return super(ArchivedMemorandumUpdateDeletedView, self).get_serializer(*args, **kwargs)


class ArchivedProgramsView(ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Program.archived.all()
    serializer_class = ProgramSerializer


class ArchivedProgramUpdateView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Program.archived.all()
    serializer_class = ProgramSerializer

    def get_serializer(self, *args, **kwargs):
        kwargs['partial'] = True
        return super(ArchivedProgramUpdateView, self).get_serializer(*args, **kwargs)
