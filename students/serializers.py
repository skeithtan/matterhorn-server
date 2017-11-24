from rest_framework.serializers import ModelSerializer
from .models import *


class StudentSerializer(ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"


class ResidencyAddressHistorySerializer(ModelSerializer):
    class Meta:
        model = ResidencyAddressHistory
        exclude = ('student',)


class StudentProgramSerializer(ModelSerializer):
    class Meta:
        model = StudentProgram
        exclude = ('student', 'study_field')


class OutboundStudentProgramSerializer(ModelSerializer):
    class Meta:
        model = OutboundProgram
        fields = "__all__"


class InboundStudentProgramSerializer(ModelSerializer):
    class Meta:
        model = InboundProgram
        fields = "__all__"


class StudentApplicationRequirementSerializer(ModelSerializer):
    class Meta:
        model = StudentApplicationRequirement
        fields = "__all__"


class DeployedStudentProgramSerializer(ModelSerializer):
    class Meta:
        model = DeployedStudentProgram
        fields = "__all__"


