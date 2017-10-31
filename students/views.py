from rest_framework.views import APIView
from rest_framework.response import Response
from students.serializers import StudentSerializer
from students.models import *

class StudentView(APIView):
    @staticmethod
    def get(request):
        students = Student.objects.all()
        student_serializer = StudentSerializer(students, many=True)

        return Response(student_serializer.data, status=200)

    @staticmethod
    def post(request):
        student_serializer = StudentSerializer(data=request.data)

        if student_serializer.is_valid():
            student_serializer.create(student_serializer.validated_data)
            return Response(student_serializer.data, status=200)
        else:
            return Response(student_serializer.errors, status=400)

