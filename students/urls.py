from django.conf.urls import url
from .views import *
from .archives import *
from .restorations import *

student_urls = [
    url(r'(?P<pk>(\d+))/$', StudentRetrieveUpdateDestroyView.as_view()),
    url(r'(?P<student_id>(\d+))/residency/$', ResidencyAddressHistoryListCreateView.as_view()),
    url(r'(?P<student_id>(\d+))/residency/(?P<pk>(\d+))/$',
        ResidencyAddressHistoryRetrieveUpdateDestroyView.as_view()),
    url(r'(?P<student_id>(\d+))/programs/$', StudentProgramListCreateView.as_view()),
    url(r'(?P<student_id>(\d+))/programs/(?P<study_field_id>(\d+))/$',
        StudentProgramRetrieveUpdateDestroyView.as_view()),
    url(r'$', StudentListCreateView.as_view()),
]

deleted_urls = [
    url(r'studentprograms/$', ArchivedStudentProgramView.as_view()),
    url(r'studentprograms/(?P<pk>(\d+))/$', ArchivedStudentProgramUpdateView.as_view()),
    url(r'studentprograms/(?P<pk>(\d+))/restore/$', StudentRestoreView.as_view()),
    url(r'residency/$', ArchivedResidencyAddressHistoryView.as_view()),
    url(r'residency/(?P<pk>(\d+))/$', ArchivedResidencyAddressHistoryUpdateView.as_view()),
    url(r'residency/(?P<pk>(\d+))/restore/$', ResidencyRestoreView.as_view()),
    url(r'students/$', ArchivedStudentView.as_view()),
    url(r'students/(?P<pk>(\d+))/$', ArchivedStudentUpdateView.as_view()),
    url(r'students/(?P<pk>(\d+))/restore/$', StudentProgramRestoreView.as_view()),
]
