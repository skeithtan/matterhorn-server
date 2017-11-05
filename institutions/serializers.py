from rest_framework.relations import PrimaryKeyRelatedField

from .models import *
from rest_framework.serializers import ModelSerializer


class InstitutionSerializer(ModelSerializer):
    class Meta:
        model = Institution
        fields = "__all__"


class MemorandumSerializer(ModelSerializer):
    linkages = PrimaryKeyRelatedField(many=True, queryset=Linkage.objects.all())

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
