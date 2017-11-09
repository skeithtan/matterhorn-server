from rest_framework.generics import ListCreateAPIView, get_object_or_404
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

from core.mixins import MasterGenericAPIViewMixin
from core.views import ModelUpdateDestroyRetrieveView
from institutions.serializers import *
from institutions.models import *
from django.contrib.auth.models import Permission
from rest_framework.response import Response


class InstitutionListCreateView(ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Institution.objects.all()
    serializer_class = InstitutionSerializer


class InstitutionUpdateDestroyRetrieveView(ModelUpdateDestroyRetrieveView):
    permission_classes = (IsAuthenticated,)
    queryset = Institution.all_objects
    serializer_class = InstitutionSerializer


class MemorandumListCreateView(MasterGenericAPIViewMixin):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Memorandum.objects.all()
    serializer_class = MemorandumSerializer
    lookup_field = 'institution_id'
    codename = 'crud_memorandum'

    def get_queryset(self):
        institution = self.kwargs['institution_id']
        return super().get_queryset().filter(institution=institution)

    def perform_create(self, serializer):
        institution = Institution.objects.get(id=self.kwargs['institution_id'])
        serializer.save(institution=institution)


class MemorandumUpdateDestroyRetrieveView(MasterGenericAPIViewMixin):
    permission_classes = (IsAuthenticated,)
    queryset = Memorandum.all_objects
    serializer_class = MemorandumSerializer
    codename = 'crud_memorandum'


class ProgramListCreateView(MasterGenericAPIViewMixin):
    permission_classes = (IsAuthenticated,)
    queryset = Program.objects.all()
    serializer_class = ProgramSerializer
    codename = 'crud_memorandum'


class ProgramRetrieveUpdateDestroyView(MasterGenericAPIViewMixin):
    permission_classes = (IsAuthenticated,)
    queryset = Program.all_objects
    serializer_class = ProgramSerializer
    codename = 'crud_memorandum'


class LinkageListCreateView(MasterGenericAPIViewMixin):
    permission_classes = (IsAuthenticated,)
    queryset = Linkage.objects.all()
    serializer_class = LinkageSerializer
    codename = 'crud_memorandum'


class LinkageRetrieveUpdateDestroyView(ModelUpdateDestroyRetrieveView):
    permission_classes = (IsAuthenticated,)
    queryset = Linkage.objects.all()
    serializer_class = LinkageSerializer

    def get_serializer(self, *args, **kwargs):
        kwargs['partial'] = True
        return super(LinkageRetrieveUpdateDestroyView, self).get_serializer(*args, **kwargs)
