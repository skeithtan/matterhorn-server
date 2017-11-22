from django.http import Http404, request
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import ValidationError
from rest_framework.relations import PrimaryKeyRelatedField

from .models import *
from rest_framework.serializers import ModelSerializer, Serializer, BaseSerializer
from rest_framework import serializers


class InstitutionSerializer(ModelSerializer):
    class Meta:
        model = Institution
        fields = "__all__"


class MemorandumSerializer(ModelSerializer):
    linkages = PrimaryKeyRelatedField(many=True, queryset=Linkage.objects.all())

    class Meta:
        model = Memorandum
        exclude = ('institution',)


class LinkageSerializer(ModelSerializer):
    class Meta:
        model = Linkage


class TermSerializer(ModelSerializer):
    class Meta:
        model = Term
        exclude = ('academic_year',)


class AcademicYearSerializer(Serializer):
    academic_year_start = serializers.IntegerField()
    terms = TermSerializer(many=True)

    def validate_academic_year_start(self, value):
        if AcademicYear.objects.filter(pk=value):
            raise ValidationError("Academic Year exists")
        else:
            return value

    def validate_terms(self, value):
        term_serializer = TermSerializer(data=value)
        if term_serializer.is_valid() is False:
            raise ValidationError("All fields for term must have values!")

        return value

    def create(self, validated_data):
        terms = validated_data.pop('terms')
        instance = AcademicYear.objects.create(**validated_data)

        for term in terms:
            Term.objects.create(academic_year=instance, **term)

        return instance


# TODO: This
class ProgramSerializer(ModelSerializer):
    class Meta:
        model = Program
        fields = "__all__"


class InboundProgramSerializer(ModelSerializer):
    program = PrimaryKeyRelatedField(queryset=Program.objects.all())

    # def validate_program(self, value):
    #     program_serializer = ProgramSerializer(data=value)
    #     if program_serializer.is_valid() is False:
    #         raise ValidationError("All fields for program must have values")
    #     return value
    #
    # def create(self, validated_data):
    #     instance = Program.objects.create(**validated_data)
    #     inbound_program = InboundProgram.objects.create(program=instance)
    #
    #     return inbound_program
    class Meta:
        model = Program
        fields = "__all__"

    def create(self, validated_data):
        instance = Program.objects.create(**validated_data)
        inbound_program = InboundProgram.objects.create(program=instance)
        return inbound_program






