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

# i keep forgetting we dont need this cos it's get :((( -- kammy
    def get_queryset(self):
        student = self.kwargs['student_id']
        return ResidencyAddressHistory.objects.filter(student=student)



# class ResidencyAddressHistoryUpdateDestroyRetrieveView(RetrieveUpdateDestroyAPIView):
#     permission_classes = (IsAuthenticated,)
#     queryset = ResidencyAddressHistory.objects.all()
#     serializer_class = StudentSerializer
#     lookup_fields = ('student_id', 'residencyaddresshistory_id')
#     lookup_url_kwarg = ('student_id', 'residencyaddresshistory_id')