from .models import *
from rest_framework.serializers import ModelSerializer


class InstitutionSerializer(ModelSerializer):
    class Meta:
        model = Institution
        fields = "__all__"


class InstitutionMemorandumSerializer(ModelSerializer):
    class Meta:
        model = InstitutionMemorandum
        fields = "__all__"


class MemorandumVersionSerializer(ModelSerializer):
    class Meta:
        model = MemorandumVersion
        fields = "__all__"

class ProgramSerializer(ModelSerializer):
    class Meta:
        model = Program
        fields = "__all__"
        
class ProgramOffering(ModelSerializer):
    class Meta:
        model = ProgramOffering
        fields = "__all__"
