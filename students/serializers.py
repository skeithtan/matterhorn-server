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
        requirements = validated_data.pop('application_requirements')

        outbound_student_program = OutboundStudentProgram.objects.create(**validated_data)

        for term in terms:
            outbound_student_program.terms_duration.add(term)

        for requirement in requirements:
            outbound_student_program.application_requirement.add(requirement)

        outbound_student_program.save()
        return outbound_student_program

    def update(self, instance, validated_data):
        instance.application_requirements.clear()
        for requirement in validated_data['application_requirements']:
            instance.application_requirements.add(requirement)
        instance.save()
        return instance


class InboundStudentProgramSerializer(ModelSerializer):
    class Meta:
        model = InboundStudentProgram
        fields = "__all__"

    def create(self, validated_data):
        terms = validated_data.pop('terms_duration')
        requirements = validated_data.pop('application_requirements')
        inbound_student_program = InboundStudentProgram.objects.create(**validated_data)

        for term in terms:
                inbound_student_program.terms_duration.add(term)
        for requirement in requirements:
            inbound_student_program.application_requirements.add(requirement)

            inbound_student_program.save()
        return inbound_student_program

    def update(self, instance, validated_data):
        instance.application_requirements.clear()
        for requirement in validated_data['application_requirements']:
            instance.application_requirements.add(requirement)
        print(instance)
        instance.save()
        return instance


class DeployedStudentProgramSerializer(ModelSerializer):
    class Meta:
        model = DeployedStudentProgram
        fields = "__all__"

    def create(self, validated_data):
        outbound_student_program = OutboundStudentProgram.objects.get(student=self.context['student'])
        print(f"{outbound_student_program.student.pk} and {outbound_student_program.program}")
        if not outbound_student_program.is_requirements_complete:
            raise ValidationError("Not all requirements have been submitted by student!")

        validated_data["student_program"] = outbound_student_program
        deployed_student = DeployedStudentProgram.objects.create(**validated_data)
        deployed_student.student_program = outbound_student_program
        deployed_student.save()

        return deployed_student


class AcceptedStudentProgramSerializer(ModelSerializer):
    class Meta:
        model = AcceptedStudentProgram
        fields = "__all__"

    def create(self, validated_data):

        inbound_student_program = InboundStudentProgram.objects.get(student=self.context['student'])
        courses = validated_data.pop('inbound_courses')
        if not inbound_student_program.is_requirements_complete:
            raise ValidationError("Not all requirements have been submitted by student!")

        validated_data["student_program"] = inbound_student_program
        accepted_student = AcceptedStudentProgram.objects.create(**validated_data)
        accepted_student.student_program = inbound_student_program

        for course in courses:
            accepted_student.inbound_courses.add(course)
        accepted_student.save()

        return accepted_student

