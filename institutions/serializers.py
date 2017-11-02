from .models import *
from rest_framework.serializers import ModelSerializer


class InstitutionSerializer(ModelSerializer):
    class Meta:
        model = Institution
        fields = "__all__"


class MemorandumSerializer(ModelSerializer):
    class Meta:
        model = Memorandum
        exclude = ('institution', )


class ProgramSerializer(ModelSerializer):
    class Meta:
        model = Program
        exclude = ('institution', )


class ProgramOfferingSerializer(ModelSerializer):
    class Meta:
        model = ProgramOffering
        exclude = ('program', )
