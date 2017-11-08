from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from students.serializers import *
from students.models import *


class StudentListCreateView(ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get_serializer(self, *args, **kwargs):
        kwargs['partial'] = True
        return super(StudentRetrieveUpdateDestroyView, self).get_serializer(*args, **kwargs)

    def get_queryset(self):
        student = self.kwargs['pk']
        return Student.objects.filter(pk=student)


class ResidencyAddressHistoryListCreateView(ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = ResidencyAddressHistory.objects.all()
    serializer_class = ResidencyAddressHistorySerializer
    lookup_field = 'student_id'

    def get_queryset(self):
        student = self.kwargs['student_id']
        return ResidencyAddressHistory.objects.filter(student=student)


class ResidencyAddressHistoryRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = ResidencyAddressHistory.objects.all()
    serializer_class = ResidencyAddressHistorySerializer
    lookup_field = 'student_id'

    def get_serializer(self, *args, **kwargs):
        kwargs['partial'] = True
        return super(ResidencyAddressHistoryRetrieveUpdateDestroyView, self).get_serializer(*args, **kwargs)

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


class StudentProgramRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = StudentProgram.objects.all()
    serializer_class = StudentProgramSerializer
    lookup_field = 'student_id'

    def get_serializer(self, *args, **kwargs):
        kwargs['partial'] = True
        return super(StudentProgramRetrieveUpdateDestroyView, self).get_serializer(*args, **kwargs)

    def get_queryset(self):
        student = self.kwargs['student_id']
        program_offering = self.kwargs['program_offering_id']
        return StudentProgram.objects.filter(student=student, program_offering=program_offering)


class StudentBinView(ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Student.all_objects.exclude(deleted_at=None)
    serializer_class = StudentSerializer


class ResidencyAddressHistoryBinView(ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = ResidencyAddressHistory.all_objects.exclude(deleted_at=None)
    serializer_class = ResidencyAddressHistorySerializer


class StudentProgramBinView(ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = StudentProgram.all_objects.exclude(deleted_at=None)
    serializer_class = StudentProgramSerializer
