from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from programs.serializers import MobilitySerializer,ProgramSerializer
from programs.models import *


# Create your views here.

class MobilityView(APIView):
    @staticmethod
    def post(request):
        mobility_serializer = MobilitySerializer(data=request.data)
        if mobility_serializer.is_valid():
            mobility_serializer.create(mobility_serializer.validated_data)
            return Response(data={
                "response": mobility_serializer.data
            }, status=200)

        else:
            return Response(data=mobility_serializer.errors, status=400)


class ProgramView(APIView):
    @staticmethod
    def post(request):
        program_serializer = ProgramSerializer(data=request.data)
        if program_serializer.is_valid():
            program_serializer.create(program_serializer.validated_data)
            return Response(data={
                "response": program_serializer.data
            }, status=200)

        else:
            return Response(data=program_serializer.errors, status=400)
