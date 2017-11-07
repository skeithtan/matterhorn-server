from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView, get_object_or_404
from rest_framework.permissions import IsAuthenticated
from institutions.serializers import *
from institutions.models import *


class InstitutionListCreateView(ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Institution.objects.all()
    serializer_class = InstitutionSerializer


class InstitutionUpdateDestroyRetrieveView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Institution.objects.all()
    serializer_class = InstitutionSerializer

    def get_serializer(self, *args, **kwargs):
        kwargs['partial'] = True
        return super(InstitutionUpdateDestroyRetrieveView, self).get_serializer(*args, **kwargs)

class MemorandumListCreateView(ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Memorandum.objects.all()
    serializer_class = MemorandumSerializer
    lookup_field = 'institution_id'

    def get_queryset(self):
        institution = self.kwargs['institution_id']
        return super().get_queryset().filter(institution=institution)

    def perform_create(self, serializer):
        institution = Institution.objects.get(id=self.kwargs['institution_id'])
        serializer.save(institution=institution)


class MemorandumUpdateDestroyRetrieveView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Memorandum.objects.all()
    serializer_class = MemorandumSerializer

    def get_serializer(self, *args, **kwargs):
        kwargs['partial'] = True
        return super(MemorandumUpdateDestroyRetrieveView, self).get_serializer(*args,**kwargs)


class ProgramListCreateView(ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Program.objects.all()
    serializer_class = ProgramSerializer

    def get_institution(self):
        queryset = Institution.objects.all()
        return get_object_or_404(queryset, pk=self.kwargs['institution_id'])

    def get_queryset(self):
        institution = self.get_institution()
        return super().get_queryset().filter(institution=institution)

    def perform_create(self, serializer):
        institution = self.get_institution()
        serializer.create(institution=institution)


class ProgramRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Program.objects.all()
    serializer_class = ProgramSerializer

    def get_serializer(self, *args, **kwargs):
        kwargs['partial'] = True
        return super(ProgramRetrieveUpdateDestroyView, self).get_serializer(*args,**kwargs)

class LinkageListCreateView(ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Linkage.objects.all()
    serializer_class = LinkageSerializer

class LinkageRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Linkage.objects.all()
    serializer_class = LinkageSerializer

    def get_serializer(self, *args, **kwargs):
        kwargs['partial'] = True
        return super(LinkageRetrieveUpdateDestroyView, self).get_serializer(*args,**kwargs)

