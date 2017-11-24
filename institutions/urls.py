from django.conf.urls import url, include
from .views import *
from .archives import *
from .restorations import *
from students.views import *

institution_urls = [
    url(r'(?P<pk>(\d+))/$', InstitutionUpdateDestroyRetrieveView.as_view()),
    url(r'(?P<institution_id>(\d+))/memorandums/$', MemorandumListCreateView.as_view()),
    url(r'$', InstitutionListCreateView.as_view()),
]

institution_archived_urls = [
    url(r'(?P<pk>(\d+))/restore/$', InstitutionRestoreView.as_view()),
    url(r'(?P<pk>(\d+))/$', ArchivedInstitutionUpdateDeletedView.as_view()),
    url(r'$', ArchivedInstitutionsView.as_view()),
]

memorandum_archived_urls = [
    url(r'(?P<pk>(\d+))/restore/$', MemorandumRestoreView.as_view()),
    url(r'(?P<pk>(\d+))/$', ArchivedMemorandumUpdateDeletedView.as_view()),
    url(r'$', ArchivedMemorandumsView.as_view()),
]

program_archived_urls = [
    url(r'(?P<pk>(\d+))/restore/$', ProgramRestoreView.as_view()),
    url(r'(?P<pk>(\d+))/$', ArchivedProgramUpdateView.as_view()),
    url(r'$', ArchivedProgramsView.as_view()),
]

memorandum_urls = [
    url(r'(?P<pk>(\d+))/$', MemorandumUpdateDestroyRetrieveView.as_view()),
]

program_urls = [
    url(r'inbound/(?P<pk>(\d+))/students/$', InboundStudentProgramListCreateView.as_view()),
    url(r'inbound/$', InboundProgramListCreateView.as_view()),
    url(r'outbound/(?P<outbound_id>(\d+))/requirements/$', RequirementListCreateView.as_view()),
    url(r'outbound/(?P<pk>(\d+))/students/$', OutboundStudentProgramListCreateView.as_view()),
    url(r'outbound/(?P<outbound_program_id>(\d+))/students/(?P<pk>(\d+))/$',
        OutboundStudentProgramRetrieveUpdateDestroyView.as_view()),
    url(r'outbound/$', OutboundProgramListCreateView.as_view()),
    url(r'(?P<pk>(\d+))/$', ProgramRetrieveUpdateDestroyView.as_view()),

]

academic_year_urls = [
    url(r'terms/$', TermListCreateView.as_view()),
    url(r'$', AcademicYearListCreateView.as_view()),
]
