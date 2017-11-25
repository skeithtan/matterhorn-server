from rest_framework.exceptions import ValidationError
from rest_framework.fields import SerializerMethodField
from rest_framework.relations import PrimaryKeyRelatedField
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
        validated_data['student_program'] = OutboundStudentProgram.objects.get(student=self.context['student'])
        student_program = (validated_data['student_program'])

        print(validated_data)

        if student_program.check_requirements(self) is False:
            print('lol1')
            raise ValidationError("Not all requirements have been submitted by student!")
        else:
            print('lol')
            deployed_student_instance = DeployedStudentProgram.objects.create(**validated_data)
            deployed_student_instance.save()
            return deployed_student_instance








