from rest_framework.views import APIView
from rest_framework.response import Response
from institutions.serializers import *
from institutions.models import *
from django.shortcuts import get_object_or_404


class InstitutionView(APIView):
    @staticmethod
    def get(request):
        institutions = Institution.objects.all()
        institutions_serializer = InstitutionSerializer(institutions, many=True).data

        return Response(data=institutions_serializer, status=200)

    @staticmethod
    def post(request):
        institution_serializer = InstitutionSerializer(data=request.data)

        if institution_serializer.is_valid():
            institution_serializer.create(institution_serializer.validated_data)

            return Response(data={
                "response": institution_serializer.data
            }, status=200)

        else:
            return Response(data=institution_serializer.errors, status=400)


class InstitutionDetail(APIView):
    @staticmethod
    def get(request, institution_id):
        institution = Institution.objects.get(id=institution_id)
        institution_serializer = InstitutionSerializer(institution)
        return Response(data=institution_serializer.data, status=200)


class MemorandumView(APIView):
    @staticmethod
    def post(request, institution_id):
        request.data["institution"] = institution_id
        memorandum_serializer = MemorandumSerializer(data=request.data)

        if memorandum_serializer.is_valid():
            memorandum_serializer.create(memorandum_serializer.validated_data)

            return Response(data={
                "response": memorandum_serializer.data
            }, status=200)

        else:
            return Response(data=memorandum_serializer.errors, status=400)

class MemorandumDetail(APIView):
    @staticmethod
    def put(request, institution_id, memorandum_id):
        memorandum = get_object_or_404(Memorandum, id=memorandum_id)
        memorandum_serializer = MemorandumSerializer(data=request.data)

        if memorandum_serializer.is_valid():
            memorandum.institution = Institution.objects.get(id=memorandum_serializer.serialized_data["institution"])

            return Response(data={
                "response": memorandum_serializer.data
            }, status=200)

        else:
            return Response(data=memorandum_serializer.errors, status=400)
