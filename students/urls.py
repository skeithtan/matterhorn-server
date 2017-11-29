from django.conf.urls import url, include
from .views import *
from .archives import *
from .restorations import *

student_urls = [
    url(r'(?P<student_id>(\d+))/residency/(?P<pk>(\d+))/$',
        ResidencyAddressHistoryRetrieveUpdateDestroyView.as_view()),
    url(r'(?P<pk>(\d+))/$', StudentRetrieveUpdateDestroyView.as_view()),
    url(r'(?P<student_id>(\d+))/residency/$', ResidencyAddressHistoryListCreateView.as_view()),
    url(r'$', StudentListCreateView.as_view()),
]

student_archived_urls = [
    url(r'(?P<pk>(\d+))/restore/$', StudentRestoreView.as_view()),
    url(r'(?P<pk>(\d+))/$', ArchivedStudentUpdateView.as_view()),
    url(r'$', ArchivedStudentView.as_view()),
]

student_programs_archived_urls = [
    # url(r'(?P<pk>(\d+))/restore/$', StudentProgramRestoreView.as_view()),
    # url(r'(?P<pk>(\d+))/$', ArchivedStudentProgramUpdateView.as_view()),
    # url(r'$', ArchivedStudentStudyFieldView.as_view()),
]

residency_archived_urls = [
    url(r'(?P<pk>(\d+))/restore/$', ResidencyRestoreView.as_view()),
    url(r'(?P<pk>(\d+))/$', ArchivedResidencyAddressHistoryUpdateView.as_view()),
    url(r'$', ArchivedResidencyAddressHistoryView.as_view()),
]
