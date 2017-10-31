from .models import *
from rest_framework.serializers import ModelSerializer, CharField


class InstitutionSerializer(ModelSerializer):
    class Meta:
        model = Institution
        fields = "__all__"

class MemorandumSerializer(ModelSerializer):
    class Meta:
        model = Memorandum
        fields = "__all__"


