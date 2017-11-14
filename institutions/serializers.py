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
        exclude = ('academic_year', )


class AcademicYearSerializer(Serializer):
    academic_year_start = serializers.IntegerField()
    terms = TermSerializer(many=True, write_only=True)

    def validate_academic_year_start(self, value):
        if AcademicYear.objects.filter(pk=value):
            raise ValidationError("Academic Year Exists!")
        else:
            return value

    # def validate_terms(self, value):
    #     term_serializer = TermSerializer(date=value)
    #     if term_serializer.is_valid() is False:
    #         raise ValidationError("All fields for term must have values!")
    #
    #     return value

    def create(self, validated_data):
        terms = validated_data.pop('terms')
        instance = AcademicYear.objects.create(**validated_data)

        for term in terms:
            Term.objects.create(academic_year=instance, **term)

        return instance


#TODO: This
class ProgramSerializer(ModelSerializer):
    memorandum = PrimaryKeyRelatedField(queryset=Memorandum.objects.all())
    linkage = PrimaryKeyRelatedField(queryset=Linkage.objects.all())
    terms = PrimaryKeyRelatedField(many=True, queryset=Term.objects.all())
    academic_year = PrimaryKeyRelatedField(queryset=AcademicYear.objects.all())

    class Meta:
        model = Program
        fields = "__all__"


