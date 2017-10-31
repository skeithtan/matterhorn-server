from rest_framework.views import APIView
from rest_framework.response import Response
from institutions.serializers import InstitutionSerializer
from institutions.models import *


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
                "response": "created institution"
            }, status=200)

        else:
            return Response(data=institution_serializer.errors, status=400)


class InstitutionDetail(APIView):
    @staticmethod
    def get(request, institution_id):
        institution = Institution.objects.get(id=institution_id)
        institution_serializer = InstitutionSerializer(institution)
        return Response(data=institution_serializer.data, status=200)
