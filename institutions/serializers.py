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


#TODO: this
class AcademicYearSerializer(ModelSerializer):
    term_academic_year = TermSerializer(many=True)

    class Meta:
        model = AcademicYear
        fields = ['academic_year_start', 'term_academic_year']

    def create(self, validated_data):
        terms = validated_data.pop('term_academic_year')
        instance = AcademicYear.objects.create(**validated_data)

        for term in terms:
            Term.objects.create(term_academic_year=instance, **term)

        return instance


#TODO: This
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
        #returning pk also doesnt work
        return memorandum

    def validate_linkage(self, value):

        try:
            linkage = get_object_or_404(Linkage, code=value)
        except Http404:
            raise ValidationError("Linkage does not exist!")

        return linkage

    def validate_academic_year(self, value):
        try:
            academic_year = get_object_or_404(AcademicYear, academic_year_start=value)
        except Http404:
            academic_year = AcademicYear.objects.create(academic_year_start=value)

        return academic_year

    def validate_terms(self, value):
        queryset = []
        for term_number in value:
            try:
                queryset.append(get_object_or_404(Term, number=term_number))
            except Http404:
                raise ValidationError("Term does not exist!")

        return queryset

    def create(self, validated_data):
        program = Program()
        program.memorandum = validated_data["memorandum"]
        program.linkage = validated_data["linkage"]
        program.academic_year = validated_data["academic_year"]
        program.save()
        print(program)
        program.save()

        for term in validated_data["terms"]:
            program.terms.add(Term.objects.get(number=term))

        program.save()
        return program

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
