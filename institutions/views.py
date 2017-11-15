from rest_framework.generics import ListCreateAPIView, get_object_or_404
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

from core.mixins import MasterGenericAPIViewMixin, SharedReadOnlyMixin
from institutions.serializers import *
from institutions.models import *
from django.contrib.auth.models import Permission
from rest_framework.response import Response


class InstitutionListCreateView(SharedReadOnlyMixin):
    permission_classes = (IsAuthenticated,)
    queryset = Institution.objects.all()
    serializer_class = InstitutionSerializer


class InstitutionUpdateDestroyRetrieveView(MasterGenericAPIViewMixin):
    permission_classes = (IsAuthenticated,)
    queryset = Institution.current
    serializer_class = InstitutionSerializer
    codename = 'crud_memorandum'

    def get_serializer(self, *args, **kwargs):
        kwargs['partial'] = True
        return super(InstitutionUpdateDestroyRetrieveView, self).get_serializer(*args, **kwargs)

    def get_queryset(self):
        institution = self.kwargs['pk']
        return super().get_queryset().filter(pk=institution)


class MemorandumListCreateView(SharedReadOnlyMixin):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Memorandum.objects.all()
    serializer_class = MemorandumSerializer
    lookup_field = 'institution_id'

    def get_queryset(self):
        institution = self.kwargs['institution_id']
        return super().get_queryset().filter(institution=institution)

    def perform_create(self, serializer):
        institution = Institution.objects.get(id=self.kwargs['institution_id'])
        serializer.save(institution=institution)


class MemorandumUpdateDestroyRetrieveView(MasterGenericAPIViewMixin):
    permission_classes = (IsAuthenticated,)
    queryset = Memorandum.current
    serializer_class = MemorandumSerializer
    codename = 'crud_memorandum'

    def get_serializer(self, *args, **kwargs):
        kwargs['partial'] = True
        return super(MemorandumUpdateDestroyRetrieveView, self).get_serializer(*args, **kwargs)

    def get_queryset(self):
        memorandum = self.kwargs['pk']
        return super().get_queryset().filter(pk=memorandum)


class ProgramListCreateView(SharedReadOnlyMixin):
    permission_classes = (IsAuthenticated,)
    queryset = Program.current
    serializer_class = ProgramSerializer


class ProgramRetrieveUpdateDestroyView(MasterGenericAPIViewMixin):
    permission_classes = (IsAuthenticated,)
    queryset = Program.current
    serializer_class = ProgramSerializer
    codename = 'crud_memorandum'

    def get_serializer(self, *args, **kwargs):
        kwargs['partial'] = True
        return super(ProgramRetrieveUpdateDestroyView, self).get_serializer(*args, **kwargs)

    def get_queryset(self):
        program = self.kwargs['pk']
        return super().get_queryset().filter(pk=program)

class LinkageListCreateView(MasterGenericAPIViewMixin):
    permission_classes = (IsAuthenticated,)
    queryset = Linkage.objects.all()
    serializer_class = LinkageSerializer
    codename = 'crud_memorandum'


class LinkageRetrieveUpdateDestroyView(MasterGenericAPIViewMixin):
    permission_classes = (IsAuthenticated,)
    queryset = Linkage.objects.all()
    serializer_class = LinkageSerializer
    codename = 'crud_memorandum'

    def get_serializer(self, *args, **kwargs):
        kwargs['partial'] = True
        return super(LinkageRetrieveUpdateDestroyView, self).get_serializer(*args, **kwargs)


class AcademicYearListCreateView(MasterGenericAPIViewMixin):
    permission_classes = (IsAuthenticated,)
    queryset = AcademicYear.objects.all()
    serializer_class = AcademicYearSerializer
    codename = 'crud_student'

    def get_serializer(self, *args, **kwargs):
        kwargs['partial'] = True
        return super(AcademicYearListCreateView, self).get_serializer(*args, **kwargs)


class TermListCreateView(ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Term.objects.all()
    serializer_class = TermSerializer
