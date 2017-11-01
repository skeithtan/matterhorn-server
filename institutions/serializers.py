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
