from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from students.serializers import *
from students.models import *


class ArchivedStudentView(ListAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Student.archived.all()
    serializer_class = StudentSerializer


class ArchivedStudentUpdateView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Student.archived.all()
    serializer_class = StudentSerializer

    def get_serializer(self, *args, **kwargs):
        kwargs['partial'] = True
        return super(ArchivedStudentUpdateView, self).get_serializer(*args, **kwargs)


class ArchivedResidencyAddressHistoryView(ListAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = ResidencyAddressHistory.archived.all()
    serializer_class = ResidencyAddressHistorySerializer


class ArchivedResidencyAddressHistoryUpdateView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = ResidencyAddressHistory.archived.all()
    serializer_class = ResidencyAddressHistorySerializer

    def get_serializer(self, *args, **kwargs):
        kwargs['partial'] = True
        return super(ArchivedResidencyAddressHistoryUpdateView, self).get_serializer(*args, **kwargs)


class ArchivedStudentStudyFieldView(ListAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = StudentProgram.archived.all()
    serializer_class = StudentProgramSerializer


class ArchivedStudentProgramUpdateView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = StudentProgram.archived.all()
    serializer_class = StudentProgramSerializer

    def get_serializer(self, *args, **kwargs):
        kwargs['partial'] = True
        return super(ArchivedStudentProgramUpdateView, self).get_serializer(*args, **kwargs)

