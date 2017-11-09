from django.conf.urls import url
from .views import *
from .deletions import *


student_urls = [
    url(r'students/$', StudentListCreateView.as_view()),
    url(r'students/(?P<pk>(\d+))/$', StudentRetrieveUpdateDestroyView.as_view()),
    url(r'deleted/students/$', DeletedStudentView.as_view()),
    url(r'deleted/students/(?P<pk>(\d+))/$', DeletedStudentUpdateView.as_view()),

]

residency_urls = [
    url(r'students/(?P<student_id>(\d+))/residency/$', ResidencyAddressHistoryListCreateView.as_view()),
    url(r'students/(?P<student_id>(\d+))/residency/(?P<pk>(\d+))/$', ResidencyAddressHistoryRetrieveUpdateDestroyView.as_view()),
    url(r'deleted/residency/$', DeletedResidencyAddressHistoryView.as_view()),
    url(r'deleted/residency/(?P<pk>(\d+))/$', DeletedResidencyAddressHistoryUpdateView.as_view()),

]

studentprogram_urls = [
    url(r'students/(?P<student_id>(\d+))/programs/$', StudentProgramListCreateView.as_view()),
    url(r'students/(?P<student_id>(\d+))/programs/(?P<program_offering_id>(\d+))/$', StudentProgramRetrieveUpdateDestroyView.as_view()),
    url(r'deleted/studentprograms/$', DeletedStudentProgramView.as_view()),
    url(r'deleted/studentprograms/(?P<pk>(\d+))/$', DeletedStudentProgramUpdateView.as_view()),

]