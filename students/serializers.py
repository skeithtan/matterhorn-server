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

    @staticmethod
    def is_requirements_complete(outbound_program):
        program = outbound_program.program
        requirements = Requirement.objects.filter(Q(program=program) | Q(program=None))

        print(requirements)
        for requirement in requirements:
            if requirement not in outbound_program.application_requirement.all():
                return False

        return True

    def create(self, validated_data):
        print(self.context["student"])

        validated_data["student_program"] = OutboundStudentProgram.objects.get(student=self.context['student'])
        outbound_program = validated_data["student_program"]

        if not self.is_requirements_complete(outbound_program):
            raise ValidationError("Not all requirements have been submitted by student!")

        deployed_student = DeployedStudentProgram.objects.create(**validated_data)
        deployed_student.student_program = outbound_program
        print(deployed_student)
        deployed_student.save()
        return deployed_student
