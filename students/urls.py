from django.conf.urls import url
from .views import *
from .deletions import *


student_urls = [
    url(r'students/$', StudentListCreateView.as_view()),
    url(r'students/(?P<pk>(\d+))/$', StudentRetrieveUpdateDestroyView.as_view()),
    url(r'students/bin/$', StudentBinView.as_view()),
    url(r'students/bin/(?P<pk>(\d+))/$', StudentUpdateBinView.as_view()),

]

residency_urls = [
    url(r'students/(?P<student_id>(\d+))/residency/$', ResidencyAddressHistoryListCreateView.as_view()),
    url(r'students/(?P<student_id>(\d+))/residency/(?P<pk>(\d+))/$', ResidencyAddressHistoryRetrieveUpdateDestroyView.as_view()),
    url(r'residency/bin/$', ResidencyAddressHistoryBinView.as_view()),
    url(r'residency/bin/(?P<pk>(\d+))/$', ResidencyAddressHistoryUpdateBinView.as_view()),

]

studentprogram_urls = [
    url(r'students/(?P<student_id>(\d+))/programs/$', StudentProgramListCreateView.as_view()),
    url(r'students/(?P<student_id>(\d+))/programs/(?P<program_offering_id>(\d+))/$', StudentProgramRetrieveUpdateDestroyView.as_view()),
    url(r'studentprograms/bin/$', StudentProgramBinView.as_view()),
    url(r'studentprograms/bin/(?P<pk>(\d+))/$', StudentProgramUpdateBinView.as_view()),

]