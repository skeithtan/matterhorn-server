from django.http import Http404
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import ValidationError
from rest_framework.relations import PrimaryKeyRelatedField

from .models import *
from rest_framework.serializers import ModelSerializer, Serializer
from rest_framework import serializers


class InstitutionSerializer(ModelSerializer):
    class Meta:
        model = Institution
        fields = "__all__"


class MemorandumSerializer(ModelSerializer):
    linkages = PrimaryKeyRelatedField(many=True, queryset=Linkage.objects.all())

    class Meta:
        model = Memorandum
        exclude = ('institution', )


class LinkageSerializer(ModelSerializer):
    class Meta:
        model = Linkage


class ProgramSerializer(Serializer):
    memorandum = serializers.IntegerField()
    linkage = serializers.CharField()
    name = serializers.CharField(max_length=64)
    academic_year = serializers.IntegerField()
    terms = serializers.ListField(child=serializers.IntegerField())

    def validate_memorandum(self, value):
        try:
            memorandum = get_object_or_404(Memorandum, pk=value)
        except Http404:
            raise ValidationError("Memorandum does not exist!")

        value = memorandum
        return value

    def validate_linkage(self, value):
        try:
            linkage = get_object_or_404(Linkage, code=value)
        except Http404:
            raise ValidationError("Linkage does not exist!")

        value = linkage
        return value

    def validate_academic_year(self, value):
        try:
            academic_year = get_object_or_404(AcademicYear, academic_year_start=value)
        except Http404:
            academic_year = AcademicYear.objects.create(academic_year_start=value)
            print(academic_year)

        value = academic_year
        return value

    # def validate_terms(self, value):
    #     for term in value:
    #         if Term.objects.get(number=term)


    def create(self, validated_data):
        return Program.objects.create(**validated_data)


    # def create(self, validated_data):
    #     academic_year = validated_data["academic_year"]
    #     print("hello")
    #     if AcademicYear.objects.get(academic_year_start=academic_year) is None:
    #         #create if doesnt exist
    #         academic_year_attr = AcademicYear(
    #             academic_year_start=academic_year
    #         )
    #         academic_year_attr.save()
    #         validated_data["academic_year"] = academic_year_attr.pk
    #         return Program.objects.create(**validated_data)
    #     else:
    #         print("helloo")
    #         #assign if exist
    #         academic_year_attr = AcademicYear.objects.get(
    #             academic_year_start=academic_year
    #         )
    #         validated_data["academic_year"] = academic_year_attr.pk
    #         return Program.objects.create(**validated_data)

