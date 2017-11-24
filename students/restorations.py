from core.views import ModelRestoreView
from students.models import Student, ResidencyAddressHistory
from students.serializers import StudentSerializer, ResidencyAddressHistorySerializer


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