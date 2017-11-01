from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from institutions.serializers import *
from institutions.models import *


class InstitutionListCreateView(ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Institution.objects.all()
    serializer_class = InstitutionSerializer


class InstitutionUpdateDestroyRetrieveView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Institution.objects.all()
    serializer_class = InstitutionSerializer


# # TODO: This
# class MemorandumCreateView(ListCreateAPIView):
#     permission_classes = (IsAuthenticated,)
#     queryset = Memorandum.objects.all()
#     serializer_class = InstitutionMemorandumSerializer
#
#
# class MemorandumUpdateDestroyRetrieveView(RetrieveUpdateDestroyAPIView):
#     permission_classes = (IsAuthenticated,)
#     queryset = Memorandum.objects.all()
#     serializer_class = InstitutionMemorandumSerializer
