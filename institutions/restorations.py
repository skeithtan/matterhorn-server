from core.views import ModelRestoreView
from institutions.models import Institution, Memorandum, Program
from institutions.serializers import InstitutionSerializer, MemorandumSerializer, ProgramSerializer


class InstitutionRestoreView(ModelRestoreView):
    def get_model(self):
        return Institution

    def get_serializer_class(self):
        return InstitutionSerializer


class MemorandumRestoreView(ModelRestoreView):
    def get_model(self):
        return Memorandum

    def get_serializer_class(self):
        return MemorandumSerializer


class ProgramRestoreView(ModelRestoreView):
    def get_model(self):
        return Program

    def get_serializer_class(self):
        return ProgramSerializer