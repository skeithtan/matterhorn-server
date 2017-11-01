from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from students.serializers import StudentSerializer
from students.models import *

class StudentListCreateView(ListCreateAPIView):
    permission_classes = (IsAuthenticated, )
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentUpdateDestroyRetrieveView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class ResidencyAddressHistoryListCreateView(ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class ResidencyAddressHistoryUpdateDestroyRetrieveView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
