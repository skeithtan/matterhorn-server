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

class LinkageSerializer(ModelSerializer):
    class Meta:
        model = Linkage

class ProgramSerializer(ModelSerializer):
    class Meta:
        model = Program
        exclude = ('institution', )
