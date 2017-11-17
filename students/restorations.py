from core.views import ModelRestoreView
from students.models import Student, ResidencyAddressHistory, StudentStudyField
from students.serializers import StudentSerializer, ResidencyAddressHistorySerializer, StudentStudyFieldSerializer


class StudentRestoreView(ModelRestoreView):
    def get_model(self):
        return Student

    def get_serializer_class(self):
        return StudentSerializer


class ResidencyRestoreView(ModelRestoreView):
    def get_model(self):
        return ResidencyAddressHistory

    def get_serializer_class(self):
        return ResidencyAddressHistorySerializer


class StudentStudyFieldRestoreView(ModelRestoreView):
    def get_model(self):
        return StudentStudyField

    def get_serializer_class(self):
        return StudentStudyFieldSerializer