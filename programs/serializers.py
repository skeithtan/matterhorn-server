from institutions.models import Institution
from .models import *
from rest_framework.serializers import ModelSerializer, CharField

class MobilitySerializer(ModelSerializer):
    class Meta:
        model = Mobility
        fields = '__all__'

class ProgramSerializer(ModelSerializer):
    class Meta:
        model = Program
        fields = '__all__'