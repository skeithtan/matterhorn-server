from rest_framework.exceptions import ValidationError
from rest_framework.fields import SerializerMethodField
from rest_framework.relations import PrimaryKeyRelatedField
from rest_framework.serializers import ModelSerializer
from .models import *
from django.db.models import Q


class StudentSerializer(ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"


class ResidencyAddressHistorySerializer(ModelSerializer):
    class Meta:
        model = ResidencyAddressHistory
        exclude = ('student',)


class OutboundStudentProgramSerializer(ModelSerializer):
    class Meta:
        model = OutboundStudentProgram
        fields = "__all__"

    def create(self, validated_data):
        terms = validated_data.pop('terms_duration')
        requirements = validated_data.pop('application_requirement')

        outbound_student_program = OutboundStudentProgram.objects.create(**validated_data)

        for term in terms:
            outbound_student_program.terms_duration.add(term)

        for requirement in requirements:
            outbound_student_program.application_requirement.add(requirement)

        outbound_student_program.save()
        return outbound_student_program

    def update(self, instance, validated_data):

        instance.application_requirement.clear()
        for requirement in validated_data['application_requirement']:
            instance.application_requirement.add(requirement)
        instance.save()
        return instance


class InboundStudentProgramSerializer(ModelSerializer):
    class Meta:
        model = InboundStudentProgram
        fields = "__all__"

    def create(self, validated_data):
        terms = validated_data.pop('terms_duration')
        inbound_student_program_instance = InboundStudentProgram.objects.create(**validated_data)

        for term in terms:
            inbound_student_program_instance.terms_duration.add(term)

        inbound_student_program_instance.save()
        return inbound_student_program_instance


class DeployedStudentProgramSerializer(ModelSerializer):
    class Meta:
        model = DeployedStudentProgram
        fields = "__all__"

    def create(self, validated_data):
        outbound_student_program = OutboundStudentProgram.objects.get(student=self.context['student'])
        if not outbound_student_program.is_requirements_complete:
            raise ValidationError("Not all requirements have been submitted by student!")

        validated_data["student_program"] = outbound_student_program
        deployed_student = DeployedStudentProgram.objects.create(**validated_data)
        deployed_student.student_program = outbound_student_program
        deployed_student.save()

        return deployed_student



