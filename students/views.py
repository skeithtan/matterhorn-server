from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from students.serializers import *
from students.models import *

class StudentListCreateView(ListCreateAPIView):
    permission_classes = (IsAuthenticated, )
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentUpdateDestroyRetrieveView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get_queryset(self):
        student = self.kwargs['pk']
        return Student.objects.filter(id_number=student)

class ResidencyAddressHistoryListCreateView(ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = ResidencyAddressHistory.objects.all()
    serializer_class = ResidencyAddressHistorySerializer
    lookup_field = 'student_id'

    def get_queryset(self):
        student = self.kwargs['student_id']
        return ResidencyAddressHistory.objects.filter(student=student)

    def perform_create(self, serializer):
        student = Student.objects.get(id_number=self.kwargs['student_id'])
        serializer.save(student=student)


class ResidencyAddressHistoryUpdateDestroyRetrieveView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = ResidencyAddressHistory.objects.all()
    serializer_class = ResidencyAddressHistorySerializer
    lookup_field = 'student_id'

    def get_queryset(self):
        student = self.kwargs['student_id']
        residency = self.kwargs['residencyaddresshistory_id']
        return ResidencyAddressHistory.objects.filter(student=student, id=residency)


class StudentProgramListCreateView(ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = StudentProgram.objects.all()
    serializer_class = StudentProgramSerializer
    lookup_field = 'student_id'

    def get_queryset(self):
        student = self.kwargs['student_id']
        return StudentProgram.objects.filter(student=student)

    def perform_create(self, serializer):
        student = Student.objects.get(self.kwargs['student_id'])
        serializer.save(student=student)

class StudentProgramUpdateDestroyRetrieveView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = StudentProgram.objects.all()
    serializer_class = StudentProgramSerializer
    lookup_field = 'student_id'

    def get_queryset(self):
        student = self.kwargs['student_id']
        program_offering = self.kwargs['program_offering_id']
        return StudentProgram.objects.filter(student=student, program_offering=program_offering)
