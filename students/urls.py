from django.conf.urls import url
from .views import *
from .deletions import *
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
    url(r'studentprograms/$', DeletedStudentProgramView.as_view()),
    url(r'studentprograms/(?P<pk>(\d+))/$', DeletedStudentProgramUpdateView.as_view()),
    url(r'studentprograms/(?P<pk>(\d+))/restore/$', StudentRestoreView.as_view()),
    url(r'residency/$', DeletedResidencyAddressHistoryView.as_view()),
    url(r'residency/(?P<pk>(\d+))/$', DeletedResidencyAddressHistoryUpdateView.as_view()),
    url(r'residency/(?P<pk>(\d+))/restore/$', ResidencyRestoreView.as_view()),
    url(r'students/$', DeletedStudentView.as_view()),
    url(r'students/(?P<pk>(\d+))/$', DeletedStudentUpdateView.as_view()),
    url(r'students/(?P<pk>(\d+))/restore/$', StudentProgramRestoreView.as_view()),
]
