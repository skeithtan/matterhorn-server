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


class MemorandumListCreateView(ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Memorandum.objects.all()
    serializer_class = MemorandumSerializer

    def get_institution(self):
        queryset = Institution.objects.all()
        return get_object_or_404(queryset, pk=self.kwargs['institution_id'])

    def get_queryset(self):
        institution = self.get_institution()
        return super().get_queryset().filter(institution=institution)

    def perform_create(self, serializer):
        institution = self.get_institution()
        serializer.save(institution=institution)


class MemorandumUpdateDestroyRetrieveView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Memorandum.objects.all()
    serializer_class = MemorandumSerializer


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


class ProgramUpdateDestroyRetrieveView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Program.objects.all()
    serializer_class = ProgramSerializer


class ProgramOfferingListCreateView(ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = ProgramOffering.objects.all()
    serializer_class = ProgramOfferingSerializer

    def get_program(self):
        queryset = Program.objects.all()
        return get_object_or_404(queryset, pk=self.kwargs['program_id'])

    def get_queryset(self):
        program = self.get_program()
        return super().get_queryset().filter(program=program)

    def perform_create(self, serializer):
        program = self.get_program()
        serializer.create(program=program)


class ProgramOfferingRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = ProgramOffering.objects.all()
    serializer_class = ProgramOfferingSerializer
